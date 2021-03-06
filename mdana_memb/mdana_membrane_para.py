import sys
import numpy as np
import MDAnalysis as mda
from MDAnalysis.analysis.leaflet import LeafletFinder, optimize_cutoff


#in_file is a structure or trajectory file of membrane 
in_file = sys.argv[1]


u = mda.Universe(in_file)

L = LeafletFinder(u, 'name P', cutoff=15.0, pbc=False)

l0 = L.groups(0)
l1 = L.groups(1)

print(l0.residues)
print()
print(l1.residues) 
print()

#the thickness of membrane
t_mem = np.abs((l1.centroid() - l0.centroid())[2])

#the z-coordinate of the center of membrane
z_mem = 0.5 * (l1.centroid() + l0.centroid())[2]

print('the thickness of membrane is', t_mem, 'angstrom')
print()
print('the z-coordinate of the center of membrane is', z_mem, 'angstrom')

