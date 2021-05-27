import sys

in_file = sys.argv[1]

def convert_pitorsion(line_str):
    l = line_str.split()
    print('  <PiTorsion class1="' + l[1] + \
          '" class2="' + l[2] + \
          '" k="' + l[3] + '" />')

print(' <AmoebaPiTorsionForce piTorsionUnit="1.0">')

with open(in_file) as f:
    for line in f:
        convert_pitorsion(line)

print(' </AmoebaPiTorsionForce>')


