""" Ask the user to enter the radius of a circle
(measurement from the centre point to the edge). Work
out the area of the circle (π*radius2).  """
import math

radius = int(input('Enter a radius of a circle: '))
area = math.pi * radius **2
print('Area of the circle is -> ', round(area,3))

