import sys
import numpy as np
import MDAnalysis as mda
from lipyphilic.lib.assign_leaflets import AssignLeaflets
from lipyphilic.lib.memb_thickness import MembThickness


#In_File:
#box_file is pbc_box file which is an out_file of OpenMM
box_file = sys.argv[1]
#tra_trans_file is trajectory file from mdana_membrane_center.py 
tra_trans_file = sys.argv[2]


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
u = mda.Universe(tra_trans_file)

for ts in u.trajectory:
    ts.dimensions = all_box_dim[u.trajectory.frame]


#Part_3:
leaflets = AssignLeaflets(
    universe=u,
    lipid_sel="name P" 
    )

leaflets.run()


memb_thickness = MembThickness(
    universe=u,
    leaflets=leaflets.leaflets,
    lipid_sel="name P"
    )

memb_thickness.run()

print('the thickness of membrane is', memb_thickness.memb_thickness, 'angstrom')

