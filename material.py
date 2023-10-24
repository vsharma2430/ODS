class soil_property :
    soil_capacity = 1.0
    coeff_friction = 0.3
    soil_capacity_wind_increase = 0.25
    soil_capacity_seismic_dbe_increase = 0.5
    soil_capacity_seismic_mce_increase = 0.5

class material : 
    name = "material_name"
    material_grade = "material_grade"
    density = 1.0
    sub_water_density = 1.0
    elasticity_modulus = 1.0

    def __init__(self, name , material_grade , density):
        self.name = name
        self.material_grade = material_grade
        self.density = density

        if(name == "soil"):
            self.property = soil_property()
            

concrete = material("concrete","M30" , 2.5)
steel = material("steel","FE500" , 7.85)
pcc = material("pcc","1:5:10" , 2.4)
water = material("water","water" , 1.0)
soil = material("soil","soil",1.8)
    