import sys
import re
import itertools

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
        match_para = re.match(i, line_str, flags=0)
        if match_para:
            return i
            break

with open(in_file) as f_in:
    lst = itertools.islice(f_in.readlines(), 40, None)
    for line in lst:
        line = line.lstrip()
        param = match_param(line)
        write_to_file(param, line)
        
