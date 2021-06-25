import sys

in_file = sys.argv[1]
residue_name = sys.argv[2]
#in_file is xyz_file(tinker_format)

# <Atom/>
def convert_atom(line_str):
    s = line_str.split()
    s[1] = s[1] + s[0]
    print('   <Atom name=\"' + s[1] + '\" type=\"' + s[5] + '\" />')

print(' <Residues>')
print('  <Residue name=\"' + residue_name + '\">')

with open(in_file) as f:
    f.readline()    
    for line in f:
        convert_atom(line)

# <Bond/>
def convert_bond(line_str):
    s = line_str.split()
    tail = s[6:]
    for atom2 in tail:
        atom1 = int(s[0])-1
        atom2 = int(atom2)-1
        if atom1 < atom2:
            print('   <Bond from="' + str(atom1) + '" to="' + str(atom2) + '" />')

with open(in_file) as f:
    f.readline()
    for line in f:
        convert_bond(line)

print('  </Residue>')
print(' </Residues>')          
