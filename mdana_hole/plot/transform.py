import sys
import numpy as np

in_file = sys.argv[1]

data = np.loadtxt(in_file)

min_r = data[:, 1]

min_r_new = []

for i in min_r:
    if i < 0:
        r = 0
    elif i >= 0:
        r = i
    min_r_new.append(r)

data_new = np.array(min_r_new)

np.savetxt('min_r_new.txt', data_new)