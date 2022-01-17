import sys


#In_File:
#box_file is pbc_box file which is an out_file of OpenMM
box_file = sys.argv[1]

#Out_File:
vmd_box_file = sys.argv[2]


def grep_box_dim(str1):

    lst1 = str1.split()

    box_x_nm = lst1[2][8:-1]
    box_y_nm = lst1[6][2:-1]
    box_z_nm = lst1[10][2:-2]

    box_nm = '{},{},{}'.format(box_x_nm, box_y_nm, box_z_nm)

    return box_nm


all_box_dim = []

with open(box_file) as f_in:
    with open(vmd_box_file, 'w') as f_out:
    
        #skip box_dim of step 0
        line = f_in.readline()

        for line in f_in:
            box_nm = grep_box_dim(line)
            print(box_nm, file=f_out)
