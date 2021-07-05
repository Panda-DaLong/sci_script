import sys

in_file = sys.argv[1]
#in_file is good format pdb file by remove_mid_ch3_pdb.py 
#this python script aims for removing cap group -CH3 in CONECT
#And output <Bond from=atom1 to=atom2 /> in xxx.xml(OpenMM forcefield file in xml format)  

def conect_to_bond(line):
    l_s = line.split()
    if l_s[0] == 'CONECT':
        atom1 = str(int(l_s[1]) - 1)
        atom2 = str(int(l_s[2]) - 1)
        print('   <Bond from="' + atom1 + '" to="' + atom2 +'"/>')
    else:
        print('', end='')  

with open(in_file) as f:
    for line in f:
        conect_to_bond(line)

