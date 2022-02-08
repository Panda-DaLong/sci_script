import sys
import math
import numpy as np
import numpy.linalg as la
import MDAnalysis as mda
import matplotlib.pyplot as plt


def tilt_angel(channel_normal_vector):
    z_axis=np.array([0,0,1])

    cos_angel = np.dot(channel_normal_vector, z_axis)
    sin_angel = la.norm(np.cross(channel_normal_vector, z_axis))

    angel_in_radian = np.arctan2(sin_angel, cos_angel)
    angle_in_degree = math.degrees(angel_in_radian)

    return angle_in_degree


tra_file = sys.argv[1]


u = mda.Universe(tra_file)

ag_cha_K = u.select_atoms('resname cha and chainID K')
ag_cha_N = u.select_atoms('resname cha and chainID N')


cha_tilt_angel_tra = []

for ts in u.trajectory:
    center_ag_cha_K = ag_cha_K.center_of_mass()
    center_ag_cha_N = ag_cha_N.center_of_mass()

    cha_vect = center_ag_cha_K - center_ag_cha_N

    cha_tilt_angel = tilt_angel(cha_vect)

    cha_tilt_angel_tra.append(cha_tilt_angel)


# plot cha_tilt_angel_tra
x1 = np.linspace(0, 10000, num=len(cha_tilt_angel_tra))
y1 = np.array(cha_tilt_angel_tra)

plt.figure(num=1)
plt.plot(x1, y1)

plt.xlabel('time')
plt.ylabel('cha_tilt_angel')
plt.title('cha_tilt_angel_tra')
plt.savefig('cha_tilt_angel_tra.png')
