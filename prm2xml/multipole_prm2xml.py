import sys

in_file = sys.argv[1]

def z_then_x(line_str):
    a1,b2,c3,d4,e5 = line_str.split()
    print('  <Multipole '+'type=\"'+b2+'\" kz=\"'+c3+'\" kx=\"'+d4+'\" c0=\"'+e5+'\" ',end='')

def bisector(line_str):
    a1,b2,c3,d4,e5 = line_str.split()
    print('  <Multipole '+'type=\"'+b2+'\" kz=\"'+c3+'\" kx=\"'+d4+'\" c0=\"'+e5+'\" ',end='')

def z_then_bisector(line_str):
    a1,b2,c3,d4,e5,f6 = line_str.split()
    print('  <Multipole '+'type=\"'+b2+'\" kz=\"'+c3+'\" kx=\"'+d4+'\" ky=\"'+e5+'\" c0="'+f6+'\" ',end='')

def trisector(line_str):
    a1,b2,c3,d4,e5,f6 = line_str.split()
    print('  <Multipole '+'type=\"'+b2+'\" kz=\"'+c3+'\" kx=\"'+d4+'\" ky=\"'+e5+'\" c0="'+f6+'\" ',end='')

def convert_1(line_str):
    l_s = line_str.split()
    long = len(l_s)
    if long == 5 :
        if int(l_s[3]) > 0:
            z_then_x(line_str)
        else:
            bisector(line_str)
    else:
        if int(l_s[2]) > 0:
            z_then_bisector(line_str)
        else:
            trisector(line_str) 

def convert_2(line_str):
    a1,b2,c3 = line_str.split()
    print('d1=\"'+a1+'\" d2=\"'+b2+'\" d3=\"'+c3+'\" ',end='')

def convert_3(line_str):
    a1 = line_str.strip()
    print('q11=\"'+a1+'\" ',end='')    

def convert_4(line_str):
    a1,b2 = line_str.split()
    print('q21=\"'+a1+'\" '+'q22=\"'+b2+'\" ',end='')

def convert_5(line_str):
    a1,b2,c3 = line_str.split()
    print('q31=\"'+a1+'\" '+'q32=\"'+b2+'\" '+'q33=\"'+c3+'\"  />')

print(' <AmoebaMultipoleForce  direct11Scale="0.0"  direct12Scale="1.0"  direct13Scale="1.0"  direct14Scale="1.0"  mpole12Scale="0.0"  mpole13Scale="0.0"  mpole14Scale="0.4"  mpole15Scale="0.8"  mutual11Scale="1.0"  mutual12Scale="1.0"  mutual13Scale="1.0"  mutual14Scale="1.0"  polar12Scale="0.0"  polar13Scale="0.0"  polar14Intra="0.5"  polar14Scale="1.0"  polar15Scale="1.0"  > ')

with open(in_file) as f:
    while True:
        line = f.readline()
        if not line: break
        convert_1(line)

        line = f.readline()
        convert_2(line)
        
        line = f.readline()
        convert_3(line)
    
        line = f.readline()
        convert_4(line)
     
        line = f.readline()
        convert_5(line)
            
