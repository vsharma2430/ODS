from load import load_data 

class factored_load :
    factor = 1.0
    load = load_data()

class load_combination : 
    load_ID = ""
    loads = []
    sbc_increase = 1.0
    reinforcement_factor = 1.0
    factor_of_safety_sliding = 1.0
    factor_of_safety_overturning = 1.0