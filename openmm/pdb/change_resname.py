import sys
import re


#in_file and out_file are both pdb files
in_file = sys.argv[1]
out_file = sys.argv[2]


#old_res_name
cha_atoms = [ str(i) for i in range(28980, 29118) ]

#new_res_name
hea_atoms = [ str(i) for i in range(28980, 29011) ]

mia_atoms = [ str(i) for i in range(29011, 29038) ]

mib_atoms = [ str(i) for i in range(29038, 29065) ]

mic_atoms = [ str(i) for i in range(29065, 29092) ]

tai_atoms = [ str(i) for i in range(29092, 29118) ]


def new_resname(atom):
    if atom in hea_atoms:
        return 'hea'
    elif atom in mia_atoms:
        return 'mia'
    elif atom in mib_atoms:
        return 'mib'
    elif atom in mic_atoms:
        return 'mic'
    elif atom in tai_atoms:
        return 'tai'
    else:
        print('Error!!!')


with open(in_file) as f_in:
    with open(out_file, 'w') as f_out:

        for line in f_in:

            atom = line[6:11]
        
            for atom in cha_atoms:
                match = re.match(f'HETATM{atom}', line)
            
                if match:
                    new_line = line[0:17] + new_resname(atom) + line[20:]
                    break
       
            if match:
                print(new_line, end='', file=f_out)
       
            elif not match: 
                print(line, end='', file=f_out)
                
            else:
                print('Error!!!')

