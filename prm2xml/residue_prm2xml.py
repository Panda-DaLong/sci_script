import sys

in_file = sys.argv[1]
residue_name = sys.argv[2]
#in_file is xyz_file(tinker_format)

# <Atom/>
def convert_atom(line_str):
    s = line_str.split()
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
    for i in tail:
        atom1 = str(int(s[0])-1)
        atom2 = str(int(i)-1)
        print('   <Bond from="' + atom1 + '" to="' + atom2 + '" />')

with open(in_file) as f:
    f.readline()
    for line in f:
        convert_bond(line)

print('  </Residue>')
print(' </Residues>')          
