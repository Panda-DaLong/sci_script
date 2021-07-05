import sys

in_file = sys.argv[1]
#in_file is good format pdb file
#this python script aims for removing cap group -CH3 in tail

add_num_atom = -4 

ch3_atoms = []
ch3_min_atom = 9
ch3_max_atom = 12
for i in range(ch3_min_atom, ch3_max_atom + 1):
    ch3_atoms.append(str(i))

def remove_ch3(line):
    l_s = line.split()
    for i in l_s:
        if i in ch3_atoms:
            return i
            break

def hetatm_change_atom_num(line_str, add_num):
    atom = str(int(line_str[9:11]) + add_num)

    if len(atom) == 1:
        atom = ' ' + atom

    new_line = line_str[:9] + atom + line_str[11:] 
    return new_line

def conect_change_atom_num(line_str, add_num):
    atom1_index = int(line_str[9:11])
    atom2_index = int(line_str[14:16])

    if atom1_index > ch3_max_atom:
        atom1_index = atom1_index + add_num
    if atom2_index > ch3_max_atom: 
        atom2_index = atom2_index + add_num 
      
    atom1 = str(atom1_index)
    atom2 = str(atom2_index)
    
    if len(atom1) == 1:
        atom1 = ' ' + atom1 
    if len(atom2) == 1:
        atom2 = ' ' + atom2
    
    new_line = line_str[:9] + atom1 + line_str[11:14] + atom2 + line_str[16:]
    return new_line

with open(in_file) as f:
#Part_1
#keep the lines before -ch3    
    for i in range(9):
        line = f.readline()
        print(line, end='')

#remove the -ch3 hetatm lines
    for i in range(4):
        next(f)

#change the hetatm lines after -ch3
    for i in range(18):
        line = f.readline()
        line = hetatm_change_atom_num(line, add_num_atom) 
        print(line, end='') 

#Part_2
#remove -ch3 conect
#keep the others and change the indexs 
    for line in f:
        if remove_ch3(line):
            print('', end='')
        else:
            line = conect_change_atom_num(line, add_num_atom)
            print(line, end='')

