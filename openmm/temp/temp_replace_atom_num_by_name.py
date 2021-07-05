import sys

atom_num_name_file = sys.argv[1]
#grep HETATM pdb_file
conect_file = sys.argv[2]
#grep CONECT pdb_file

d_num_name = dict()

def add_item(line_str):
    l_s = line_str.split()
    k = l_s[1]
    v = l_s[2]
    d_num_name[k] = v

def num_to_name(line_str):
    l_s = line_str.split()
    long = len(l_s)
    for d_key, d_value in d_num_name.items():
        for i in range(long):
            if l_s[i] == d_key : 
                l_s[i] = d_value
    print('  '.join(l_s)) 

with open(atom_num_name_file) as f1:
    for line in f1:
        add_item(line)

with open(conect_file) as f2:
    for line in f2:
        num_to_name(line) 
