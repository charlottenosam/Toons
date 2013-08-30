# ======================================================================
# Import useful packages

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

# Initiate the Blobs class - import the galaxy properties and plot

    def __init__(self, pars):        
        self.hello = "blobs says 'hello there'"
        self.set_parameters(pars)   
        self.x = None
        self.y = None 
        self.q = None
        self.phi = None 
        self.size = None 
        self.colour = None 
        self.brightness = None
        return

# -----------------------------------------------------------------------

# Normalise data columns to make toons easier to see - 
# this returns the magnitude of the data vector
    def magdata(self,vectordata):
        totalarea = np.sqrt(np.sum(vectordata*vectordata))
        return totalarea          


# ----------------------------------------------------------------------

# Normalise data columns to make toons easier to see - 
# this returns the normalised data (divide by magnitude)
    def normdata(self,vectordata):
        normarea = vectordata/self.magdata(vectordata)
        return normarea          

# ----------------------------------------------------------------------

# Finds data values as a percentage of the total value - used to provide
# alpha values for brightness etc.
    def percentdata(self,vectordata):       
        totaldata = np.sum(vectordata)
        percentarea = vectordata/totaldata
        return percentarea          

# ----------------------------------------------------------------------

# Define the parameters for the blobs      
    def set_parameters(self,pars):
        # x co-ordinates
        if pars is not None:
            if 'x' in pars:
                self.x = pars['x']
            else:
                self.x = None
                print "You must set x co-ordinates"
        
        # y co-ordinates    
            if 'y' in pars:
                self.y = pars['y']
            else:
                self.y = None
                print "You must set y co-ordinates"

        # axis ratio q = b/a
            if 'q' in pars:
                self.q = pars['q']
            else:
                self.q = [0.5 for i in range(len(self.x))]
            
        # axis angle
            if 'phi' in pars:
                self.phi = pars['phi']
            else:
                self.phi = [-30.0 for i in range(len(self.x))]
        
        # size of blob (property to represent)                
            if 'size' in pars:
                self.size = pars['size']
            else:
                self.size = [4 for i in range(len(self.x))]
        
        # colour of blob        
            if 'colour' in pars:
                self.colour = pars['colour']
            else:
                self.colour = ["blue" for i in range(len(self.x))]

        # brightness parameter will be alpha of blob
            if 'brightness' in pars:
                self.brightness = self.percentdata(pars['brightness'])
                if i in range(len(self.x)) > 10:
                    self.brightness = 10*self.percentdata(pars['brightness']) 
                print self.brightness
            else:
                self.brightness = [0.8 for i in range(len(self.x))]
            return
    
# -----------------------------------------------------------------------

# Create a new dictionary for the blob
# !!! But it won't recognise self.x from earlier... What's gone wrong? !!! #
# I get the error "'Blobs' object has no attribute 'x'" #
    
    def get_parameters(self):
#        self.myblob = vars(self)
#        print self.myblob
        self.myblob = {'x':self.x, 'y':self.y, 'q':self.q, 'phi':self.phi, 
                   'size':self.size, 'colour':self.colour, 'brightness':self.brightness}
        return self.myblob

# -----------------------------------------------------------------------                

# Plot the blobs
                
    def plot_blobs(self):
        # get the parameters
        blob = self.get_parameters()
        print blob
        # define PI
        PI = 3.14159265359
       
        # work out appropriate size for the toons
        scale = 3 / self.magdata(blob['size'])
           
        # plot on the current axes
        ax = plt.gca()
     
        # plot disks
        for i in range(len(blob['x'])):
            a = math.sqrt(scale * blob['size'][i] / (blob['q'][i] * PI))
            b = blob['q'][i] * a
            ax.add_patch(Ellipse((blob['x'][i], blob['y'][i]), a, b, 
                                facecolor=blob['colour'][i], edgecolor="black", 
                                alpha=blob['brightness'][i], angle=blob['phi'][i]))
