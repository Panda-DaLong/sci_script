import sys

in_file = sys.argv[1]
residue_name = sys.argv[2]
#in_file is xyz_file(tinker_format)

# <Atom/>
def convert_atom(line_str):
    s = line_str.split()
    print('   <Atom name=\"' + s[1] + '\" type=\"' + s[5] + '\" />')

print(' </Residue>')
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
        print('   <Bond from="' + s[0] + '" to="' + i + '" />')

with open(in_file) as f:
    f.readline()
    for line in f:
        convert_bond(line)

print(' </Residue>')



          
