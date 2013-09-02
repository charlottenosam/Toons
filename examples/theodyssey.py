# -*- coding: utf-8 -*-
# Example plots using galtoons

# ======================================================================

# Import useful packages
import pylab as plt
import numpy
import os
import toons
 
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

# calculate u-r magnitude
urcolour = magu - magr
# bulge mass
bulgemass = bulgetototal * totalmass
# disk mass
diskmass = totalmass - bulgemass

# ----------------------------------------------------------------------

# Create bulges, disks and halo dictionaries. Initialise them in Galtoons

mybulges = {'name':'bulge', 'x':totalmass, 'y':urcolour, 'size':bulgemass, 'brightness':agnbolometricluminosity}
mydisks = {'name':'disk', 'x':totalmass, 'y':urcolour, 'size':diskmass, 'brightness':agnbolometricluminosity}

# Instantiate the Galtoons object, mytoons
mytoons = toons.Galtoons(bulges=mybulges,disks=mydisks,halos=None)


# ----------------------------------------------------------------------

# Realize the galtoons!

# Create the plot

# Plot u-r vs stellar mass
ax = plt.subplot(111)

# Plot toons
mytoons.plot_toons()

# ----------------------------------------------------------------------
# Make the plot nice:
ax.set_xlim(9.4,11.0)
ax.set_ylim(1.0,3.0)
plt.xlabel(r'Stellar Mass (log M$_{\odot}$)')
plt.ylabel('u-r colour (mag)')
plt.title('Late-Type Galaxies')
plt.grid(True)

# Save the plot and tell user what it's called:
savedfile = "testbulgelessdisks-disks+bulge-blobs.png"
plt.savefig(savedfile)
print "Plot saved as "+os.getcwd()+"/"+savedfile 
plt.show()

# ----------------------------------------------------------------------
