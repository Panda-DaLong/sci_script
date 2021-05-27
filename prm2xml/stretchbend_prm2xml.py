import sys

in_file = sys.argv[1]

def convert(line_str):
    l = line_str.split()
    print('  <StretchBend class1="' + l[1] + '" class2="' + l[2] + \
          '" class3="' + l[3] + '" k1="' + l[4] + '" k2="' + l[5] + '" />')

print(' <AmoebaStretchBendForce stretchBendUnit="1.0">')

with open(in_file) as f:
    for line in f:
        convert(line)

print('</AmoebaStretchBendForce>')


