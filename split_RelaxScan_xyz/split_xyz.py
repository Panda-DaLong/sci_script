# split total_scan_xyz to divided_xyz

filepath = input('filepath=: ')

s_n = int(input('scan_number=: '))

a_n = int(input('atom_number=: '))
line_n = a_n + 2

for i in range(s_n):

    a = i * line_n 
    b = a + line_n

    with open(filepath) as f:
         lines = f.readlines()
         split = lines[a:b]
    
    c = i + 1
 
    with open('{}'.format(c)+'.xyz', 'w') as g:
         g.writelines(split)
