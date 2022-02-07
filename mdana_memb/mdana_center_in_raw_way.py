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

def translate_array(center_position, atom_position, pbc, axis_direction):
    trans_arr = [0, 0, 0]
    pbc_half = pbc / 2
    for axis_direction in [0, 1, 2]:
        if atom_position[axis_direction] > center_position[axis_direction] + pbc_half[axis_direction]:
            trans_arr[axis_direction] = -pbc[axis_direction]
        elif atom_position[axis_direction] < center_position[axis_direction] - pbc_half[axis_direction]:
            trans_arr[axis_direction] = +pbc[axis_direction]
    return trans_arr


u = mda.Universe(tra_file)

workflow = [set_box,
            trans.wrap(u.atoms, compound='residues')]

u.trajectory.add_transformations(*workflow)

'''
ag_cha_L = u.select_atoms('resname cha and chainID L')


pbc = u.dimensions
pbc_half = pbc / 2
center_position = ag_cha_L.center_of_mass()

print(pbc)
print(center_position)

#if ag_center < pbc_half:
#   refer = ag_center + pbc_half 
#   if x < refer:
#       x += pbc_half - ag_center
#   elif x > refer:
#       x += -pbc_half - ag_center
#elif ag_center > pbc_half:
#    refer = ag_center - pbc_half
#    if x < refer:
#        x += 3 * pbc_half - ag_center
#    elif x > refer:
#        x += pbc_half - ag_center

if center_position[0] < pbc_half[0]:
    x_coor_refer = center_position[0] + pbc_half[0]

    x_trans_1 = pbc_half[0] - center_position[0]
    x_trans_2 = -pbc_half[0] - center_position[0]

elif center_position[0] > pbc_half[0]:
    x_coor_refer = center_position[0] - pbc_half[0]

    x_trans_1 = 3 * pbc_half[0] - center_position[0]
    x_trans_2 = pbc_half[0] - center_position[0]


if center_position[1] < pbc_half[1]:
    y_coor_refer = center_position[1] + pbc_half[1]

    y_trans_1 = pbc_half[1] - center_position[1]
    y_trans_2 = -pbc_half[1] - center_position[1]

elif center_position[1] > pbc_half[1]:
    y_coor_refer = center_position[1] - pbc_half[1]

    y_trans_1 = 3 * pbc_half[1] - center_position[1]
    y_trans_2 = pbc_half[1] - center_position[1]


if center_position[2] < pbc_half[2]:
    z_coor_refer = center_position[2] + pbc_half[2]

    z_trans_1 = pbc_half[2] - center_position[2]
    z_trans_2 = -pbc_half[2] - center_position[2]

elif center_position[2] > pbc_half[2]:
    z_coor_refer = center_position[2] - pbc_half[2]

    z_trans_1 = 3 * pbc_half[2] - center_position[2]
    z_trans_2 = pbc_half[2] - center_position[2]

print(x_coor_refer, x_trans_1, x_trans_2)
print(y_coor_refer, y_trans_1, y_trans_2)
print(z_coor_refer, z_trans_1, z_trans_2)

x_coor_sele = {'prop x <= {}'.format(x_coor_refer): np.array([x_trans_1, 0, 0]), 'prop x >= {}'.format(x_coor_refer): np.array([x_trans_2, 0, 0])}
y_coor_sele = {'prop y <= {}'.format(y_coor_refer): np.array([0, y_trans_1, 0]), 'prop y >= {}'.format(y_coor_refer): np.array([0, y_trans_2, 0])}
z_coor_sele = {'prop z <= {}'.format(z_coor_refer): np.array([0, 0, z_trans_1]), 'prop z >= {}'.format(z_coor_refer): np.array([0, 0, z_trans_2])}


i = 1

for x in x_coor_sele.keys():
    for y in y_coor_sele.keys():
        for z in z_coor_sele.keys():
            
            print(str(i) * 10)

            ag = u.select_atoms(x + ' and ' + y + ' and ' + z)     
           
            trans_arr = x_coor_sele[x] + y_coor_sele[y] + z_coor_sele[z]
                        
            ag.translate(trans_arr)

            print('*' * 10)
            i = i + 1
'''

with mda.Writer(cen_file, u.atoms.n_atoms) as w:
#    for ts in u.trajectory:
    w.write(u)

#有些原子在盒子外面，导致变换出错
#把原子wrap到盒子里以后，计算通道单体质心却又出错了，因为一个单体被分成了在盒子各个角的几部分
#还是用tcl脚本最老的办法，居中的螺旋单体保持不动，平移其他的，体系不必在盒子里
#实在不行就还是同tcl脚本来去周期，抓紧分析HOLE