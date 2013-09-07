# -*- coding: utf-8 -*-
# Example plots using galtoons

# Galtoons example - Bulgeless Disk data

# ======================================================================

# Import useful packages
import pylab as plt
import numpy
import os
import math
import toons
 
# ======================================================================
# Read in the data

# Read data from bulgeless_agn_properties_testtable.cat, skip the header row
bulgelessdisks_array = numpy.loadtxt('bulgeless_agn_properties_testtable.cat',
                                      skiprows=1)

# Extract useful data from table

# Total mass in stellar units
totalmass = bulgelessdisks_array[:,20]
# Magnitudes
magu = bulgelessdisks_array[:,5]
magr = bulgelessdisks_array[:,7]
# Redshift
redshift = bulgelessdisks_array[:,1]
# AGN to host luminosity
agntohostlum = bulgelessdisks_array[:,2]
# Bulge to total mass ratio
bulgetototal = bulgelessdisks_array[:,3]
# AGN bolometric luminosity
agnbollum = bulgelessdisks_array[:,4]

# ----------------------------------------------------------------------
# Prepare the data

# Calculate u-r magnitude
urcolour = magu - magr

# Luminosity in AB maggies
luminosity = pow(10.0, -2.5 * urcolour)

# Bulge mass
bulgemass = bulgetototal * totalmass

# Disk mass
diskmass = totalmass - bulgemass

# ----------------------------------------------------------------------
# Create bulges, disks and halo dictionaries. Initialise them in Galtoons

mybulges = {'name':'bulge', 'x':totalmass, 'y':urcolour, 'size':bulgemass, 
            'brightness':luminosity, 'colour':urcolour, 
            'colourname':'u-r magnitude'}

mydisks = {'name':'disk', 'x':totalmass, 'y':urcolour, 'size':diskmass, 
           'colour':urcolour, 'colourname':'u-r magnitude', 
           'brightness':luminosity}

# Instantiate the Galtoons object, mytoons
mytoons = toons.Galtoons(bulges=mybulges,disks=mydisks,halos=None)


# ----------------------------------------------------------------------
# Realize the galtoons!

# Create the plot
ax = plt.subplot(111, aspect='equal', axisbg='black')

# Plot the galtoons
mytoons.plot_toons()

# Make the plot nice:
ax.set_xlim(9.4,11.0)
ax.set_ylim(1.0,3.0)
plt.xlabel(r'Stellar Mass (log M$_{\odot}$)')
plt.ylabel('u-r colour (mag)')
plt.title('Late-Type Galaxies')
plt.grid(True, color='0.75')

# Save the plot and tell user what it's called
savedfile = "testbulgelessdisks-mycolours.png"
plt.savefig(savedfile)
print "Plot saved as "+os.getcwd()+"/"+savedfile 
plt.show()

# ----------------------------------------------------------------------
