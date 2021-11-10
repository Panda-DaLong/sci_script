from simtk.openmm.app import *
from simtk.openmm import *
from simtk.unit import *
import time


def output_time(f):
    now = time.localtime()
    now_format = time.strftime("%Y-%m-%d-%H_%M_%S", now) 
    print(now_format, file=f)


Topology.loadBondDefinitions('cha_modi.temp')
Topology.loadBondDefinitions('dopc.temp')

pdb = PDBFile('smaller_system_2b.pdb')
forcefield = ForceField('hea-ch3.xml', 'mid-ch3.xml', 'tai-ch3.xml', 'conect.xml', 'dopc.xml', 'amoeba2013.xml')

system = forcefield.createSystem(pdb.topology, nonbondedMethod=PME,
        nonbondedCutoff=1*nanometer, vdwCutoff=1.2*nanometer, constraints=HBonds,
        polarisation='mutual', mutualInducedTargetEpsilon=0.00001)
system.addForce(AndersenThermostat(300*kelvin, 1/picosecond))
system.addForce(MonteCarloBarostat(1*bar, 300*kelvin))
integrator = VerletIntegrator(0.002*picoseconds)

platform = Platform.getPlatformByName('CPU')
simulation = Simulation(pdb.topology, system, integrator, platform)
simulation.context.setPositions(pdb.positions)

with open('openmm_out', 'a') as f:
    print('Start minimizing', file=f)
    output_time(f)

simulation.minimizeEnergy()

with open('openmm_out', 'a') as f:
    print('End minimizing', file=f)
    output_time(f)

positions = simulation.context.getState(getPositions=True).getPositions()
PDBFile.writeFile(simulation.topology, positions, open('min_output.pdb', 'w'))

