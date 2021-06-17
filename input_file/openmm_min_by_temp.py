from simtk.openmm.app import *
from simtk.openmm import *
from simtk.unit import *
from sys import stdout

Topology.loadBondDefinitions('dopc_temp.xml')
#dopc_temp.xml is a template for dopc which is a customized residue
#Topology.loadBondDefinitions() must be before PDBFile()

pdb = PDBFile('dopc_4.pdb')

forcefield = ForceField('dopc.xml')

system = forcefield.createSystem(pdb.topology, nonbondedMethod=PME,
        nonbondedCutoff=1*nanometer, vdwCutoff=1.2*nanometer, constraints=HBonds,
        polarisation='mutual', mutualInducedTargetEpsilon=0.00001)

integrator = VerletIntegrator(0.002*picoseconds)

platform = Platform.getPlatformByName('CUDA')
properties = {"CudaPrecision": 'single', "DeviceIndex": '0'}

simulation = Simulation(pdb.topology, system, integrator, platform, properties)
simulation.context.setPositions(pdb.positions)

simulation.minimizeEnergy()

simulation.reporters.append(PDBReporter('output.pdb', 1000))
simulation.reporters.append(StateDataReporter('min.log', 1000, step=True,
        potentialEnergy=True, temperature=True))
simulation.step(10000)
