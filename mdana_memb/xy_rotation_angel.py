import sys
import math
import numpy as np
import MDAnalysis as mda
from MDAnalysis import transformations as trans
import matplotlib.pyplot as plt


tra_file = sys.argv[1]


def vector_angle_360(vec1, vec2):
    
    x1 = vec1[0]
    y1 = vec1[1]
    x2 = vec2[0]
    y2 = vec2[1]
    
    dot = x1*x2 + y1*y2      # dot product
    det = x1*y2 - y1*x2      # determinant
    angle = math.atan2(det, dot)  # atan2(y, x) or atan2(sin, cos)
    
    angle_in_degree = math.degrees(angle)

    return angle_in_degree


u = mda.Universe(tra_file)


ag_cha_K = u.select_atoms('resname cha and chainID K')
ag_cha_L = u.select_atoms('resname cha and chainID L')
ag_cha_M = u.select_atoms('resname cha and chainID M')
ag_cha_N = u.select_atoms('resname cha and chainID N')

rotation_angel_K_L_tra = []
rotation_angel_L_M_tra = []
rotation_angel_M_N_tra = []


for ts in u.trajectory:

    center_ag_cha_K = ag_cha_K.center_of_mass()
    center_ag_cha_L = ag_cha_L.center_of_mass()
    center_ag_cha_M = ag_cha_M.center_of_mass()
    center_ag_cha_N = ag_cha_N.center_of_mass()
   
    ag_cha_K.translate(-center_ag_cha_K)
    ag_cha_L.translate(-center_ag_cha_L)
    ag_cha_M.translate(-center_ag_cha_M)
    ag_cha_N.translate(-center_ag_cha_N)
    
    rotation_angel_K_L = []
    rotation_angel_L_M = []
    rotation_angel_M_N = []

    for atom_K in ag_cha_K:
        for atom_L in ag_cha_L:
            if atom_K.element in ['C', 'N', 'O'] and atom_K.name == atom_L.name:
                
                atom_K_xy = atom_K.position[:2]
                atom_L_xy = atom_L.position[:2]

                angle_K_L = vector_angle_360(atom_K_xy, atom_L_xy)
                rotation_angel_K_L.append(angle_K_L)

    for atom_L in ag_cha_L:
        for atom_M in ag_cha_M:
            if atom_L.element in ['C', 'N', 'O'] and atom_L.name == atom_M.name:

                atom_L_xy = atom_L.position[:2]
                atom_M_xy = atom_M.position[:2]

                angle_L_M = vector_angle_360(atom_L_xy, atom_M_xy)
                rotation_angel_L_M.append(angle_L_M)
    
    for atom_M in ag_cha_M:
        for atom_N in ag_cha_N:
            if atom_M.element in ['C', 'N', 'O'] and atom_M.name == atom_N.name:
                
                atom_M_xy = atom_M.position[:2]
                atom_N_xy = atom_N.position[:2]

                angle_M_N = vector_angle_360(atom_M_xy, atom_N_xy)
                rotation_angel_M_N.append(angle_M_N)

    rotation_angel_K_L_tra.append(np.mean(rotation_angel_K_L))
    rotation_angel_L_M_tra.append(np.mean(rotation_angel_L_M))
    rotation_angel_M_N_tra.append(np.mean(rotation_angel_M_N))


#plot rotation_angel_K_L_tra
x1 = np.linspace(0, 10000, num=len(rotation_angel_K_L_tra))
y1 = np.array(rotation_angel_K_L_tra)

plt.figure(num=1)
plt.plot(x1, y1)

plt.xlabel('time')
plt.ylabel('rotation_angel')
plt.title('rotation_angel_K_L_tra')
plt.savefig('rotation_angel_K_L_tra.png')

#plot rotation_angel_L_M_tra
x1 = np.linspace(0, 10000, num=len(rotation_angel_L_M_tra))
y1 = np.array(rotation_angel_L_M_tra)

plt.figure(num=2)
plt.plot(x1, y1) 

plt.xlabel('time')
plt.ylabel('rotation_angel')
plt.title('rotation_angel_L_M_tra')
plt.savefig('rotation_angel_L_M_tra.png')

#plot rotation_angel_M_N_tra
x1 = np.linspace(0, 10000, num=len(rotation_angel_M_N_tra))
y1 = np.array(rotation_angel_M_N_tra)

plt.figure(num=3)
plt.plot(x1, y1)

plt.xlabel('time')
plt.ylabel('rotation_angel')
plt.title('rotation_angel_M_N_tra')
plt.savefig('rotation_angel_M_N_tra.png')

