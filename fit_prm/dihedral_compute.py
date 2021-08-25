import sys
import re
import numpy as np


in_file = sys.argv[1]
#in_file is a pdb file
dihedral_file = sys.argv[2]
#dihedral is a csv file


def read_file(filename):
    coordinates = []
    with open(filename, 'r') as f:
        for line in f:
            mat = re.match('HETATM', line, flags=0)
            if mat:
                lst_line = line.split()
                coordinate_x = lst_line[5]
                coordinate_y = lst_line[6]
                coordinate_z = lst_line[7]
                coordinates.append((coordinate_x, coordinate_y, coordinate_z)) 
    return np.array(coordinates, dtype=float)

def dihedral(coordinates, a, b, c, d):
    i = coordinates[a]
    j = coordinates[b]
    k = coordinates[c]
    l = coordinates[d]
    f, g, h = i-j, j-k, l-k
    a = np.cross(f, g)
    b = np.cross(h, g)
    axb = np.cross(a, b)
    cos = np.dot(a, b)
    sin = np.dot(axb, g) /  np.linalg.norm(g)
    r = -np.arctan2(sin, cos)
    return np.degrees(r)


arr_coor = read_file(in_file)

arr_dihe = np.loadtxt(dihedral_file, dtype=int, delimiter=',')

x = arr_dihe.shape[0]
y = arr_dihe.shape[1]

for i in range(x):
    atom_a = arr_dihe[i][0]
    atom_b = arr_dihe[i][1]
    atom_c = arr_dihe[i][2]
    atom_d = arr_dihe[i][3]
    print('dihedral {} {} {} {} : '.format(atom_a, atom_b, atom_c, atom_d), end='')
    print(dihedral(arr_coor, atom_a, atom_b, atom_c, atom_d))

