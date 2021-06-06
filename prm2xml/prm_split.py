import sys
import re

in_file = sys.argv[1]

params_lst = ['atom', 'multipole', 'polarize', 'vdw', 'bond', 'angle', 'strbnd', 'opbend', 'torsion']

def write_to_file(param, line_str):
    if param == None:
        pass
    else:
        out_file = str(param) + '.prm'
        with open(out_file, 'a') as f_out:
            print(line_str, file = f_out, end='')

def match_param(line_str):
    for i in params_lst:
        match_1 = re.match(i, line_str, flags=0)
        match_2 = re.match(i, line_str, flags=1)
        if match_1 or match_2:
            return i
            break

with open(in_file) as f_in:
    for line in f_in.readlines():
        param = match_param(line)
        write_to_file(param, line)
        
