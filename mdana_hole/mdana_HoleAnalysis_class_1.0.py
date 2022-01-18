import sys
import MDAnalysis as mda
from MDAnalysis.analysis import hole2


#in_file is a pdb file
in_file = sys.argv[1]


u = mda.Universe(in_file)


# to compute the normal vector of channel as a param of hole class
ag_cha_K = u.select_atoms('resname cha and chainID K')
ag_cha_N = u.select_atoms('resname cha and chainID N')

center_ag_cha_K = ag_cha_K.center_of_mass()
center_ag_cha_N = ag_cha_N.center_of_mass()

channel_normal_vector = center_ag_cha_K - center_ag_cha_N


# to use HOLE with the in_file
h2 = hole2.HoleAnalysis(u, 
        executable='~/hole2/exe/hole', 
        select='resname cha',
        cpoint='center_of_geometry',
        cvect=channel_normal_vector,
        ignore_residues=['DOP', 'HOH'],
        sample=0.1)

h2.run()


# to create a VMD surface of the pore
h2.create_vmd_surface(filename='hole.vmd')

h2.delete_temporary_files()
