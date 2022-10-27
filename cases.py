import figures
Units=figures.Units
Figure=figures.Figure
def units(area,volume):
    
    units = Units(input("choose the unit: meters, centimeters millimeters:\n"))
    match units:
        case units.Meters:
            print("-"*40)
            print("area=",area,"m^2\nvolume=",volume,"m^3")
        case units.Centimeters:
            print("-"*40)
            print("area=",area,"cm^2\nvolume=",volume,"cm^3")
        case units.Millimeters:
            print("-"*40)
            print("area=",area,"mm^2\nvolume=",volume,"mm^3")

def Figures():
    figure = Figure(input("choose the figure:square, triangle, circle, cylinder, cube, cuboid:\n"))
    match figure:
        case figure.Square:
            print("you choosed square")
            a=int(input("enter a"))
            b=int(input("enter b"))
            area=a**2
            print("-"*40)
            units(area,volume=0)

        case figure.Triangle:
            print("you choosed triangle")
            print("-"*40)
            a=int(input("enter a"))
            h=int(input("enter h"))
            area=(a*h)/2
            units(area,volume=0)
        case figure.Circle:
            print("you choosed circle")
            print("-"*40)
            r=int(input("enter r"))
            area=3.14*r**2
            units(area,volume=0)
        case figure.Cylinder:
            print("you choosed cylinder")
            print("-"*40)
            r=int(input("enter r"))
            h=int(input("enter h"))
            area=2*3.14*r**2+h*(2*r*3.14)
            volume=3.14*r**2*h
            units(area,volume)
        case figure.Cube:
            print("you choosed cube")
            print("-"*40)
            a=int(input("enter a"))
            area=6*a**2
            volume=a**3
            units(area,volume)
        case figure.Cuboid:
            print("you choosed cuboid")
            print("-"*40)
            a=int(input("enter a"))
            b=int(input("enter b"))
            h=int(input("enter h"))
            area=2*(a*h)+2*(a*b)+2*(b*h)
            volume=a*b*h
            units(area,volume)