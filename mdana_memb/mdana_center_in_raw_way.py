import sys
import numpy as np
import MDAnalysis as mda


#In_File:
#box_file is pbc_box file which is an out_file of OpenMM
box_file = sys.argv[1]
#tra_file is trajectory file which is an out_file of OpenMM
tra_file = sys.argv[2]

#Out_File:
cen_file = sys.argv[3]


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
def set_box(ts):
    ts.dimensions = all_box_dim[ts.frame]
    return ts

def pbc_transform_atom(center_position, atom_position, pbc, axis_direction):
    pbc_half = pbc / 2
    if atom_position[axis_direction] > center_position[axis_direction] + pbc_half[axis_direction]:
        return atom_position[axis_direction] - pbc[axis_direction]
    elif atom_position[axis_direction] < center_position[axis_direction] - pbc_half[axis_direction]:
        return atom_position[axis_direction] + pbc[axis_direction]


u = mda.Universe(tra_file)

u.trajectory.add_transformations(set_box)

ag_cha_L = u.select_atoms('resname cha and chainID L')


for ts in u.trajectory:
    print('**************')
    print(ts.dimensions)

    center_ag_cha_L = ag_cha_L.center_of_mass()
    print(center_ag_cha_L)

prop [abs] property operator value
与（中心+盒子一半）做比较，选中不同的区域作为原子组，对该原子组做translate变换

    for atom in u.atoms:
        print('@@@@@')
        print(atom.name)
        print(atom.position)

#        for axis_direction in [0, 1, 2]:
#            atom.position[axis_direction] = pbc_transform_atom(center_ag_cha_L, atom.position, ts.dimensions, axis_direction)
#            atom.position[axis_direction] = 999

#        atom.translate([-999, 0, 0])
        print(atom.position)
        print('$$$$$')
    
    print('**************')

#with mda.Writer(cen_file, u.atoms.n_atoms) as w:
#    for ts in u.trajectory:
#        w.write(u)
