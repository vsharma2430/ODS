import math
from material import material
from material import water
import markdown2
from markdown2 import Markdown

markdowner = Markdown()

class point :
    x = 1.0
    y = 1.0
    z = 1.0

class shape:
    def area(self):
        pass
    def section_modulus_major(self):
        pass
    def section_modulus_minor(self):
        pass
    def dimension(self):
        pass

class shape_circle (shape):
    center : point
    radius = 1.0
    area_factor = math.pi/4.0
    section_modulus_factor = math.pi/32.0

    def dimension(self):
        return self.radius
    def area(self):
        return self.area_factor * self.radius * self.radius
    def section_modulus_minor(self):
        return self.section_modulus_factor * self.radius * self.radius * self.radius

class shape_square (shape):
    center : point
    side : float
    area_factor = 1.0
    section_modulus_factor = 0.16666667

    def dimension(self):    
        return self.side
    def area(self):
        return self.area_factor * self.side * self.side
    def perimeter(self):
        return 2 * math.pi * self.side 
    def section_modulus_minor(self):
        return self.section_modulus_factor * self.side * self.side * self.side

class shape_rectangle (shape):
    center : point
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
    center : point
    side : float
    area_factor = 0.866
    section_modulus_factor = 0.1042
    section_modulus_mm_factor =  0.1203

    def dimension(self):    
        return self.side
    def area(self):
        return self.area_factor * self.side * self.side
    def section_modulus_minor(self):
        return self.section_modulus_factor * self.side * self.side * self.side
    def section_modulus_major(self):
        return self.section_modulus_mm_factor * self.side * self.side * self.side
   
class shape_octagon (shape):
    center : point
    side : float
    area_factor = 2 * (1 + math.sqrt(2))
    section_modulus_factor = 1.540437583
    section_modulus_mm_factor = 1.423178754            #0.1011422 * cube(D)
    #PIP Factors
    side_diagonal_factor = 2.414213562
    side_diameter_factor = 2.613125929
    diagonal_diameter_factor = 1.0823922

    def dimension(self):    
        return self.side
    def area(self):
        return self.area_factor * self.side * self.side
    def section_modulus_minor(self):
        return self.section_modulus_factor * self.side * self.side * self.side
    def section_modulus_major(self):
        return self.section_modulus_mm_factor * self.side * self.side * self.side

class object_3d : 
    shape_name : str
    shape_object : shape
    bottom_elevation : float
    top_elevation : float
    water_elevation : float
    material : material

    def properties_report(self):
        report_html_list = []
        report_html_list.append("| Property | Value |" + "\n" + "| --- | --- |")
        report_html_list.append("| Shape | " + self.shape_name + "|")
        report_html_list.append("| Dimension | " + str(self.shape_object.dimension())+ "|")
        report_html_list.append("| Top Elevation | " + str(self.top_elevation)+ "|")
        report_html_list.append("| Bottom Elevation | " + str(self.bottom_elevation)+ "|")
        report_html_list.append("| Density | " + str(self.material.density)+ "|")
        report_html_list.append("| Area | " + str(self.shape_object.area())+ "|")
        report_html_list.append("| Section Modulus (major) | " + str(self.shape_object.section_modulus_major())+ "|")
        report_html_list.append("| Section Modulus (minor) | " + str(self.shape_object.section_modulus_minor())+ "|")
        report_html_list.append("| Weight | " + str(self.weight())+ "|")
        return markdown2.markdown(text="\n".join(report_html_list), extras=["tables"])

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
