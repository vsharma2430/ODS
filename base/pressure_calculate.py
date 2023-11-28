import math
import matplotlib.pyplot as plt
from .object_threeD import shape_octagon
from .misc import compare_value_delta,value_delta,PaToMPa,Mtomm
valA = 101.97162129779

def calculate_length_of_strips(shape:str,side:float,discrete_unit:int):
    length_res = []
    root_2 = math.sqrt(2)
    
    if(shape == "octagon"):
        side_dicrete = int(round(discrete_unit / shape_octagon.side_diagonal_factor,0))
        x_limit = int(round(discrete_unit / shape_octagon.side_diagonal_factor / root_2,0))
        diagonal = side * shape_octagon.side_diagonal_factor

        for i in range(0,x_limit):
            length_res.append(side +  i / x_limit * side * root_2)

        for i in range(x_limit,side_dicrete+x_limit):
            length_res.append(diagonal)

        for i in range(side_dicrete+x_limit,discrete_unit):
            length_res.append(diagonal - ( i - (side_dicrete+x_limit) )/ x_limit * side * root_2)

    return length_res

def calculate_pressure_in_strips(pmax:float,pmin:float,swp:float,sp:float,k:float,discrete_unit:int):
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

    #for i in range(0,discrete_unit):
    pressure_res=list(map(lambda x : x-swp-sp,pressure_res))

    return pressure_res

def calculate_moment_face(equivalent_pedestal_square_size:float, footing_diagonal:float,pressure:[],length:[],discrete_unit:int):
    discrete_size = footing_diagonal / discrete_unit
    location1 = int((footing_diagonal - equivalent_pedestal_square_size)/2/footing_diagonal * discrete_unit)
    location2 = int(((footing_diagonal - equivalent_pedestal_square_size)/2+equivalent_pedestal_square_size)/footing_diagonal * discrete_unit)
    lever_arm_1 = []
    lever_arm_2 = []
    
    for i in range(0,discrete_unit):
        lever_arm_1.append( (abs(i-location1))/discrete_unit*footing_diagonal)
        lever_arm_2.append( (abs(i-location2))/discrete_unit*footing_diagonal)

    moment_array_1 = []
    moment_1 = 0
    moment_2 = 0
    for i in range(0, location1) : 
        moment_i = calculate_moment(length[i]*discrete_size,pressure[i],lever_arm_1[i]) 
        moment_array_1.append(moment_i)
        moment_1 = moment_1 + moment_i

    moment_array_2 = []
    for i in range(location2, discrete_unit) : 
        moment_i = calculate_moment(length[i]*discrete_size,pressure[i],lever_arm_2[i]) 
        moment_array_2.append(moment_i)
        moment_2 = moment_2 + moment_i
    return [moment_1,moment_2]

def calculate_shear_dby2(equivalent_pedestal_square_size:float, footing_diagonal:float,footing_depth:float,pressure:[],length:[],discrete_unit:int):
    discrete_size = footing_diagonal / discrete_unit
    location1 = int(((footing_diagonal - equivalent_pedestal_square_size/2)/2 - (footing_depth/2) )/footing_diagonal * discrete_unit)
    location2 = int((((footing_diagonal - equivalent_pedestal_square_size)/2)+equivalent_pedestal_square_size+(footing_depth/2))/footing_diagonal * discrete_unit)

    shear_array_1 = []
    shear_1 = 0
    shear_2 = 0
    for i in range(0, location1) : 
        shear_i = calculate_shear(length[i]*discrete_size,pressure[i]) 
        shear_array_1.append(shear_i)
        shear_1 = shear_1 + shear_i

    shear_array_2 = []
    for i in range(location2, discrete_unit) : 
        shear_i = calculate_shear(length[i]*discrete_size,pressure[i]) 
        shear_array_2.append(shear_i)
        shear_2 = shear_2 + shear_i

    return [shear_1,shear_2];                                       

def calculate_moment(area,pressure,lever): 
    return area*pressure*lever

