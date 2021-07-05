import sys
import re

in_file = sys.argv[1]
residue_name = sys.argv[2]

if len(residue_name) != 3:
    print('residue_name should be 3 characters long')

info_lst = ['HETATM', 'CONECT']

def match_info(line):
    for info in info_lst:
        mat = re.match(info, line, flags=0)
        if mat:
            return info
            break

def modi_hetatm(line):
    atom_num = line[9:11].lstrip()
    atom_name_old = line[13]
    
    atom_name_new = atom_name_old + atom_num
    if len(atom_name_new) < 3:
        atom_name_new = ' ' + atom_name_new 

    line_new = line[:12] + atom_name_new + line[15:17] + residue_name + line[20:54]
    print(line_new) 

def modi_conect(line):
    s = line.split()
    atom1 = int(s[1])

    for atom2 in s[2:]:
        atom2 = int(atom2)

        if atom1 < atom2:
            atom1_str = str(atom1)
            atom2_str = str(atom2)

            if len(atom1_str) < 2:
                    atom1_str = ' ' + atom1_str
            if len(atom2_str) < 2:
                    atom2_str = ' ' + atom2_str

            line_new = 'CONECT' + '  ' + atom1_str + '  ' + atom2_str
            print(line_new)

with open(in_file) as f_in:
    for line in f_in:
        info = match_info(line)

        if info == 'HETATM':
            modi_hetatm(line)

        elif info == 'CONECT':
            modi_conect(line)
        
