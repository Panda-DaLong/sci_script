import sys

in_file = sys.argv[1]

def convert(line_str):
    l = line_str.split()
    
    #Unit Convert
    openmm_amp_fac = 2.092          # kcal to kJ and a factor of 1/2
    openmm_angle_fac = 0.01745329   # degrees to radians
    for i in [5, 7, 9]:
        l_i = float(l[i]) * openmm_amp_fac
        l[i] = str(round(l_i, 4))
    for i in [6, 8, 10]:
        l_i = float(l[i]) * openmm_angle_fac
        l[i] = str(round(l_i, 4))
    
    print('  <Torsion class1="' + l[1] + '" class2="' + l[2] + \
          '" class3="' + l[3] + '" class4="' + l[4] + \
          '"   amp1="' + l[5] + '" angle1="' + l[6] + \
          '"   amp2="' + l[7] + '" angle2="' + l[8] + \
          '"   amp3="' + l[9] + '" angle3="' + l[10] + '" />')

print(' <AmoebaTorsionForce torsionUnit="0.5">')

with open(in_file) as f:
    for line in f:
        convert(line)

print(' </AmoebaTorsionForce>')
