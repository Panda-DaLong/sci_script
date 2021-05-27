import sys

in_file = sys.argv[1]

def convert(line_str):
    l = line_str.split()
    print('  <Bond class1="' + l[1] + '" class2="' + l[2] + '" length="' + \
          l[3] + '" k="' + l[4] + '"/>')

print(' <AmoebaBondForce bond-cubic="-25.5" bond-quartic="379.3125">')

with open(in_file) as f:
    for line in f:
        convert(line)

print(' </AmoebaBondForce>')
