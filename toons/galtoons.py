# ======================================================================
# Import useful packages

from blobs import *

# ======================================================================

class Galtoons(object):
    """
    NAME
        Galtoons

    PURPOSE
        Represent galaxy data as a set of matplotlib patches. Superimposes 3 "blobs"
        to represent halos, disks and bulges.

    COMMENTS

    INITIALISATION
    
    METHODS AND VARIABLES
        
    BUGS

    AUTHORS
        Charlotte A. Mason (UCSB)

    LICENSE
        GPLv2

    HISTORY
      2013-07-18  Started (C Mason)
    """
# ----------------------------------------------------------------------
# ----------------------------------------------------------------------

# Initiate the Galtoons class - make bulge, disk and halo Blob objects

    def __init__(self, bulges=None, disks=None, halos=None):        
        self.hello = "galtoons says 'hello there'"
#         self.bulgeblobs = Blobs(bulges)
#         self.diskblobs = Blobs(disks)
#         self.haloblobs = Blobs(halos)
#         self.allblobs = {'bulges':self.bulgeblobs, 'disks':self.diskblobs, 'halos':self.haloblobs}

# Phil's more compact version:
        self.components = {'bulges':Blobs(bulges), 'disks':Blobs(disks), 'halos':Blobs(halos)}

# -----------------------------------------------------------------------

# Plot galtoons made up of up to 3 blobs:

    def plot_toons(self):

        # Loop over halos, disks and bulges:
        for ofTypeX in self.components:
        
            if self.components[ofTypeX].exist:
                                
                self.components[ofTypeX].plot_blobs()
