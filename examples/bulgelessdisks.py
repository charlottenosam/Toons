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
# Instantiate the Galtoons class

mytoons = toons.Galtoons()

# Instantiate a Galtoons object:
# PJM: how about something like the following initialisation instead?

#mycoords = {'x':totalmass, 'y':urcolour}
#mybulges = {'size':bulgesize, 'mass':bulgemass, 'colour':urcolour}
#mydisks = {'size':disksize, 'mass':diskmass, 'colour':urcolour}

# mytoons = toons.Galtoons(bulges=mybulges,disks=None,halos=None)
# Dictionaries are nice because you can reference them by the name of a parameter.
# Its a choice whether you do all this parsing of the data outside the galtoons
# class or inside...


# ----------------------------------------------------------------------

# Realize the galtoons!
# PJM: perhaps aim for a command like the following?
#   mytoons.scatterplot(massstellar, urcolour)
# where the two arguments are the x,y positions of the galtoons?
# This is not ideal either, because the galtoons should know where they are 
# in parameter space! You could initialise the galtoons with bulge, disk and 
# halo properties, in dictionaries, but then internally make composite properties
# like stellarmass and colour, which you could then call as follows:
#   mytoons.scatterplot('stellarmass', 'colour')


# Create the plot

# Plot u-r vs stellar mass
ax = plt.subplot(111)

# Plot toons
mytoons.plot_toons(totalmass, urcolour, diskmass, bulgemass, "cyan")

# ----------------------------------------------------------------------
# Make the plot nice:
ax.set_xlim(9.4,11.0)
ax.set_ylim(1.0,3.0)
plt.xlabel(r'Stellar Mass (log M$_{\odot}$)')
plt.ylabel('u-r colour (mag)')
plt.title('Late-Type Galaxies')
plt.grid(True)

# Save the plot and tell user what it's called:
savedfile = "testbulgelessdisks-disks&bulge-realisticcolours.png"
plt.savefig(savedfile)
print "Plot saved as "+os.getcwd()+"/"+savedfile 
plt.show()

# ----------------------------------------------------------------------
