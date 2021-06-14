from simtk.openmm.app import *
from simtk.openmm import *
from simtk.unit import *
from sys import stdout

pdb = PDBFile('dopc.pdb')
forcefield = ForceField('dopc.xml')

system = forcefield.createSystem(pdb.topology, nonbondedMethod=PME,
        nonbondedCutoff=1*nanometer, vdwCutoff=1.2*nanometer, constraints=HBonds,
        polarisation='mutual', mutualInducedTargetEpsilon=0.00001)
integrator = VerletIntegrator(0.002*picoseconds)

platform = Platform.getPlatformByName('CUDA')
properties = {"CudaPrecision": 'single', "CudaDeviceIndex": '0'}
simulation = Simulation(pdb.topology, system, integrator, platform, properties)
simulation.context.setPositions(pdb.positions)

simulation.minimizeEnergy()

simulation.reporters.append(PDBReporter('output.pdb', 10000))
simulation.reporters.append(StateDataReporter('min.log', 10000, step=True,
        potentialEnergy=True, temperature=True))
simulation.step(100000)
