import argparse
import figures
import cases
from math import pi

def square_area(a):
    return a**2

# w klasie pochodnej TestCase
# def test_square_area_with_side_equal_one(self):
#     self.assertEqual(1, square_area(1))
#     self.assertEqual(1, square_area(1))
#     self.assertEqual(1, square_area(1))

def triangle_area(a,h):
    return (a*h)/2

def circle_area(r):
    return pi*r**2

def cylinder_area(r,h):
    return 2*pi*r**2+h*(2*r*pi)

def cylinder_volume(r,h):
    return pi*r**2*h

def cube_area(a):
    return 6*a**2

def cube_volume(a):
    return a**3

def cuboid_area(a,b,h):
    return 2*(a*h)+2*(a*b)+2*(b*h)

def cuboid_volume(a,b,h):
    return a*b*h

def square_message(area, unit):
    return "Square area="+ str(area)+" "+unit

def triangle_message(area,unit):
    return "Triangle area="+str(area)+" "+unit

def circle_message(area, unit):
    return "circle area="+ str(area)+" "+unit

def cylinder_message(area,unit1,volume,unit2):
    return "cylinder area="+ str(area)+" "+unit1+"\n"+"cylinder volume="+str(volume)+" "+unit2

def cube_message(area,unit1,volume,unit2):
    return "cube area="+ str(area)+" "+unit1+"\n"+"cube volume="+str(volume)+" "+unit2

def cuboid_message(area,unit1,volume,unit2):
    return "cuboid area="+ str(area)+" "+unit1+"\n"+"cuboid volume="+str(volume)+" "+unit2



