# -*- coding: utf-8 -*-
# Example plots using galtoons

# Plotting the catalogue of galaxies around "The Odyssey"

# ======================================================================

# Import useful packages
import pylab as plt
import numpy as np
import os
import toons
 
# ======================================================================
# Read in the data

odyssey_array = np.loadtxt('The_Odyssey_g-r_GIM2D.txt')

# Extract useful data from table
# RA and DEC co-ordinates in arcsec 
ra = odyssey_array[:,14]
dec = odyssey_array[:,15]
# Redshift
z = odyssey_array[:,2]
# Magnitudes
gmag = odyssey_array[:,5]
rmag = odyssey_array[:,6]
# Bulge fraction:
bulgefrac = odyssey_array[:,7]
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


# Axis ratio
bulge_q = 1.0 - bulge_e

# Bulge area in arcsec
bulge_Re_arcsec = bulge_Re_kpc / scale_kpc_arcsec
bulge_size = PI * bulge_q * bulge_Re_arcsec * bulge_Re_arcsec

# Disk area in arcsec
disk_Re_kpc = 1.678 * disk_Rd_kpc
disk_Re_arcsec = disk_Re_kpc / scale_kpc_arcsec
disk_size = PI * disk_Re_arcsec * disk_Re_arcsec

# Fluxes and colors - catalog only has one colour, unfortunately:
rflux = pow(10.0, -2.5 * rmag)
bulge_rflux = rflux*bulgefrac
disk_rflux = rflux*(1.0 - bulgefrac)
grcolour = gmag - rmag

# Mean surface brightness within Re:
bulge_rflux[bulge_rflux==0.0] = 6.28e-12 # replace all 0 values
bulge_Re_arcsec[bulge_Re_arcsec==0.0] = 0.001 # replace all 0 values
bulge_sb = -2.5*np.log10(bulge_rflux / (2.0 * PI * (bulge_Re_arcsec**2)))  
disk_rflux[disk_rflux==0.0] = 6.28e-12 # replace all 0 values
disk_Re_arcsec[disk_Re_arcsec==0.0] = 0.001 # replace all 0 values
disk_sb = -2.5*np.log10(disk_rflux / (2.0 * PI * (disk_Re_arcsec**2)))  

# ----------------------------------------------------------------------
# Create bulges, disks and halo dictionaries. Initialise them in Galtoons

mybulges = {'name':'bulge', 'x':ra, 'y':dec, 'z':z, 'size':bulge_size, 
            'phi':bulge_phi, 'q':bulge_q, 'colour':grcolour, 
            'colourname':'g-r colour', 'brightness':bulge_sb}
            
mydisks = {'name':'disk', 'x':ra, 'y':dec, 'z':z, 'size':disk_size, 
           'phi':disk_phi, 'colour':grcolour, 'colourname':'g-r colour', 
           'brightness':disk_sb}

# Instantiate the Galtoons object, mytoons

mytoons = toons.Galtoons(halos=None, disks=mydisks, bulges=mybulges)


# ----------------------------------------------------------------------
# Draw the galtoons!

# Create the plot:
ax = plt.subplot(111, aspect='equal', axisbg='black')

# Plot the galtoons:
myplot = mytoons.plot()

# Plot The Odyssey as a green point in the centre of the field:
ra0 = 248.0873
dec0 = 19.82660
plt.plot(ra0, dec0, '+g')
# plt.text(ra0, dec0, 'The Odyssey', color='white')
circ = plt.Circle((ra0, dec0), radius=0.45, edgecolor='g', facecolor='none')
ax.add_patch(circ)

# Make the plot nice:
ax.set_xlim(248.6,247.6)
ax.set_ylim(19.3,20.3)
plt.xlabel('RA (deg)')
plt.ylabel('DEC (deg)')
plt.title('The Odyssey')
plt.grid(True, color='0.75')

# Save the plot and tell the user what it's called:
savedfile = "example-theodyssey.png"
plt.savefig(savedfile,dpi=300)
print "Plot saved as "+os.getcwd()+"/"+savedfile 
# plt.show()

# ----------------------------------------------------------------------
