import sys
import pandas as pd

add_num = 500

in_file = sys.argv[1]
#in_file is a tinker_format_xyz file from poledit(choose 1)

out_file = './' + str(in_file) + '_2'

with open(in_file) as f_in:
    with open(out_file, 'w') as f_out:
        line = f_in.readline()
        print(line, end='', file = f_out)

df = pd.read_csv(in_file, dtype=str, sep='\s+', header=None, skiprows=[0], names=list(range(10)))

df[5] = df[5].astype(int) + add_num

with open(out_file, 'a') as f_out:
    df.to_string(f_out, header=False, index=False, na_rep='')

