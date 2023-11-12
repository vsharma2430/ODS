from misc import gravity_constant,tonneToN,MPaToPa

class soil_property :
    soil_capacity = tonneToN(10)       #t/m2 to n/m2
    coeff_friction = 0.3

class steel_property :
    fy :float      #in Pa / Yield strength
    ft :float      #in Pa / Tensile strength

class concrete_property : 
    fck :float     #compressive strength 
    fct :float     #tensile strength 


class material : 
    name = "material_name"
    material_grade = "material_grade"
    density :float
    sub_water_density :float
    elasticity_modulus :float

    def __init__(self, name , material_grade , density):
        self.name = name
        self.material_grade = material_grade
        self.density = density
        self.sub_water_density = density - tonneToN(1.0)
        if(name == "soil"):
            self.property = soil_property()
        elif(name == "steel"):
            self.property = steel_property()
        elif(name == "concrete"):
            self.property = concrete_property()
            

concrete = material("concrete","M30" , tonneToN(2.5))
concrete.property.fck=MPaToPa(30)
steel = material("steel","FE500" ,tonneToN(7.85))
steel.property.fy = MPaToPa(500)
pcc = material("pcc","1:5:10" , tonneToN(2.4))
water = material("water","water" , tonneToN(1.0))
soil = material("soil","soil",tonneToN(1.8))
submerged_soil = material("soil","submerged_soil",tonneToN(1.1))


def calculate_sbc_gross(sbc_net,natural_ground_level,bottom_of_foundation,water_level,soil_density,sub_soil_density,sbc_increase) :
        return sbc_net * (1+sbc_increase)  + \
            ((natural_ground_level - bottom_of_foundation)*soil_density)
    
def calculate_sbc_gross_water(sbc_net,natural_ground_level,bottom_of_foundation,water_level,soil_density,sub_soil_density,sbc_increase) :
    if(water_level < bottom_of_foundation) : 
        return sbc_net * (1+sbc_increase)  + \
            ((natural_ground_level - bottom_of_foundation)*soil_density)
    else:
        return sbc_net * (1+sbc_increase) + \
            max(((natural_ground_level - bottom_of_foundation)*soil_density),0)  + \
            max((water_level-bottom_of_foundation)*sub_soil_density,0)
        
#print(calculate_sbc_gross(2,natural_ground_level,0,1.5,soil.density,submerged_soil.density,1.25))