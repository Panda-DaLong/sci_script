import sys
from xml.etree.ElementTree import parse
import numpy as np


#xml_file is a forcefield file
#residue_name is the name of the residue of which the total charge to check
xml_file = sys.argv[1]

residue_name = sys.argv[2]


#parse xml_file 
xml = parse(xml_file)

root = xml.getroot()


#construct the list of atom in residue
atom_lst = []

def add_atom(residue):
    for atom in residue.iterfind('Atom'):
        atom_type = atom.get('type')
        atom_lst.append(atom_type)

for residue in root.iterfind('Residues/Residue'):
    if residue.get('name') == residue_name:
        add_atom(residue)
        break 
    

#construct the key of atom's charge
charge_key = {}

for multipole in root.iterfind('AmoebaMultipoleForce/Multipole'):
    atom_type = multipole.get('type')
    atom_charge = float(multipole.get('c0'))
    charge_key[atom_type] = atom_charge   


#construct the list of charge in residue
charge_lst = []

for atom in atom_lst:
    charge = charge_key[atom]
    charge_lst.append(charge)


#compute the total charge
charge_np = np.array(charge_lst)

total_charge = charge_np.sum()

print(f'total charge of {residue_name} is {total_charge}')

