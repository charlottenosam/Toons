# -*- coding: utf-8 -*-
# Example plots using galtoons

# ======================================================================

# Import useful packages
import pylab as plt
import numpy
import os
import toons
import math
from matplotlib.patches import Ellipse
 
# ======================================================================
# Read in the data

# Read in data from bulgeless_agn_properties_testtable.cat, skip the header row
bulgelessdisks_array = numpy.loadtxt('bulgeless_agn_properties_testtable.cat', skiprows=1)

# Extract useful data from table
totalmass = bulgelessdisks_array[:,20]
magu = bulgelessdisks_array[:,5]
magr = bulgelessdisks_array[:,7]
redshift = bulgelessdisks_array[:,1]
agntohostluminosity = bulgelessdisks_array[:,2]
bulgetototal = bulgelessdisks_array[:,3]
agnbolometricluminosity = bulgelessdisks_array[:,4]

# ----------------------------------------------------------------------
# Prepare the data

# Instantiate the Galtoons class
mytoons = toons.Galtoon()
print mytoons.hello
mytoons.pleasework()

# calculate u-r magnitude
urcolour = magu - magr

# Normalise the data
bulgemass = bulgetototal * totalmass
areabulgemass = 400 * mytoons.normarea(bulgemass)

# ----------------------------------------------------------------------
# Create the plot

# Plot u-r vs stellar mass
ax = plt.subplot(111)

# Disk Mass
diskmass = totalmass - bulgemass

mytoons.plot_toons(totalmass, urcolour, diskmass, "orange")

#PI = 3.14162
#for i in range(len(bulgemass)):
 #   a = 0.8 * 0.5 * math.sqrt(bulgemass[i] / PI)
  #  b = 0.8 * 4 * a
   # ax.add_patch(Ellipse((totalmass[i], urcolour[i]), a, b, facecolor="orange", edgecolor="black", alpha=0.5, angle=-45.0))

# Bulge Mass
ax.scatter(totalmass, urcolour, s=areabulgemass, c='r', alpha=1)

# Make the plot nice
ax.set_xlim(9.0,12.3)
ax.set_ylim(0.8,3.3)
plt.xlabel(r'Stellar Mass (log M$_{\odot}$)')
plt.ylabel('u-r colour (mag)')
plt.title('Late-Type Galaxies')
plt.grid(True)

# Save the plot and tell user what it's called
savedfile = "testbulgelessdisks.png"
#plt.savefig(savedfile)
#print "Plot saved as "+os.getcwd()+"/"+savedfile 
plt.show()

# ----------------------------------------------------------------------