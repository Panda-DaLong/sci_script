import sys
import os
import re
import itertools


out_file = 'head_2.key_2'

add_num = 500

in_file = sys.argv[1]
#in_file is a tinker_format key file from poledit(choose 1)


#split a tinker key file from poledit(choose 1)
#
path = './' + str(in_file) + '_split/'
os.mkdir(path)

params_lst = ['atom','multipole','polarize']

def write_to_file(param, line_str):
    if param == None:
        pass
    else:
        out_file = path + str(param) + '.prm'
        with open(out_file, 'a') as f_out:
            print(line_str, file = f_out, end='')

def match_param(line_str):
    for i in params_lst:
        mat = re.match(i, line_str, flags=0)
        if mat:
            return i
            break


with open(in_file) as f_in:

     for line in f_in:
        param = match_param(line)
        write_to_file(param, line)

        if param == 'multipole':
            for i in range(0, 4):
                line = next(f_in)
                write_to_file(param, line)
#
#split a tinker key file from poledit(choose 1)
#
#
#
#add atom_num of several splited tinker key files and write to one file             
#
def add(i):
    i = int(i)
    if i > 0:
        i = i + add_num
    elif i < 0:
        i = i - add_num
    i = str(i)
    return i

def join_write(file_to_write, list_to_join):
    with open(file_to_write, 'a') as f_out:
        print('    '.join(list_to_join), file = f_out)

def tidy_multipole(line_str):
    l_s = line_str.split()
    long = len(l_s)
    if long == 5 :
        for i in range(1, 4):
            l_s[i] = add(l_s[i])
    elif long == 6: 
        for i in range(1, 5):
            l_s[i] = add(l_s[i])
    join_write(out_file, l_s)

def tidy_atom(line_str):
    l_s = line_str.split()
    for i in range(1, 3):
        l_s[i] = add(l_s[i])
    join_write(out_file, l_s)

def tidy_polarize(line_str):
    l_s = line_str.split()
    long = len(l_s)
    l_s[1] = add(l_s[1])
    for i in range(4, long):
        l_s[i] = add(l_s[i])
    join_write(out_file, l_s)


for i in ['atom.prm', 'polarize.prm', 'multipole.prm']:

    with open(path + i) as f_in:
    
        if i == 'atom.prm':
            for line in f_in:
                tidy_atom(line)
    
        elif i == 'polarize.prm':
            for line in f_in:
                tidy_polarize(line)

        elif i == 'multipole.prm':
            for line in f_in:
                tidy_multipole(line)
                for i in range(4):
                    line = next(f_in)
                    with open(out_file, 'a') as f_out:
                        print(line, file = f_out, end = '')
#
#add atom_num of several splited tinker key files and write to one file
