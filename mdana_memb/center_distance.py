import sys
import numpy as np
import MDAnalysis as mda
import matplotlib.pyplot as plt


tra_file = sys.argv[1]


def dist(vec1, vec2):
    distance = np.sqrt(np.sum(np.square(vec1 - vec2)))
    return distance


u = mda.Universe(tra_file)


ag_cha_K = u.select_atoms('resname cha and chainID K')
ag_cha_L = u.select_atoms('resname cha and chainID L')
ag_cha_M = u.select_atoms('resname cha and chainID M')
ag_cha_N = u.select_atoms('resname cha and chainID N')

distance_KL_tra = []
distance_LM_tra = []
distance_MN_tra = []


for ts in u.trajectory:

    center_ag_cha_K = ag_cha_K.center_of_mass()
    center_ag_cha_L = ag_cha_L.center_of_mass()
    center_ag_cha_M = ag_cha_M.center_of_mass()
    center_ag_cha_N = ag_cha_N.center_of_mass()

    distance_KL = dist(center_ag_cha_K, center_ag_cha_L)
    distance_LM = dist(center_ag_cha_L, center_ag_cha_M)
    distance_MN = dist(center_ag_cha_M, center_ag_cha_N)
    
    distance_KL_tra.append(distance_KL)
    distance_LM_tra.append(distance_LM)
    distance_MN_tra.append(distance_MN)


#plot distance_KL_tra
x1 = np.linspace(0, 10000, num=len(distance_KL_tra))
y1 = np.array(distance_KL_tra)

plt.figure(num=1)
plt.plot(x1, y1)

plt.xlabel('time')
plt.ylabel('distance')
plt.title('distance_KL_tra')
plt.savefig('distance_KL_tra.png')

#plot distance_LM_tra
x2 = np.linspace(0, 10000, num=len(distance_LM_tra))
y2 = np.array(distance_LM_tra)

plt.figure(num=2)
plt.plot(x2, y2)

plt.xlabel('time')
plt.ylabel('distance')
plt.title('distance_LM_tra')
plt.savefig('distance_LM_tra.png')

#plot distance_MN_tra
x3 = np.linspace(0, 10000, num=len(distance_MN_tra))
y3 = np.array(distance_MN_tra)

plt.figure(num=3)
plt.plot(x3, y3)

plt.xlabel('time')
plt.ylabel('distance')
plt.title('distance_MN_tra')
plt.savefig('distance_MN_tra.png')

