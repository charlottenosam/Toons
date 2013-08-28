# ======================================================================

import pylab as plt
import numpy as np
import math
from matplotlib.patches import Ellipse

# ======================================================================

class Blobs(object):
    """
    NAME
        Blobs

    PURPOSE
        Creates ellipses with properties that represent galaxy data.

    COMMENTS
        Area of ellipse, A = PI*a*b, where a and b are semi-major and semi-minor axes.
        Axis ratio, q = b/a.
        We scale the ellipse area by a factor 3/(norm of data vector).

    INITIALISATION
    
    METHODS AND VARIABLES
        Blobs.normdata(vectordata)      Finds the norm of a given column of data
        Blobs.plot_blobs()              Plots ellipses with properties defined by given galaxy properties
        
    BUGS

    AUTHORS
        Charlotte A. Mason (UCSB)

    LICENSE
        GPLv2

    HISTORY
      2013-08-25  Started (C Mason)
    """
# ----------------------------------------------------------------------
# ----------------------------------------------------------------------

    def __init__(self, x, y, q, phi, size, colour, brightness):        
        self.hello = "blobs says 'hello there'"
        self.x = x
        self.y = y
        self.q = q
        self.phi = phi
     #   if phi = None:
    #        self.phi = -70.0
        self.size = size
        self.colour = colour
        self.brightness = brightness
        
# -----------------------------------------------------------------------

# Normalise data columns to make toons easier to see - 
# 'area' will be the area of the toon
    def normdata(self, vectordata):

        unitarea = np.sqrt(np.sum(vectordata*vectordata))
      #  area = vectordata/unitarea   
        return unitarea          

# -----------------------------------------------------------------------

def plot_blobs(self):
        # define PI
        PI = 3.14159265359
       
        # work out appropriate size for the toons
        normarea = self.normdata(self.size)
        scale = 3 / normarea
           
        # plot on the current axes
        ax = plt.gca()
     
        # plot disks
        for i in range(len(self.size)):
            a = math.sqrt(scale * self.size[i] / (self.q * PI))
            b = self.q * a
            ax.add_patch(Ellipse((self.x[i], self.y[i]), a, b, 
                                facecolor=self.colour, edgecolor="black", 
                                alpha=self.brightness, angle=self.phi))
