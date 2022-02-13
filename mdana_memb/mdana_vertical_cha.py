import sys
import math
import numpy as np
import numpy.linalg as la
import MDAnalysis as mda


center_file = sys.argv[1]

vertical_file = sys.argv[2]


def vector_angle(vec1, vec2):

    cos_angel = np.dot(vec1, vec2)
    sin_angel = la.norm(np.cross(vec1, vec2))

    angel_in_radian = np.arctan2(sin_angel, cos_angel)
    angle_in_degree = math.degrees(angel_in_radian)

    return angle_in_degree

def rotate_to_vertical_cha(ts):

    ag_cha_K = u.select_atoms('resname cha and chainID K')
    ag_cha_L = u.select_atoms('resname cha and chainID L')

    center_ag_cha_K = ag_cha_K.center_of_mass()
    center_ag_cha_L = ag_cha_L.center_of_mass()

    center_point = (center_ag_cha_K + center_ag_cha_L) / 2

    channel_normal_vector = center_ag_cha_K - center_ag_cha_L
    z_axis = np.array([0, 0, 1])
    
    direction_vector = np.cross(channel_normal_vector, z_axis)
    rotation_angle = vector_angle(channel_normal_vector, z_axis)

    u.atoms.rotateby(angle=rotation_angle, axis=direction_vector, point=center_point)

    return ts


u = mda.Universe(center_file)

u.trajectory.add_transformations(rotate_to_vertical_cha)


with mda.Writer(vertical_file, u.atoms.n_atoms) as w:
    for ts in u.trajectory:
        w.write(u)