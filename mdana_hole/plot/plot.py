import sys
import numpy as np
import matplotlib.pyplot as plt


in_file = sys.argv[1]

data = np.loadtxt(in_file)


nums,bins,patches = plt.hist(data, bins=30, range=(0, 3), edgecolor='k', density=False)

plt.show()