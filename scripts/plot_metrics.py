from sympy import *
import numpy as np
import argparse
from scipy import stats


import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as axes3d
import matplotlib.font_manager as font_manager

# It's also possible to use the reduced notation by directly setting font.family:
plt.rcParams.update({
  "text.usetex": True,
  "font.family": "Helvetica",
  'font.size': 12,

})





data_dir = fig_dir  = "/home/hjardali/Repos/NAV_ws/src/reactive_assistance/data/"
trial = data_dir + "adm_gap_1/"

odom  = np.loadtxt( trial + "odom.txt" ).T
t_odom = odom[0]
lin_vel = odom[1]
ang_vel = odom[2]

scan  = np.loadtxt( trial + "scan.txt" ).T
t_scan = scan[0]
rmin = scan[1]

dt_odom=t_odom[1]-t_odom[0]
dt_scan= t_scan[1]-t_scan[0]

def check_total_time(t_odom, lin_vel):
    

print("odom shape: ", np.shape(odom))



#################### training VS Removal of PCL ####################  
fig, ax0 = plt.subplots(nrows=1, sharex=True, figsize=(8,3))

ax0.plot( odom[0], odom[1], label='Odom linear vel')
ax0.plot( odom[0], odom[2], label='Odom angular vel')


ax0.set_xlabel('Time [s]')
ax0.set_ylabel('Velocity')
ax0.legend()

plt.savefig(fig_dir + '/velocities.png', bbox_inches = 'tight', pad_inches = 0)
plt.show()