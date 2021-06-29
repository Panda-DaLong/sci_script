import sys

in_file = sys.argv[1]

def convert(line_str):
    l = line_str.split()
    
    #Unit Convert
    openmm_k_fac = 0.7302458    # kcal/radian^2 to kJ/degree^2
    l_4 = float(l[4]) * openmm_k_fac
    l[4] = str(round(l_4, 4))
    l_5 = float(l[5]) * openmm_k_fac
    l[5] = str(round(l_5, 5))

    print('  <StretchBend class1="' + l[1] + '" class2="' + l[2] + \
          '" class3="' + l[3] + '" k1="' + l[4] + '" k2="' + l[5] + '" />')

print(' <AmoebaStretchBendForce stretchBendUnit="1.0">')

with open(in_file) as f:
    for line in f:
        convert(line)

print(' </AmoebaStretchBendForce>')


