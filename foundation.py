from object_threeD import object_3d
from material import concrete

# FOUNDATION CONFIGURATION 
# 1. PEDESTAL
# 2. FOUNDATION
# 3. PILES

# SURROUNDINGS CONFIG
# 1. GROUND (HPP AND NGL)
# 2. WATER LEVEL 

class surroundings :
    highest_pavement_point : float
    natural_ground_level : float
    water_level : float

    def __init__(self,highest_pavement_point,natural_ground_level,water_level):
        self.highest_pavement_point = highest_pavement_point
        self.natural_ground_level = natural_ground_level
        self.water_level = water_level

class open_foundation : 
    pedestal : object_3d
    foundation : object_3d

    def __init__(self,pedestal,foundation):
        self.pedestal = pedestal
        self.foundation = foundation