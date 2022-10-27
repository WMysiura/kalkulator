from enum import Enum
class Figure (Enum):
    
    Square = "square"
    Triangle = "triangle" 
    Circle = "circle"
    Cylinder = "cylinder"
    Cube = "cube"
    Cuboid = "cuboid"
    
class Units(Enum):
    
    Meters = "meters"
    Centimeters = "centimeters"
    Millimeters = "millimeters"