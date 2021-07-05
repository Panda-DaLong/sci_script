import sys

in_file = sys.argv[1]
#in_file is from replace_atom_num_by_name.py

residue_name = 'tai'

def conect_to_bond(line_str):
    l_s = line_str.split()
    atom1 = l_s[1]
    atom2 = l_s[2]
    print('         <Bond from="'+atom1+'" to="'+atom2+'"/>')

print('   <Residues>')
print('      <Residue name="{}">'.format(residue_name))

with open(in_file) as f:
    for line in f:
        conect_to_bond(line)

print('      </Residue>')
print('   </Residues>')
