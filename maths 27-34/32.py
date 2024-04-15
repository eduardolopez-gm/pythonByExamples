""" Ask for the radius and the depth of a cylinder
and work out the total volume (circle
area*depth) rounded to three decimal
places.  """
import math

radius = int(input('Enter a radius of the cylinder: '))
depth = int(input('Enter the depth of the cylinder: '))
volume = (math.pi * radius **2 ) * depth
print('Volume of the cylinder is -> ', round(volume, 3))


