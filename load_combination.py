from load import load_data
import markdown2
from misc import roundOff

class factored_load :
    factor : float
    load : load_data

    def __init__(self,factor:float,load:load_data):
        self.factor = factor
        self.load = load
    
    def property(self):
        print(roundOff(self.factor) + " " + self.load.print())

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
        self.sbc_increase = sbc_increase
        self.reinforcement_factor = reinforcement_factor
        self.factor_of_safety_overturning = factor_of_safety_overturning
        self.factor_of_safety_sliding = factor_of_safety_sliding

    def calculate_total_load(self):
        self.factored_loads_total = load_data("total",0,0,0)

        for i in range(len(self.loads)) :
            load_i = self.loads[i]
            self.factored_loads_total.axial += load_i.factor * load_i.load.axial
            self.factored_loads_total.shear += load_i.factor * load_i.load.shear
            self.factored_loads_total.moment += load_i.factor * load_i.load.moment

    def property(self):
        report_html_list = []
        loads_str : str = " + ".join(map(lambda lx : roundOff(lx.factor) + " * (" + str(lx.load.name) +")" , self.loads))
        report_html_list.append("|"+ self.load_ID + "|" + loads_str  + "|" + roundOff(self.factored_loads_total.axial) + "|" + roundOff(self.factored_loads_total.shear) + "|" + roundOff(self.factored_loads_total.moment) + "|" + roundOff(self.sbc_increase) + "|" + roundOff(self.reinforcement_factor) + "|" + roundOff(self.factor_of_safety_overturning) + "|" + roundOff(self.factor_of_safety_sliding) + "|")
        return report_html_list


       


