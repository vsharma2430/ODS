from load import load_data 

class factored_load :
    factor = 1.0
    load = load_data()

    def __init__(self,factor=1.0,load=load_data(1,1,1,1)):
        self.factor = factor
        load = load_data

class load_combination : 
    load_ID = ""
    loads = []  #FACTORED LOADS ARRAY
    sbc_increase = 1.0
    reinforcement_factor = 1.0
    factor_of_safety_sliding = 1.0
    factor_of_safety_overturning = 1.0

    def __init__(self,load_ID="1",loads=[],sbc_increase=1.0,reinforcement_factor=1.0,factor_of_safety_sliding=1.0,factor_of_safety_overturning = 1.0):
        self.load_ID = load_ID
        self.loads = loads
        self.sbc_increase =sbc_increase
        self.reinforcement_factor = reinforcement_factor
        self.factor_of_safety_overturning = factor_of_safety_overturning
        self.factor_of_safety_sliding = factor_of_safety_sliding

