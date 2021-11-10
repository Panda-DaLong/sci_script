from simtk.openmm.app import *
from simtk.openmm import *
from simtk.unit import *
import time
import os


def output_time(f):
    now = time.localtime()
    now_format = time.strftime("%Y-%m-%d-%H_%M_%S", now)
    print(now_format, file=f)


if not os.path.exists('md_out'):
    os.mkdir('md_out')


pdb = PDBFile('pure_bilayer_ini.pdb')

a, b, c = Vec3(5.0130, 0.0, 0.0), Vec3(0.0, 5.0120, 0.0), Vec3(0.0, 0.0, 6.8030)
top = GromacsTopFile('topol.top', periodicBoxVectors = (a, b, c),
        includeDir = os.getcwd())

system = top.createSystem(nonbondedMethod=PME, nonbondedCutoff=1*nanometer,
        constraints=HBonds)

system.addForce(AndersenThermostat(310*kelvin, 1/picosecond))
system.addForce(MonteCarloAnisotropicBarostat(Vec3(1.0,1.0,1.0), 310))


#add restraint
dopc_head = ('C11','C12','C13','C14','C15','N','O12','O13','O14','P')

res1 = CustomExternalForce("k1 * periodicdistance(x0,y0,z,x0,y0,z0)^2")
res1.addGlobalParameter("k1", 10.0*kilocalories_per_mole/angstroms**2)
res1.addPerParticleParameter("x0")
res1.addPerParticleParameter("y0")
res1.addPerParticleParameter("z0")

res2 = CustomExternalForce("k2 * periodicdistance(x0,y0,z,x0,y0,z0)^2")
res2.addGlobalParameter("k2", 5.0*kilocalories_per_mole/angstroms**2)
res2.addPerParticleParameter("x0")
res2.addPerParticleParameter("y0")
res2.addPerParticleParameter("z0")

for atm in pdb.getTopology().atoms():

    if atm.residue.name == 'cha':
        res1.addParticle(atm.index, pdb.getPositions()[atm.index])
    
    elif atm.residue.name == 'DOPC' and atm.name in dopc_head:
        res1.addParticle(atm.index, pdb.getPositions()[atm.index])

    else:
        res2.addParticle(atm.index, pdb.getPositions()[atm.index])

system.addForce(res1)
system.addForce(res2)


integrator = VerletIntegrator(0.001*picoseconds)

platform = Platform.getPlatformByName('CUDA')
properties = {'Precision': 'single', 'DeviceIndex': '0'}

simulation = Simulation(top.topology, system, integrator, platform, properties)
simulation.context.setPositions(pdb.positions)


#MIN...
with open('./md_out/min.log', 'w') as f:
    print('Start minimizing', file=f)
    output_time(f)

simulation.minimizeEnergy()

with open('./md_out/min.log', 'a') as f:
    print('End minimizing', file=f)
    output_time(f)

positions = simulation.context.getState(getPositions=True).getPositions()
PDBFile.writeFile(simulation.topology, positions, open('./md_out/min_output.pdb', 'w'))


#NPT
npt_out_name = 'npt_1'
npt_step = 1000000
npt_range = 10

simulation.reporters.append(PDBReporter(f'./md_out/{npt_out_name}.pdb', npt_step))
simulation.reporters.append(StateDataReporter(file=f'./md_out/{npt_out_name}.log',
                            reportInterval=npt_step, step=True, time=True,
                            potentialEnergy=True, kineticEnergy=True, totalEnergy=True,
                            temperature=True, volume=True, density=True, speed=True))

with open(f'./md_out/{npt_out_name}.box', 'w') as f:
    print('step 0:', simulation.context.getState().getPeriodicBoxVectors(), file=f)

for i in range(npt_range):
    simulation.step(npt_step)
    with open(f'./md_out/{npt_out_name}.box', 'a') as f:
        print(f'step {npt_step * (i+1)}:', simulation.context.getState().getPeriodicBoxVectors(), file=f)


with open(f'./md_out/{npt_out_name}.chk', 'wb') as f:
    f.write(simulation.context.createCheckpoint())

