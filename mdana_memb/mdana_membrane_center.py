import sys
import numpy as np
import MDAnalysis as mda
from MDAnalysis import transformations as trans


#In_File:
#box_file is pbc_box file which is an out_file of OpenMM
box_file = sys.argv[1]
#tra_file is trajectory file which is an out_file of OpenMM
tra_file = sys.argv[2]

#Out_File:
cen_file = 'center_npt_2.pdb'


#Part_1:
def grep_box_dim(str1):

    lst1 = str1.split()

    box_x_nm = lst1[2][8:-1]
    box_y_nm = lst1[6][2:-1]
    box_z_nm = lst1[10][2:-2]

    box_nm = []
    for i in [box_x_nm, box_y_nm, box_z_nm]:
        box_nm.append(float(i))
    
    box_nm = np.array(box_nm)

    box_angstrom = box_nm * 10

    box_direct = np.array((90, 90, 90))

    box_dim = np.concatenate((box_angstrom, box_direct))

    return box_dim


all_box_dim = []

with open(box_file) as f:
    
    #skip box_dim of step 0
    line = f.readline()

    for line in f:

        box_dim = grep_box_dim(line)

        all_box_dim.append(box_dim)


#Part_2:
u = mda.Universe(tra_file, in_memory=True)

ag_all = u.atoms

ag_water = u.select_atoms('resname HOH')


with mda.Writer(cen_file, ag_all.n_atoms) as w:

    for ts in u.trajectory:

        water_center = ag_water.center_of_mass()

        box_bottom = all_box_dim[u.trajectory.frame][0:3]
       
        ag_all.translate(box_bottom - water_center)

        #Wrap not_cha_b
        ts.dimensions = all_box_dim[u.trajectory.frame]

        ag_all.wrap(compound='residues')

        #Write out
        w.write(u)

