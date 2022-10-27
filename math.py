
from operator import contains
import figures
import cases
import methods
import tests
import argparse
import math
from unittest import TestCase
from pickle import TRUE
from typing import List
volume:int
pi=math.pi
Units=figures.Units
Figure=figures.Figure

myTest=tests.TryTesting()
contains
parser = argparse.ArgumentParser(prog="math",usage='%(prog)s [options]', description='Aplication Math 1.0')
parser.add_argument("-i","--interactive",action="store_true", help="interactive mode")
parser.add_argument("-f","--figure", help =" enum[square,triangle, circle, cylinder, cube]", default = "def")
parser.add_argument("-p","--params",action="append",help= "list of parameters depends on figure")
parser.parse_args("-p 1 -p 2 -p 3".split())
parser.add_argument("-u","--unit",type=str, help = "enum[meters, centimeters, millimeters]", default = "def")

my_args = parser.parse_args()
converted=vars(my_args)
if converted["interactive"]!=True:
    figure=Figure(converted["figure"])
    match figure:
        case figure.Square:
            print("-"*40)
            units=Units(converted["unit"])
            match units:
                case units.Meters:
                    a=int(converted["params"][0])
                    u="m^2"
                    print(methods.square_message(methods.square_area(a),u))
                case units.Centimeters:
                    a=int(converted["params"][0])
                    u="cm^2"
                    print(methods.square_message(methods.square_area(a),u))
                case units.Millimeters:
                    a=int(converted["params"][0])
                    u="mm^2"
                    print(methods.square_message(methods.square_area(a),u))

        case figure.Triangle:
            print("-"*40)
            units=Units(converted["unit"])
            match units:
                case units.Meters:
                    r=int(converted["params"][0])
                    h=int(converted["params"][1])
                    u="m2"
                    print(methods.triangle_message(methods.triangle_area(r,h),u))
                case units.Centimeters:
                    r=int(converted["params"][0])
                    h=int(converted["params"][1])
                    u="cm2"
                    print(methods.triangle_message(methods.triangle_area(r,h),u))
                case units.Millimeters:
                    r=int(converted["params"][0])
                    h=int(converted["params"][1])
                    u="mm2"
                    print(methods.triangle_message(methods.triangle_area(r,h),u))
            
        case figure.Circle:
            print("-"*40)
            units=Units(converted["unit"])
            match units:
                case units.Meters:
                    a=int(converted["params"][0])
                    u="m^2"
                    print(methods.circle_message(methods.circle_area(a),u))
                case units.Centimeters:
                    a=int(converted["params"][0])
                    u="cm^2"
                    print(methods.circle_message(methods.circle_area(a),u))
                case units.Millimeters:
                    a=int(converted["params"][0])
                    u="mm^2"
                    print(methods.circle_message(methods.circle_area(a),u))
        case figure.Cylinder:
            print("-"*40)
            units=Units(converted["unit"])
            match units:
                case units.Meters:
                    r=int(converted["params"][0])
                    h=int(converted["params"][1])
                    u1="m^2"
                    u2="m^3"
                    print(methods.cylinder_message(methods.cylinder_area(r,h),u1,methods.cylinder_volume(r,h),u2))
                case units.Centimeters:
                    r=int(converted["params"][0])
                    h=int(converted["params"][1])
                    u1="cm^2"
                    u2="cm^3"
                    print(methods.cylinder_message(methods.cylinder_area(r,h),u1,methods.cylinder_volume(r,h),u2))
                case units.Millimeters:
                    r=int(converted["params"][0])
                    h=int(converted["params"][1])
                    u1="mm^2"
                    u2="mm^3"
                    print(methods.cylinder_message(methods.cylinder_area(r,h),u1,methods.cylinder_volume(r,h),u2))
        case figure.Cube:
            print("-"*40)
            units=Units(converted["unit"])
            match units:
                case units.Meters:
                    a=int(converted["params"][0])
                    u1="m^2"
                    u2="m^3"
                    print(methods.cube_message(methods.cube_area(a),u1,methods.cube_volume(a),u2))
                case units.Centimeters:
                    a=int(converted["params"][0])
                    u1="cm^2"
                    u2="cm^3"
                    print(methods.cube_message(methods.cube_area(a),u1,methods.cube_volume(a),u2))
                case units.Millimeters:
                    a=int(converted["params"][0])
                    u1="mm^2"
                    u2="mm^3"
                    print(methods.cube_message(methods.cube_area(a),u1,methods.cube_volume(a),u2))
        case figure.Cuboid:
            print("-"*40)
            units=Units(converted["unit"])
            match units:
                case units.Meters:
                    a=int(converted["params"][0])
                    b=int(converted["params"][1])
                    h=int(converted["params"][2])
                    u1="m^2"
                    u2="m^3"
                    print(methods.cuboid_message(methods.cuboid_area(a,b,h),u1,methods.cuboid_volume(a,b,h),u2))
                case units.Centimeters:
                    a=int(converted["params"][0])
                    b=int(converted["params"][1])
                    h=int(converted["params"][2])
                    u1="cm^2"
                    u2="cm^3"
                    print(methods.cuboid_message(methods.cuboid_area(a,b,h),u1,methods.cuboid_volume(a,b,h),u2))
                case units.Millimeters:
                    a=int(converted["params"][0])
                    b=int(converted["params"][1])
                    h=int(converted["params"][2])
                    u1="mm^2"
                    u2="mm^3"
                    print(methods.cuboid_message(methods.cuboid_area(a,b,h),u1,methods.cuboid_volume(a,b,h),u2))
else:
    cases.Figures()


    
