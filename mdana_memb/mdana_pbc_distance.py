import sys
import numpy as np
import MDAnalysis as mda
from MDAnalysis.analysis import distances


#box_file is pbc_box file which is an out_file of OpenMM
box_file = sys.argv[1]
#tra_file is trajectory file which is an out_file of OpenMM
tra_file = sys.argv[2]


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


u = mda.Universe(tra_file)
        

u.trajectory.add_transformations(set_box)


ag_cha_K = u.select_atoms('resname cha and chainID K')
ag_cha_L = u.select_atoms('resname cha and chainID L')
ag_cha_M = u.select_atoms('resname cha and chainID M')
ag_cha_N = u.select_atoms('resname cha and chainID N')

distance_KL_tra = []
distance_LM_tra = []
distance_MN_tra = []


for ts in u.trajectory:

    center_ag_cha_K = ag_cha_K.center_of_mass(pbc=True, compound='residues')
    center_ag_cha_L = ag_cha_L.center_of_mass(pbc=True, compound='residues')
    center_ag_cha_M = ag_cha_M.center_of_mass(pbc=True, compound='residues')
    center_ag_cha_N = ag_cha_N.center_of_mass(pbc=True, compound='residues')

    dist_arr_KL = distances.distance_array(center_ag_cha_K, center_ag_cha_L, box=u.dimensions)
    dist_arr_LM = distances.distance_array(center_ag_cha_L, center_ag_cha_M, box=u.dimensions)
    dist_arr_MN = distances.distance_array(center_ag_cha_M, center_ag_cha_N, box=u.dimensions)

    distance_KL_tra.append(float(dist_arr_KL))
    distance_LM_tra.append(float(dist_arr_LM))
    distance_MN_tra.append(float(dist_arr_MN))


#save distance_KL_tra
arr_distance_KL_tra = np.array(distance_KL_tra)
np.save('distance_KL_tra.npy', arr_distance_KL_tra)
np.savetxt('distance_KL_tra.txt', arr_distance_KL_tra)

#save distance_LM_tra
arr_distance_LM_tra = np.array(distance_LM_tra)
np.save('distance_LM_tra.npy', arr_distance_LM_tra)
np.savetxt('distance_LM_tra.txt', arr_distance_LM_tra)

#save distance_MN_tra
arr_distance_MN_tra = np.array(distance_MN_tra)
np.save('distance_MN_tra.npy', arr_distance_MN_tra)
np.savetxt('distance_MN_tra.txt', arr_distance_MN_tra)

