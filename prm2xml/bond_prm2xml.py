import sys

in_file = sys.argv[1]

def convert(line_str):
    l = line_str.split()
    
    #Unit Convert
    l_3 = float(l[3]) * 418.4
    l[3] = str(round(l_3, 4))
    l_4 = float(l[4]) * 0.1
    l[4] = str(round(l_4, 4))
    
    print('  <Bond class1="' + l[1] + '" class2="' + l[2] + '" k="' + \
          l[3] + '" length="' + l[4] + '"/>')

print(' <AmoebaBondForce bond-cubic="-25.5" bond-quartic="379.3125">')

with open(in_file) as f:
    for line in f:
        convert(line)

print(' </AmoebaBondForce>')
