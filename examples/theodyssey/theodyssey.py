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
# RA and DEC co-ordinates in arcsec 
ra = odyssey_array[:,14]
dec = odyssey_array[:,15]
# Magnitudes
gmag = odyssey_array[:,5]
rmag = odyssey_array[:,6]
# Scales kpc/arcsec
scale_kpc_arcsec = odyssey_array[:,4]
# Bulge properties
bulge_Re_kpc = odyssey_array[:,8]       # semi-major axis: a
bulge_e = odyssey_array[:,9]            # ellipticity: e = 1 - b/a = 1 - q
bulge_phi = odyssey_array[:,10]
# Disk properties
disk_Rd_kpc = odyssey_array[:,11]       # scale ratio
disk_inclination = odyssey_array[:,12]
disk_phi = odyssey_array[:,13]


# ----------------------------------------------------------------------
# Prepare the data

# Define PI
PI = 3.14159265359

# Magnitude difference
grmag = gmag - rmag

# Axis ratio
bulge_q = 1.0 - bulge_e

# Bulge area in arcsec
bulge_Re_arcsec = bulge_Re_kpc / scale_kpc_arcsec
bulge_size = PI * bulge_q * bulge_Re_arcsec * bulge_Re_arcsec

# Disk area in arcsec
disk_Re_kpc = 1.678 * disk_Rd_kpc
disk_Re_arcsec = disk_Re_kpc / scale_kpc_arcsec
disk_size = PI * disk_Re_arcsec * disk_Re_arcsec

# Luminosity in AB maggies
flux = pow(10.0, -2.5 * grmag)

# Mean surface brightness with Re
meansb = flux / (2.0 * 3.14 * (bulge_Re_arcsec**2))  

# ----------------------------------------------------------------------
# Create bulges, disks and halo dictionaries. Initialise them in Galtoons

mybulges = {'name':'bulge', 'x':-ra, 'y':dec, 'size':bulge_size, 
            'phi':bulge_phi, 'q':bulge_q, 'colour':grmag, 
            'colourname':'g-r magnitude', 'brightness':flux}
            
mydisks = {'name':'disk', 'x':-ra, 'y':dec, 'size':disk_size, 'phi':bulge_phi, 
           'colour':grmag, 'colourname':'g-r magnitude'} 
           #'brightness':flux}

# Instantiate the Galtoons object, mytoons
mytoons = toons.Galtoons(halos=None, disks=mydisks, bulges=mybulges)


# ----------------------------------------------------------------------
# Realize the galtoons!

# Create the plot
ax = plt.subplot(111, aspect='equal', axisbg='black')

# Plot the galtoons
myplot = mytoons.plot_toons()

# Plot The Odyssey
plt.plot(-248.08737, 19.82660, 'or')
plt.text(-248.08737, 19.82660, 'The Odyssey', color='white')

# Make the plot nice
ax.set_xlim(-247.5,-248.7)
ax.set_ylim(19.2,20.4)
plt.xlabel('RA (arcsec)')
plt.ylabel('DEC (arcsec)')
plt.title('The Odyssey')
plt.grid(True, color='0.75')

# Save the plot and tell user what it's called
savedfile = "example-theodyssey.png"
plt.savefig(savedfile)
print "Plot saved as "+os.getcwd()+"/"+savedfile 
plt.show()

# ----------------------------------------------------------------------
