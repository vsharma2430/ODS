import math
from material import material
from material import water

class point :
    x = 1.0
    y = 1.0
    z = 1.0

class shape : 
    points = []

class shape_circle :
    center = point()
    radius = 1.0
    area_factor = math.pi/4.0
    section_modulus_factor = math.pi/32.0
    
    def area(self):
        return self.area_factor * radius * radius

class shape_square :
    center = point()
    side = 1.0
    area_factor = 1.0
    section_modulus_factor = 0.16666667

    def area(self):
            return self.area_factor * side * side

class shape_rectangle :
    center = point()
    width_x = 1.0
    length_y = 1.0

class shape_hexagon :
    center = point()
    side = 1.0
    area_factor = 0.866
    section_modulus_factor = 0.1042
    section_modulus_mm_factor =  0.1203

    def area(self):
            return self.area_factor * side * side

   
class shape_octagon :
    center = point()
    side = 1.0
    area_factor = 0.828427125
    section_modulus_factor = 0.079758898
    section_modulus_mm_factor = 0.073687764

    def area(self):
            return self.area_factor * side * side


class object_3d : 
    shape_name = "shape_name"
    shape 
    bottom_elevation = 1.0
    top_elevation = 1.0
    water_elevation = 1.0
    material = material("material_name","material_grade",1.0)

    def __init__(self, shape_name,dimension):
        self.shape_name = shape_name
        if(self.shape_name == "square"):
            self.shape = shape_square()
            self.shape.side = dimension
        elif(self.shape_name == "circle"):
            self.shape = shape_circle()
            self.shape.radius = dimension
        elif(self.shape_name == "hexagon"):
            self.shape = shape_circle()
            self.shape.side = dimension
        elif(self.shape_name == "octagon"):
            self.shape = shape_octagon()
            self.shape.side = dimension
    
    
        







