import sys
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

scan_opbend = sys.argv[1]
scan_qm_energy = sys.argv[2]
scan_mm_energy = sys.argv[3]

def function(x, k):
    result = 0.02191418 * k * np.square(x)
    return result

x = np.loadtxt(scan_opbend)
y_qm = np.loadtxt(scan_qm_energy)
y_mm = np.loadtxt(scan_mm_energy)

y_qm = y_qm * 627.51
y_qm = np.around(y_qm, 4)

y_diff = y_qm - y_mm
y = y_diff - y_diff[0] 

param_est, err_est = curve_fit(function, x, y)
k_est = param_est[0]

k_est = np.around(k_est, 4)
print(k_est)

#p1 = plt.plot(x, y, "rx")
#p2 = plt.plot(x, function(x, k_est), "k--")
#plt.show()
