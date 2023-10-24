class load_data:
    moment = 1.0
    shear = 1.0
    moment_factor = 1.0
    shear_factor = 1.0

class vessel_load : 
    #VESSEL LOADS
    erection_load = load_data()
    operating_load = load_data()
    testing_load = load_data()

    #WIND AND SEISMIC LOADS
    wind_load = load_data()
    seismic_dbe = load_data()
    seismic_mce = load_data()


    