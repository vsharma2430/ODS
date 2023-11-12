from bolt import bolt_data
from load import vessel_load

class vessel_segment:
    bottom_elevation :float
    top_elevation :float
    diameter :float
    shape_factor :float

class equipment : 
    bolt : bolt_data
    load : vessel_load
    vessel_segments = []