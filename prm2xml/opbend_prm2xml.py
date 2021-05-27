import sys

in_file = sys.argv[1]

def convert_opbend(line_str):
    l = line_str.split()
    print('  <Angle class1="' + l[1] + '" class2="' + l[2] + \
          '" class3="' + l[3] + '" class4="' + l[4] + \
          '" k="' + l[5] + '"/>')

print(' <AmoebaOutOfPlaneBendForce type="ALLINGER" opbend-cubic="-0.014" opbend-quartic="5.6e-05" opbend-pentic="-7e-07" opbend-sextic="2.2e-08">')

with open(in_file) as f:
    for line in f:
        convert_opbend(line)

print(' </AmoebaOutOfPlaneBendForce>')


