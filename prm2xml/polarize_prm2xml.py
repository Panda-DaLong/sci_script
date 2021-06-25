import sys 

in_file = sys.argv[1]

def convert(line_str):
    l = line_str.split()
    middle = l[4:-1]
    tail = l[-1]

    #Unit Convert
    openmm_pol_fac = 0.001          # Angstrom^3 to nm^3
    l_2 = float(l[2]) * openmm_pol_fac
    l[2] = str(round(l_2, 4))
  
    print('  <Polarize type="' + l[1] + '" polarizability="' + l[2] + '" thole="' + l[3] + '\"', end=' ')
    num = 0
    for i in middle:
        num = num + 1
        print('pgrp' + str(num) + '="' + i + '"', end=' ')
    num = num + 1
    print('pgrp' + str(num) + '="' + tail + '"' + '/>')    

with open(in_file) as f:
    for line in f:
        convert(line)

print(' </AmoebaMultipoleForce>')
print('</ForceField>')
