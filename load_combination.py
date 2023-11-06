from load import load_data 

class factored_load :
    factor = 1.0
    load = load_data()

    def __init__(self,factor=1.0,load=load_data(1,1,1,1)):
        self.factor = factor
        load = load_data

class load_combination : 
    load_ID : str
    loads : []       #FACTORED LOADS ARRAY
    factored_loads_total : load_data
    sbc_increase :float
    reinforcement_factor :float
    factor_of_safety_sliding :float
    factor_of_safety_overturning :float

    def __init__(self,load_ID="1",loads=[],sbc_increase=1.0,reinforcement_factor=1.0,factor_of_safety_sliding=1.0,factor_of_safety_overturning = 1.0):
        self.load_ID = load_ID
        self.loads = loads
        self.sbc_increase =sbc_increase
        self.reinforcement_factor = reinforcement_factor
        self.factor_of_safety_overturning = factor_of_safety_overturning
        self.factor_of_safety_sliding = factor_of_safety_sliding

    def calculate_total_load(self):
        self.factored_loads_total = load_data(0,0,0,1,1,1)
        for i in range(len(self.loads)) :
            load_i : factored_load = self.loads[i]
            self.factored_loads_total.axial += load_i.factor * load_i.load.axial
            self.factored_loads_total.shear += load_i.factor * load_i.load.shear
            self.factored_loads_total.moment += load_i.factor * load_i.load.moment