def calculate_shear(area,pressure): 
    return area*pressure

def calculate_xu_byD(fy:float):
    fy_compare = PaToMPa(fy)
    if(compare_value_delta(fy_compare,250,value_delta)):
        return 0.53
    elif(compare_value_delta(fy_compare,415,value_delta)):
        return 0.48
    elif(compare_value_delta(fy_compare,500,value_delta)):
        return 0.46
    else:
        return 0.46

def calculate_fsc_flexure(fy:float):
    fy_compare = PaToMPa(fy)
    if(compare_value_delta(fy_compare,250,value_delta)):
        return 0.87*fy
    elif(compare_value_delta(fy_compare,415,value_delta)):
        return 0.79*fy
    elif(compare_value_delta(fy_compare,500,value_delta)):
        return 0.746*fy
    else:
        return 0.746*fy
    
def calculate_Z(designMoment:float,rfdesignFactor:float,rf_width:float,rf_depth:float):
    return designMoment * rfdesignFactor / (rf_width * rf_depth * rf_depth)

def calculate_add_double_pt_primary(moment:float,fy:float,depth:float):
    return moment / (0.87 * fy * valA * depth )
 
def calculate_add_double_pt_secondary(add_double_primary:float,fy:float,fsc_flexure:float):
    return 0.87 * fy * valA * add_double_primary / (fsc_flexure * valA - 0.447 * fy * valA)
        
def calculate_mu_lim(xubyd:float,rf_width:float,rf_depth:float,fck:float,fy:float):
    xu_lim = xubyd*rf_depth
    return 0.362 * fck * rf_width * xu_lim * (rf_depth-0.42*xu_lim)/1000

def calculate_min_rf(fy:float):
    fy_compare = PaToMPa(fy)
    if(compare_value_delta(fy_compare,500,value_delta)):
        return 0.12
    else:
        return 0.15

def calculate_rf(design_moment:float,rf_factor:float,rf_width:float,rf_depth:float,fck:float,fy:float):
    fck = PaToMPa(fck)
    fy = PaToMPa(fy)
    rf_width = Mtomm(rf_width)
    rf_depth = Mtomm(rf_depth)
    print(design_moment)
    var1 = 1 - 4.6 * design_moment / ( fck* rf_width * rf_depth * rf_depth)
    print(var1)
    
    if var1>0:
        var2 = 1- math.sqrt(var1)
        return 0.5*fck/fy*var2
    
    return [0,0]

def calculate_rf_single(design_moment:float,rf_factor:float,rf_width:float,rf_depth:float,fck:float,fy:float):
    main_rf_arr = calculate_rf(design_moment,rf_factor,rf_width,rf_depth,fck,fy)
    return main_rf_arr

def calculate_rf_double(design_moment:float,limit_moment:float,rf_factor:float,rf_width:float,rf_depth:float,fck:float,fy:float,fsc_flexure:float):
    main_rf_arr = calculate_rf(limit_moment,rf_factor,rf_width,rf_depth,fck,fy)
    add_double_pt_1 = calculate_add_double_pt_primary(design_moment-limit_moment,fy,rf_depth)
    add_double_pt_2 = calculate_add_double_pt_secondary(add_double_pt_1,fy,fsc_flexure)
    
    main_rf = main_rf_arr[0]+add_double_pt_1
    secondary_rf = add_double_pt_2
    
    return [main_rf,secondary_rf,main_rf_arr[0],add_double_pt_1,add_double_pt_2]


#print(calculate_moment_face(1,2,calculate_pressure_in_strips(100,0,0,1024),calculate_length_of_strips("octagon",2/shape_octagon.side_diagonal_factor,1024),1024))
#print(calculate_shear_dby2(1,2,0.5,calculate_pressure_in_strips(100,0,0,1024),calculate_length_of_strips("octagon",2/shape_octagon.side_diagonal_factor,1024),1024))
#calculate_pressure_in_strips(100,90,0.3,1000)
#calculate_length_of_strips("octagon",1,1000)