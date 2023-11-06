import math
from material import material
from material import water

class point :
    x = 1.0
    y = 1.0
    z = 1.0

class shape:
    def area(self):
        pass

class shape_circle (shape):
    center = point()
    radius = 1.0
    area_factor = math.pi/4.0
    section_modulus_factor = math.pi/32.0
    
    def area(self):
        return self.area_factor * self.radius * self.radius
    def section_modulus(self):
        return self.section_modulus_factor * self.radius * self.radius * self.radius

class shape_square (shape):
    center = point()
    side : float
    area_factor = 1.0
    section_modulus_factor = 0.16666667

    def area(self):
        return self.area_factor * self.side * self.side
    def perimeter(self):
        return 2 * math.pi * self.side 
    def section_modulus(self):
        return self.section_modulus_factor * self.side * self.side * self.side

class shape_rectangle (shape):
    center = point()
    width_x : float
    length_y : float

class Triangle(shape):
    def __init__(self, base, height, side1, side2, side3):
        self.base = base
        self.height = height
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def area(self):
        return 0.5 * self.base * self.height
    def perimeter(self):
        return self.side1 + self.side2 + self.side3

class shape_hexagon (shape):
    center = point()
    side : float
    area_factor = 0.866
    section_modulus_factor = 0.1042
    section_modulus_mm_factor =  0.1203

    def area(self):
        return self.area_factor * self.side * self.side
    def section_modulus(self):
        return self.section_modulus_factor * self.side * self.side * self.side
    def section_modulus_mm(self):
        return self.section_modulus_mm_factor * self.side * self.side * self.side
   
class shape_octagon (shape):
    center = point()
    side : float
    area_factor = 0.828427125
    section_modulus_factor = 0.079758898
    section_modulus_mm_factor = 0.073687764

    def area(self):
        return self.area_factor * self.side * self.side
    def section_modulus(self):
        return self.section_modulus_factor * self.side * self.side * self.side
    def section_modulus_mm(self):
        return self.section_modulus_mm_factor * self.side * self.side * self.side

class object_3d : 
    shape_name : str
    shape_object : shape
    bottom_elevation : float
    top_elevation : float
    water_elevation : float
    material : material

    def __init__(self, shape_name,dimension):
        self.shape_name = shape_name
        if(self.shape_name == "square"):
            self.shape_object = shape_square()
            self.shape_object.side = dimension
        elif(self.shape_name == "circle"):
            self.shape_object = shape_circle()
            self.shape_object.radius = dimension
        elif(self.shape_name == "hexagon"):
            self.shape_object = shape_circle()
            self.shape_object.side = dimension
        elif(self.shape_name == "octagon"):
            self.shape_object = shape_octagon()
            self.shape_object.side = dimension
    
    def weight_water(self):
        area = self.shape_object.area() 
        weight1 = max (self.top_elevation - self.bottom_elevation , 0) * area * self.material.density
        weight2 = max (self.water_elevation - self.bottom_elevation , 0) * area * water.density
        return weight1 + weight2
    
    def weight(self):
        area = self.shape_object.area() 
        weight = max (self.top_elevation - self.bottom_elevation , 0) * area * self.material.density
        return weight
    
    def weight_negative(self):
        area = self.shape_object.area() 
        weight = (self.top_elevation - self.bottom_elevation) * area * self.material.density
        return weight
        







