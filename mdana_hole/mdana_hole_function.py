import sys
import MDAnalysis as mda
from MDAnalysis.analysis import hole2


#in_file is a pdb file
in_file = sys.argv[1]


# to compute the center of channel as a param of hole function
u = mda.Universe(in_file)

ag_cha = u.select_atoms('resname cha')

cha_center = ag_cha.center_of_mass()


# to use HOLE with the in_file
profiles = hole2.hole(in_file,
        executable='~/hole2/exe/hole', 
        cpoint=cha_center,
        cvect=[0, 0, 1],
        ignore_residues=['DOP', 'HOH'])


# to create a VMD surface of the pore
hole2.create_vmd_surface(filename='hole.vmd', sph_process='~/hole2/exe/sph_process')

