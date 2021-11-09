import sys
import os
import itertools
import numpy as np
import MDAnalysis as mda


channel_pdb = sys.argv[1]


if not os.path.exists('temp'):
    os.mkdir('temp')


rotat_angel = np.linspace(0, 360, num=36, endpoint=False) * np.pi / 180
#rotat_angel = np.linspace(0, 360, num=18, endpoint=False) * np.pi / 180

x_y_z_rotat_angel = [(x, y, z) for x in rotat_angel for y in rotat_angel for z in rotat_angel]


all_total_pair_z = []

for i, x_y_z in enumerate(x_y_z_rotat_angel):
    
    packmol_input = './temp/rotation_' + str(i) + '.inp'
    packmol_output = './temp/rotation_' + str(i) + '.pdb'
    packmol_log = './temp/rotation_' + str(i) + '.log'

    x, y, z = x_y_z

    with open(packmol_input, 'w') as f:
        print('nloop 200', file=f)
        print('tolerance 2.0', file=f)
        print('', file=f)
        print('output ' + packmol_output, file=f)
        print('filetype pdb', file=f)
        print('add_box_sides', file=f)
        print('', file=f)
        print('structure ' + channel_pdb, file=f)
        print('  number 1', file=f)
        print('  center', file=f)
        print('  fixed 0. 0. 0. ' + str(x) + ' ' + str(y) + ' ' +  str(z), file=f)
        print('end structure', file=f)

    os.system('packmol < ' + packmol_input + ' > ' + packmol_log)
    
    #compute the total_pair_z  
    u = mda.Universe(packmol_output)

    atoms_z = []

    for atom in u.atoms:
        atoms_z.append(atom.position[2])


    total_pair_z = 0
    
    for c in itertools.combinations(atoms_z, 2):
        a1, b2 = c
        total_pair_z += abs(a1 - b2)
    
    #append the total_pair_z
    all_total_pair_z.append(total_pair_z)


print('***** len *****')
print(len(all_total_pair_z))

#if channel is short
print('***** min *****')
print(min(all_total_pair_z))
print(all_total_pair_z.index(min(all_total_pair_z)))

#if channel is long
print('***** max *****')
print(max(all_total_pair_z))
print(all_total_pair_z.index(max(all_total_pair_z)))


