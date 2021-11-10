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

system.addForce(AndersenThermostat(300*kelvin, 1/picosecond))
system.addForce(MonteCarloAnisotropicBarostat(Vec3(1.0,1.0,1.0), 300))


integrator = VerletIntegrator(0.001*picoseconds)

platform = Platform.getPlatformByName('CUDA')
properties = {'Precision': 'single', 'DeviceIndex': '0'}

simulation = Simulation(top.topology, system, integrator, platform, properties)
simulation.context.setPositions(pdb.positions)


#Load chk_file
npt_out_name_old = 'npt_3'

with open(f'./md_out/{npt_out_name_old}.chk', 'rb') as f:
    simulation.context.loadCheckpoint(f.read())


#NPT
npt_out_name = 'npt_4'
npt_step = 1000000
npt_range = 500

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

