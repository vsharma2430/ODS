from object_threeD import object_3d
from material import concrete

# FOUNDATION CONFIGURATION 
# 1. PEDESTAL
# 2. FOUNDATION
# 3. PILES

# SURROUNDINGS CONFIG
# 1. GROUND (HPP AND NGL)
# 2. WATER LEVEL 

highest_pavement_point = 1.5
natural_ground_level = 1.0
water_level = 0.5

class foundation : 
    pedestal = object_3d("octagon",1.0)
    pedestal.material = concrete
    pedestal.top_elevation = 5.0
    pedestal.bottom_elevation = 2.0
    pedestal.water_elevation = water_level

    foundation = object_3d("octagon",2.0)
    foundation.material = concrete
    foundation.top_elevation = pedestal.bottom_elevation
    foundation.bottom_elevation = 0
    foundation.water_elevation = water_level
    
    piles = []