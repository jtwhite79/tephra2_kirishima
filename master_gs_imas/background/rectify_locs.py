import numpy as np

n2 = 3534024.
e2 = 676858.

n1 = 3538377.
e1 = 110616.

ndelt_1_to_2 = n2 - n1
edelt_1_to_2 = e2 - e1

org_locs = np.loadtxt("kirishima_samples.xyz2.utm")
org_locs[:,0] += edelt_1_to_2
org_locs[:,1] += ndelt_1_to_2

np.savetxt("kirishima_samples.xyz2.utm.shift",org_locs, fmt="%10.3f")
new_locs = np.loadtxt("points.dat")
new_locs[:,2] = 1000.0
np.savetxt("points.dat.elev",new_locs, fmt="%10.3f")

