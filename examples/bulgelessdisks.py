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
massstellar = bulgelessdisks_array[:,20]
magu = bulgelessdisks_array[:,5]
magr = bulgelessdisks_array[:,7]
redshift = bulgelessdisks_array[:,1]
agntohostluminosity = bulgelessdisks_array[:,2]
bulgetototal = bulgelessdisks_array[:,3]
agnbolometricluminosity = bulgelessdisks_array[:,4]

# ----------------------------------------------------------------------
# Prepare the data

# Instantiate a Galtoons object:
# PJM: how about something like the following initialisation instead?
# mycoords = {'x':x, 'y':y, 'ra':ra, 'dec':dec} etc
# mybulges = {'mass':bulgemass, 'colour':urcolour}
# mytoons = toons.Galtoons(bulges=mybulges,disks=None,halos=None)
# Dictionaries are nice because you can reference them by the name of a parameter.
# Its a choice whether you do all this parsing of the data outside the galtoons
# class or inside...

mytoons = toons.Galtoons()
print mytoons.hello
mytoons.pleasework()

# calculate u-r magnitude
urcolour = magu - magr

# Normalise the data
bulgemass = numpy.multiply(bulgetototal, massstellar)
areabulgemass = 100 * mytoons.normarea(bulgemass) # 'numpy.float64' object is not callable

# ----------------------------------------------------------------------
# Create the u-r vs stellar mass plot:
ax=plt.subplot(111)

# Realize the galtoons!
# PJM: perhaps aim for a command like the following?
#   mytoons.scatterplot(massstellar, urcolour)
# where the two arguments are the x,y positions of the galtoons?
# This is not ideal either, because the galtoons should know where they are 
# in parameter space! You could initialise the galtoons with bulge, disk and 
# halo properties, in dictionaries, but then internally make composite properties
# like stellarmass and colour, which you could then call as follows:
#   mytoons.scatterplot('stellarmass', 'colour')

ax.scatter(massstellar, urcolour, s=areabulgemass, c='g')

# Make the plot nice:
ax.set_xlim(9.0,12.3)
ax.set_ylim(0.8,3.3)
plt.xlabel(r'Stellar Mass (log M$_{\odot}$)')
plt.ylabel('u-r colour (mag)')
plt.title('Late-Type Galaxies')
plt.grid(True)

# Save the plot and tell user what it's called:
savedfile = "testbulgelessdisks.png"
plt.savefig(savedfile)
print "Plot saved as "+os.getcwd()+"/"+savedfile 
plt.show()

# ----------------------------------------------------------------------
