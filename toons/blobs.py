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

# Initiate the Blobs class by importing the toons' components' properties:

    def __init__(self, pars):        
        self.hello = "blobs says 'hello there'"
        self.name = None
        
        # Initialise variables:
        self.exist = False
        self.x = None
        self.y = None 
        self.q = None
        self.phi = None 
        self.size = None 
        self.colour = None 
        self.brightness = None
        
        # Now set according to argument:
        self.set_parameters(pars)
        
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

        if pars is not None:
            
            if 'name' in pars:
                self.name = pars['name']
            else:
                self.name = None
            
            # x co-ordinates
            if 'x' in pars:
                self.x = pars['x']
            else:
                self.x = None
                print "Warning: you must set x co-ordinates for a blob to exist..."
        
            # y co-ordinates    
            if 'y' in pars:
                self.y = pars['y']
            else:
                self.y = None
                print "Warning: you must set y co-ordinates for a blob to exist..."

            # Now we know if these blobs exist:
            if self.x == None or self.y == None:
                self.exist = False
                return
            else:
                self.exist = True

            # axis ratio q = b/a
            if 'q' in pars:
                self.q = pars['q']
            else:
                self.q = [0.5 for i in range(len(self.x))]
            
            # axis angle
            if 'phi' in pars:
                self.phi = pars['phi']
            else:
                self.phi = [30.0 for i in range(len(self.x))]
        
            # size of blob (property to represent)                
            if 'size' in pars:
                self.size = pars['size']
            else:
                self.size = [4 for i in range(len(self.x))]
        
            # colour of blob        
            if 'colour' in pars:
                self.colour = pars['colour']
            else:
                self.colour = ["cyan" for i in range(len(self.x))]

            # brightness parameter will be alpha of blob
            if 'brightness' in pars:
                self.brightness = self.percentdata(pars['brightness'])
                if i in range(len(self.x)) > 10:
                    self.brightness = 10*self.percentdata(pars['brightness']) 
            else:
                self.brightness = [0.8 for i in range(len(self.x))]
            return
    
# -----------------------------------------------------------------------

# Create a new dictionary for the blob
    
    def get_parameters(self):
                
        pars = {'name':self.name, 'x':self.x, 'y':self.y, 'q':self.q, 'phi':self.phi, 
                   'size':self.size, 'colour':self.colour, 'brightness':self.brightness}
        # print "In get_parameters, pars = ",pars
        
        return pars

# -----------------------------------------------------------------------                

# Plot the blobs
                
    def plot_blobs(self):

        # Get this blob's parameters:
        blob = self.get_parameters()
        print "Plotting "+blob['name']+" components..."
        
        # define PI
        PI = 3.14159265359
       
        # work out appropriate size for the toons
        scale = 0.25 / self.magdata(blob['size'])
           
        # plot on the current axes
        ax = plt.gca()
     
        # plot disks
        for i in range(len(blob['x'])):
            a = math.sqrt(scale * blob['size'][i] / (blob['q'][i] * PI))
            b = blob['q'][i] * a
            ax.add_patch(Ellipse((blob['x'][i], blob['y'][i]), a, b, 
                                facecolor=blob['colour'][i], edgecolor="black", 
                                alpha=blob['brightness'][i], angle=blob['phi'][i]))
