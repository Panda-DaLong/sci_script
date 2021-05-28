import sys

in_file = sys.argv[1]

def convert(line_str):
    a1,b2,c3,d4,e5,f6,g7,h8,j9 = line_str.split()
    print('  '+'<Type'+' '+'name=\"'+b2+'\" '+'class=\"'+c3+'\" '+'element=\"'+d4+'\" ' \
          +'mass=\"'+h8+'\"/>')

print('<ForceField>')
print(' <AtomTypes>')

for line in open(in_file):
    convert(line)

print(' </AtomTypes>')


