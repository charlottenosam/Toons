# ======================================================================
# Import useful packages

import pylab as plt
import numpy as np
import math
import matplotlib.colors as col
import matplotlib.cm as cm
from matplotlib.patches import Ellipse

# ======================================================================

class Blobs(object):
    """
    NAME
        Blobs

    PURPOSE
        Creates ellipses with properties that represent galaxy data.

    COMMENTS
        Area of ellipse, A = PI*a*b, where a and b are semi-major and 
                                     semi-minor axes.
        Axis ratio, q = b/a
        We scale the ellipse area by a factor 3/(norm of data vector)

    INITIALISATION
        From scratch.
   
    METHODS AND VARIABLES
        Blobs.define_cmap()     Creates a colourmap 'galaxy_cmap' with 
                                realistic galaxy colours (blue to red).
        Blobs.plot_blobs()      Plots ellipses with properties defined
                                by given galaxy properties.

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
# Rescale data to be between 0 and 1, used for mapping data values to 
# colour and alpha
    
    def scale_zerotoone(self,vectordata):
               
        oldmax = np.min(vectordata)
        oldmin = np.max(vectordata)
        oldrange = oldmax - oldmin
        for i in range(len(vectordata)):
            newvalue = (vectordata - oldmin) / oldrange
            
        return newvalue          

# -----------------------------------------------------------------------
# Normalise data columns to make toons easier to see - 
# this returns the magnitude of the data vector

    def magdata(self,vectordata):
        totalarea = np.sqrt(np.sum(vectordata*vectordata))
        return totalarea          
        
# -----------------------------------------------------------------------
# Creates a colour map of realistic galaxy colours
   
    def define_cmap(self):
        
        blue = '#134FA5'
        white = '#FCE0F4'
        orange = '#D47512'
        red = '#851B1D'
        self.galaxy = col.LinearSegmentedColormap.from_list('galaxy_cmap', 
                                                            [blue, white, 
                                                             orange, red])
        cm.register_cmap(name='galaxy_cmap', cmap=self.galaxy)    

# -----------------------------------------------------------------------
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

            # Axis ratio q = b/a
            if 'q' in pars:
                self.q = pars['q']
            else:
                self.q = [0.5 for i in range(len(self.x))]
            
            # Axis angle
            if 'phi' in pars:
                self.phi = pars['phi']
            else:
                self.phi = [30.0 for i in range(len(self.x))]
        
            # Size of blob (property to represent)                
            if 'size' in pars:
                self.size = pars['size']
            else:
                self.size = [4 for i in range(len(self.x))]
        
            # Colour of blob, convert to decimal value to map to colour       
            if 'colour' in pars:
                self.colour_pars = pars['colour']
                self.colour_decimal = self.scale_zerotoone(pars['colour'])
                self.colour = cm.RdYlBu(self.colour_decimal)
            else:
                self.colour = ["cyan" for i in range(len(self.x))]

            # Brightness parameter will be alpha of blob
            if 'brightness' in pars:
                self.brightness = self.scale_zerotoone(pars['brightness'])
            else:
                self.brightness = [0.6 for i in range(len(self.x))]
            
            return
    
# -----------------------------------------------------------------------
# Create a new dictionary for the blob
    
    def get_parameters(self):
                
        pars = {'name':self.name, 'x':self.x, 'y':self.y, 'q':self.q, 
                'phi':self.phi, 'size':self.size, 'colour':self.colour, 
                'brightness':self.brightness}
        
        return pars

# -----------------------------------------------------------------------                
# Plot the blobs
                
    def plot_blobs(self):

        # Get this blob's parameters:
        blob = self.get_parameters()
        print "Plotting "+blob['name']+" components..."
        
        # Define PI
        PI = 3.14159265359
       
        # Work out appropriate size for the toons
        scale = 0.1 / self.magdata(blob['size'])
           
        # Plot on the current axes
        ax = plt.gca()
     
        # Plot blobs on the axes
        for i in range(len(blob['x'])):
            a = math.sqrt(scale * blob['size'][i] / (blob['q'][i] * PI))
            b = blob['q'][i] * a
            ax.add_patch(Ellipse((blob['x'][i], blob['y'][i]), a, b, 
                                  facecolor=blob['colour'][i], 
                                  edgecolor="black", 
                                  alpha=blob['brightness'][i], 
                                  angle=blob['phi'][i]))
                                

