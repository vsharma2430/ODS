import math
import numpy 
from object_threeD import shape_octagon
import matplotlib.pyplot as plt

def calculate_length_of_strips(shape:str,side:float,discrete_unit:int):
    length_res = []
    root_2 = math.sqrt(2)
    
    if(shape == "octagon"):
        side_dicrete = int(round(discrete_unit / shape_octagon.side_diagonal_factor,0))
        x_limit = int(round(discrete_unit / shape_octagon.side_diagonal_factor / root_2,0))
        diagonal = side * shape_octagon.side_diagonal_factor

        print(side_dicrete)
        print(x_limit)
        print(diagonal)

        for i in range(0,x_limit):
            length_res.append(side +  i / x_limit * side * root_2)

        for i in range(x_limit,side_dicrete+x_limit):
            length_res.append(diagonal)

        for i in range(side_dicrete+x_limit,discrete_unit):
            length_res.append(diagonal - ( i - (side_dicrete+x_limit) )/ x_limit * side * root_2)

    return length_res

def calculate_pressure_in_strips(pmax:float,pmin:float,k:float,discrete_unit:int):
    pressure_res = []
    if(round(k,3)!=0):
        pmin = 0

    pressure_strips = int((1-k)*discrete_unit)
    pressure_slope = (pmax - pmin)/(pressure_strips)

    for i in range(0,pressure_strips):
        pressure_i = pmax - pressure_slope * i
        pressure_res.append(pressure_i)
    for i in range(pressure_strips,discrete_unit):
        pressure_res.append(0)

    return pressure_res

#calculate_pressure_in_strips(100,90,0.3,1000)
#calculate_length_of_strips("octagon",1,1000)