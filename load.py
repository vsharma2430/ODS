class load_data:
    moment : float
    shear : float
    moment_factor : float
    shear_factor : float

    def __init__(self,moment=1.0,shear=1.0,moment_factor = 1.0,shear_factor=1.0):
        self.moment = moment
        self.shear = shear
        self.moment_factor = moment_factor
        self.shear_factor = shear_factor

class vessel_load : 
    #VESSEL LOADS
    empty_load : load_data
    erection_load : load_data
    operating_load : load_data
    testing_load : load_data

    #WIND AND SEISMIC LOADS
    wind_load : load_data
    seismic_dbe : load_data
    seismic_mce : load_data

    