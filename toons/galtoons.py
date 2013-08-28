# ======================================================================

import pylab as plt
import numpy as np
import math
from matplotlib.patches import Ellipse
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

    def __init__(self, disks=None, bulges=None, halos=None):        
        self.hello = "galtoons says 'hello there'"
        haloblobs = None
#         haloblobs = Blobs(halos)
        diskblobs = Blobs(disks)
        bulgeblobs = Blobs(bulges)
        self.components = {'halos':haloblobs, 'disks':diskblobs, 'bulges':bulgeblobs}

# -----------------------------------------------------------------------

# Plot galtoons made up of up to 3 blobs

    def plot_toons(self, haloblobs, diskblobs, bulgeblobs):
        
        for k in self.components:
            if self.components[k] is not None:
                self.components[k].plot_blobs()

    
