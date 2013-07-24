# -*- coding: utf-8 -*-
# Example plots using galtoons

# ======================================================================

# Import useful packages
import pylab as plt
import numpy
import os
import toons
import galtoon
 
# ======================================================================
# Read in the data

# Read in data from bulgeless_agn_properties_testtable.cat, skip the header row
bulgelessdisks_array = numpy.loadtxt('bulgeless_agn_properties_testtable.cat', skiprows=1)

# Extract useful data from table
massstellar = bulgelessdisks_array[:,20]
magu = bulgelessdisks_array[:,5]
magr = bulgelessdisks_array[:,7]
redshift = bulgelessdisks_array[:,1]
agntohostluminosity = bulgelessdisks_array[:,2]
bulgetototal = bulgelessdisks_array[:,3]
agnbolometricluminosity = bulgelessdisks_array[:,4]

# ----------------------------------------------------------------------
# Prepare the data

# calculate u-r magnitude
urcolour = magu - magr

# Normalise the data
bulgemass = bulgetototal * massstellar
areabulgemass = toons.normarea(bulgemass) # AttributeError: 'module' object has no attribute 'normarea'

# ----------------------------------------------------------------------
# Create the plot

# Plot u-r vs stellar mass
ax=plt.subplot(111)
ax.scatter(massstellar, urcolour, c='b')

# Make the plot nice
ax.set_xlim(9.0,12.3)
ax.set_ylim(0.8,3.3)
plt.xlabel(r'Stellar Mass (log M$_{\odot}$)')
plt.ylabel('u-r colour (mag)')
plt.title('Late-Type Galaxies')
plt.grid(True)

# Save the plot and tell user what it's called
savedfile = "testbulgelessdisks.png"
plt.savefig(savedfile)
print "Plot saved as "+os.getcwd()+"/"+savedfile 
plt.show()

# ----------------------------------------------------------------------