import sys

in_file = sys.argv[1]
#in_file is good format pdb file
#this python script aims for removing cap group -CH3 in tail

ch3_atoms = []
for i in range(28, 36):
    ch3_atoms.append(str(i))

def remove_ch3(line):
    l_s = line.split()
    for i in l_s:
        if i in ch3_atoms:
            return i
            break 

with open(in_file) as f:
#Part_1
#keep the lines before -ch3    
    for i in range(27):
        line = f.readline()
        print(line, end='')

#remove the -ch3 hetatm lines
    for i in range(8):
        next(f)

#Part_2
#remove -ch3 conect and keep the others
    for line in f:
        if remove_ch3(line):
            print('', end='')
        else:
            print(line, end='')

