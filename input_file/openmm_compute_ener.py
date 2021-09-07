from simtk.openmm.app import *
from simtk.openmm import *
from simtk.unit import *


Topology.loadBondDefinitions('cha_modi.temp')

pdb = PDBFile('cha_modi.pdb')
forcefield = ForceField('hea-ch3.xml', 'mid-ch3.xml', 'tai-ch3.xml', 'conect.xml')


system = forcefield.createSystem(pdb.topology, nonbondedMethod=PME,
        nonbondedCutoff=1*nanometer, vdwCutoff=1.2*nanometer, constraints=HBonds,
        polarisation='mutual', mutualInducedTargetEpsilon=0.00001)

system.addForce(AndersenThermostat(300*kelvin, 1/picosecond))
system.addForce(MonteCarloBarostat(1*bar, 300*kelvin))

integrator = VerletIntegrator(0.002*picoseconds)

platform = Platform.getPlatformByName('CPU')
simulation = Simulation(pdb.topology, system, integrator, platform)

simulation.context.setPositions(pdb.positions)


state = simulation.context.getState(getEnergy=True)
print(state.getPotentialEnergy())

