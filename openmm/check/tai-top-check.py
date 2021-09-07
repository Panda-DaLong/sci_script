import sys
from xml.etree.ElementTree import parse, Element

xml_file = sys.argv[1]
bond_file = sys.argv[2]

#parse xml_file 
atoms = []
bonds_xml = []

xml = parse(xml_file)

root = xml.getroot()

for atom in root.findall('Atom'):
    atoms.append(atom.attrib['name'])

for bond in root.findall('Bond'):
    atom1 = bond.attrib['from']
    atom2 = bond.attrib['to']
    atom1_index = int(atom1)
    atom2_index = int(atom2)
    atom1_name = atoms[atom1_index]
    atom2_name = atoms[atom2_index]
    bonds_xml.append(set([atom1_name, atom2_name]))

print('******')
print('bonds in bonds_xml:')
print(bonds_xml)
print(len(bonds_xml))

#parse bond_file
bonds_bond = []

with open(bond_file) as file_2:
#the first line in file_2 is external_bond
    file_2.readline()
    for line in file_2:
        l_s = line.split()
        atom1_name = l_s[2][1:-1]
        atom2_name = l_s[11][1:-1]
        bonds_bond.append(set([atom1_name, atom2_name]))

print('******')
print('bonds in bonds_bond:')
print(bonds_bond)
print(len(bonds_bond))

#compare bonds_xml with bonds_bond
print('******')
print('compare bonds_xml with bonds_bond:')
print('compare_1:')

for bond in bonds_xml:
    if bond not in bonds_bond:
        print(bond, end='')
        print(' is in bonds_xml,', end='')
        print(' but not in bonds_bond')

print('compare_2:')
   
for bond in bonds_bond:
    if bond not in bonds_xml:
        print(bond, end='')
        print(' is in bonds_bond,', end='')
        print(' but not in bonds_xml')

