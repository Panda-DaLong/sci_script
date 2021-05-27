import sys

in_file = sys.argv[1]

def convert(line_str):
    l = line_str.split()
    print('  <Angle class1="' + l[1] + '" class2="' + l[2] + '" class3="' + \
          l[3] + '" k="' + l[4] + '" angle1="' + l[5] + '"  />')

print(' <AmoebaAngleForce angle-cubic="-0.014" angle-quartic="5.6e-05" angle-pentic="-7e-07" angle-sextic="2.2e-08">')

with open(in_file) as f:
    for line in f:
        convert(line)

print(' </AmoebaAngleForce>')

