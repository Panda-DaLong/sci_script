import sys
import numpy as np
import matplotlib.pyplot as plt


#data_file is a txt file
data_file = sys.argv[1]


def get_file_name(file_str):
    point_index = file_str.index('.')
    file_name = file_str[0:point_index]
    return file_name


arr_distance_tra = np.loadtxt(data_file) 

tra_frames = len(arr_distance_tra)
# frame_step=2ns
tra_start_time = 2
tra_end_time = 2 * tra_frames 

# Waring: start point and end point !!!
x1 = np.linspace(tra_start_time, tra_end_time, num=tra_frames)  
y1 = np.array(arr_distance_tra)


plt.figure(num=1, figsize=(50, 20))
plt.plot(x1, y1)

plt.xlabel('time(ns)', fontsize=30)
plt.ylabel('distance(angstrom)', fontsize=30)

plt.xlim([0, tra_end_time])
plt.ylim([0, 15])

plt.xticks(fontsize=20)
plt.yticks(fontsize=20)

figure_name = get_file_name(data_file)
plt.title(figure_name, fontsize=50)
plt.savefig(fname='{}.png'.format(figure_name), dpi=500, bbox_inches='tight')

