import sys 

in_file = sys.argv[1]

def convert(line_str):
    l = line_str.split()
    l_2 = float(l[2]) / 10
    l[2] = str(round(l_2, 4))
    while True:
        if len(l) == 5: break
        l.append('1.0')
    print('  <Vdw class="' + l[1] + '" sigma="' + l[2] + '" epsilon="' \
          + l[3] + '" reduction="' + l[4] + '" />')

print(''' <AmoebaVdwForce type="BUFFERED-14-7" radiusrule="CUBIC-MEAN" radiustype="R-MIN" radiussize="DIAMETER" epsilonrule="HHG" vdw-13-scale="0.0" vdw-14-scale="1.0" vdw-15-scale="1.0" >''')

with open(in_file) as f:
    for line in f:
        convert(line)

print(' </AmoebaVdwForce>')

 
