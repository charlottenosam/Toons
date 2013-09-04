# -*- coding: utf-8 -*-
# Example plots using galtoons

# Plotting the catalogue of galaxies around "The Odyssey"

# ======================================================================

# Import useful packages
import pylab as plt
import numpy
import os
import toons
 
# ======================================================================
# Read in the data

# Read in data from The_Odyssey_g-r_GIM2D.txt
odyssey_array = numpy.loadtxt('The_Odyssey_g-r_GIM2D.txt')

# Extract useful data from table
ra = odyssey_array[:,14]
dec = odyssey_array[:,15]
gmag = odyssey_array[:,5]
rmag = odyssey_array[:,6]
scale_kpc_arcsec = odyssey_array[:,4]
bulge_Re_kpc = odyssey_array[:,8]       # semi-major axis: a
bulge_e = odyssey_array[:,9]            # ellipticity: e = 1 - b/a = 1 - q
bulge_phi = odyssey_array[:,10]
disk_Rd_kpc = odyssey_array[:,11]
disk_inclination = odyssey_array[:,12]
disk_phi = odyssey_array[:,13]


# ----------------------------------------------------------------------
# Prepare the data

# define PI
PI = 3.14159265359

# magnitude
grmag = gmag - rmag

# axis ratio
bulge_q = 1.0 - bulge_e

# bulge area in arcsec
bulge_Re_arcsec = bulge_Re_kpc / scale_kpc_arcsec
bulge_size = PI * bulge_q * bulge_Re_arcsec * bulge_Re_arcsec

# disk area in arcsec
disk_Re_kpc = 1.678 * disk_Rd_kpc
disk_Re_arcsec = disk_Re_kpc / scale_kpc_arcsec
disk_size = PI * disk_Re_arcsec * disk_Re_arcsec
# ----------------------------------------------------------------------

# Create bulges, disks and halo dictionaries. Initialise them in Galtoons

mybulges = {'name':'bulge', 'x':-ra, 'y':dec, 'size':bulge_size, 'phi':bulge_phi, 'q':bulge_q, 'colour':grmag}  #["orange" for i in range(len(ra))]}
mydisks = {'name':'disk', 'x':-ra, 'y':dec, 'size':disk_size, 'phi':disk_phi, 'colour':grmag}

# Instantiate the Galtoons object, mytoons
mytoons = toons.Galtoons(halos=None, disks=mydisks, bulges=mybulges)


# ----------------------------------------------------------------------

# Realize the galtoons!

# Create the plot

# Plot u-r vs stellar mass
ax = plt.subplot(111, aspect='equal')

# Plot toons
mytoons.plot_toons()

# Plot The Odyssey
plt.plot(-248.08737, 19.82660, 'or')
plt.text(-248.08737, 19.82660, 'The Odyssey')
# ----------------------------------------------------------------------
# Make the plot nice:

ax.set_xlim(-247.5,-248.7)
ax.set_ylim(19.2,20.4)
#plt.colorbar()
plt.xlabel('RA (arcsec)')
plt.ylabel('DEC (arcsec)')
plt.title('The Odyssey')
plt.grid(True)

# Save the plot and tell user what it's called:
savedfile = "test-theodyssey.png"
plt.savefig(savedfile)
print "Plot saved as "+os.getcwd()+"/"+savedfile 
plt.show()

# ----------------------------------------------------------------------
