import sys 

in_file = sys.argv[1]

def convert(line_str):
    l = line_str.split()
    middle = l[4:-1]
    tail = l[-1]
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
