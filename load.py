class load_data:
    axial : float
    moment : float
    shear : float
    axial_factor : float
    moment_factor : float
    shear_factor : float

    def __init__(self,axial=1.0,moment=1.0,shear=1.0,axial_factor=1.0,moment_factor = 1.0,shear_factor=1.0):
        self.axial = axial
        self.moment = moment
        self.shear = shear
        self.axial_factor = axial_factor
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

    