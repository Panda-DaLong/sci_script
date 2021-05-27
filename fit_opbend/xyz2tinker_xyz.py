import sys

xyz_file = sys.argv[1]

conect_file = sys.argv[2]
#conect_file is from a tinker_xyz_file by conect_from_TinkerXYZ.py

with open(conect_file) as cf:
    cf_lins = cf.readlines()
    cf_len = len(cf_lins)
          
with open(xyz_file) as xf:
    xf_lin1 = xf.readline()
    xf_lin2 = xf.readline()
    print(xf_lin1, end='')
    
    for i in range(cf_len):
        xf_lin = xf.readline()
        out_lin = xf_lin.rstrip() + '  ' + cf_lins[i]
        i = i + 1
        out_lin = str(i) + out_lin
        print(out_lin, end='')
