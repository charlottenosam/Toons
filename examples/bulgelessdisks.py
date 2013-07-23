# -*- coding: utf-8 -*-
# Example plots using galtoons

# ======================================================================

import pylab as plt
import numpy
#import toons
import os, sys
 
# ======================================================================


os.chdir(os.path.dirname(os.path.abspath(sys.argv[0])))

# read in data from bulgeless_agn_properties_testtable.cat
bulgelessdisks_array = numpy.loadtxt('bulgeless_agn_properties_testtable.cat', skiprows=1)

# Extract the stellar mass and u-r columns
mass_stellar = bulgelessdisks_array[:,20]
mag_u = bulgelessdisks_array[:,5]
mag_r = bulgelessdisks_array[:,7]
u_r = mag_u - mag_r

# Plot u-r vs stellar mass
ax=plt.subplot(111)
ax.scatter(mass_stellar, u_r, c='b')
ax.set_xlim(9.0,12.3)
ax.set_ylim(0.8,3.3)
plt.xlabel(u'Stellar Mass log M\u2609')
plt.ylabel('u-r colour')
plt.title('Late-Type Galaxies')
plt.grid(True)
plt.savefig("testbulgelessdisks.png")
plt.show()
#plt.scatter(x, y, s=bmass, c='b', marker=bulge)
