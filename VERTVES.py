#library imports
import math
import os
import markdown2

#custom imports
from base import *

report_file = "Report/vertes_report.html"
report_html = open(report_file, "w")
report_html_list = ["<html><head><link rel=\"stylesheet\" href=\"style.css\"></head><body>"]

pedestal_side = 0.7
foundation_side = 0.9
cover = cover_thickness(0.05,0.075,0.05)

pedestal = object_3d("octagon",pedestal_side)
foundation = object_3d("octagon",foundation_side)

pedestal.material = concrete
pedestal.top_elevation = 4.0
pedestal.bottom_elevation = 2.5
pedestal.water_elevation = 0.5

foundation.material = concrete
foundation.top_elevation = pedestal.bottom_elevation
foundation.bottom_elevation = 0
foundation.water_elevation = 0.5

equipment = equipment()
openFoundation = open_foundation(pedestal,foundation,cover)
surroundings = surroundings(3,2.5,0.5)

sbc_net = soil.property.soil_capacity
weight_of_footing = openFoundation.foundation.weight()
weight_of_pedestal = openFoundation.pedestal.weight()

foundation_area:float = openFoundation.foundation.shape_object.area()
pedestal_area:float = openFoundation.pedestal.shape_object.area()
soil_area = max(foundation_area - pedestal_area,0)
foundation_section_modulus_major = openFoundation.foundation.shape_object.section_modulus_major()
foundation_section_modulus_minor = openFoundation.foundation.shape_object.section_modulus_minor()

soil_height = max(surroundings.natural_ground_level - openFoundation.foundation.bottom_elevation,0)
weight_of_soil = soil_area * soil_height * soil.density 
shear_lever = openFoundation.pedestal.top_elevation - openFoundation.foundation.bottom_elevation
weight_total = weight_of_soil + weight_of_footing + weight_of_pedestal
foundation_diameter = openFoundation.foundation.shape_object.side * shape_octagon.side_diameter_factor
foundation_diagonal = openFoundation.foundation.shape_object.side * shape_octagon.side_diagonal_factor

report_html_list.append(markdown2.markdown("#**VERTVES REPORT**"))
report_html_list.append(markdown2.markdown("##INPUT"))

report_html_list.append(markdown2.markdown("###SITE"))
report_html_list.extend(surroundings.properties_report())

report_html_list.append(markdown2.markdown("###GEOMETRY"))

report_html_list.append(markdown2.markdown("####PEDESTAL"))
report_html_list.extend(openFoundation.pedestal.properties_report())

report_html_list.append(markdown2.markdown("####FOUNDATION"))
report_html_list.extend(openFoundation.foundation.properties_report())

report_html_list.append(markdown2.markdown("#####COVER"))
report_html_list.extend(openFoundation.foundation_cover.properties_report())

report_html_list.append(markdown2.markdown("####SOIL"))
report_soil = []
width_table = [300,200]
report_soil.append("| Property | Value |")
report_soil.append("|:---|:---:|")
report_soil.append("".join(map(lambda wid: "|<img width=" + str(wid) + "/>", width_table)) + "|")
report_soil.append("| SBC (net) | " + roundOff(sbc_net)+ "|")
report_soil.append("| Top Elevation | " + roundOff(surroundings.natural_ground_level)+ "|")
report_soil.append("| Bottom Elevation | " + roundOff(openFoundation.foundation.bottom_elevation)+ "|")
report_soil.append("| Length | " + roundOff(surroundings.natural_ground_level - openFoundation.foundation.bottom_elevation)+ "|")
report_soil.append("| Density | " + roundOff(soil.density)+ "|")
report_soil.append("| Area | " + roundOff(soil_area)+ "|")
report_soil.append("| Weight | " + roundOff(weight_of_soil)+ "|")
report_html_list.append(markdown2.markdown(text="\n".join(report_soil), extras=["tables"]))

report_html_list.append(markdown2.markdown("####CALCULATED VALUES"))
report_total = []
width_table = [300,200]
report_total.append("| Property | Value |")
report_total.append("|:---|:---:|")
report_total.append("".join(map(lambda wid: "|<img width=" + str(wid) + "/>", width_table)) + "|")
report_total.append("| Total Weight | " + roundOff(weight_total)+ "|")
report_total.append("| Shear Lever | " + roundOff(shear_lever)+ "|")
report_html_list.append(markdown2.markdown(text="\n".join(report_total), extras=["tables"]))

#BASIC LOADS
vessel_load = vessel_load()
vessel_load.empty_load = load_data("Vessel : Empty",tonneToN(3),tonneToN(0),0)
vessel_load.erection_load = load_data("Vessel : Erection",tonneToN(3.5),tonneToN(0),0)
vessel_load.operating_load = load_data("Vessel : Operating",tonneToN(4.2),tonneToN(0),0)
vessel_load.testing_load = load_data("Vessel : Testing",tonneToN(3.2),tonneToN(0),0)
vessel_load.wind_load = load_data("Wind : Wind",tonneToN(0),tonneToN(0.5),tonneToN(4))
vessel_load.seismic_dbe = load_data("Seismic : DBE",tonneToN(0),tonneToN(0.7),tonneToN(5))
vessel_load.seismic_mce = load_data("Seismic : MCE",tonneToN(0),tonneToN(1.2),tonneToN(8))

report_html_list.append(markdown2.markdown("###LOADS"))
report_html_list.extend(vessel_load.report())

inbuilt_factored_loads_1 = []
inbuilt_factored_loads_1.append(factored_load(1, vessel_load.empty_load))
inbuilt_load_combination_1 = load_combination(load_ID="1001",loads=inbuilt_factored_loads_1,sbc_increase=0,reinforcement_factor=1.5,factor_of_safety_overturning=1.5,factor_of_safety_sliding=2.0)

inbuilt_factored_loads_2 = []
inbuilt_factored_loads_2.append(factored_load(1,vessel_load.empty_load))
inbuilt_factored_loads_2.append(factored_load(1,vessel_load.wind_load))
inbuilt_load_combination_2 = load_combination(load_ID="1002",loads=inbuilt_factored_loads_2,sbc_increase=0.5,reinforcement_factor=1.5,factor_of_safety_overturning=1.5,factor_of_safety_sliding=2.0)

inbuilt_factored_loads_3 = []
inbuilt_factored_loads_3.append(factored_load(1,vessel_load.operating_load))
inbuilt_load_combination_3 = load_combination(load_ID="1003",loads=inbuilt_factored_loads_3,sbc_increase=0,reinforcement_factor=1.5,factor_of_safety_overturning=1.5,factor_of_safety_sliding=2.0)

inbuilt_factored_loads_4 = []
inbuilt_factored_loads_4.append(factored_load(1,vessel_load.operating_load))
inbuilt_factored_loads_4.append(factored_load(1,vessel_load.wind_load))
inbuilt_load_combination_4 = load_combination(load_ID="1004",loads=inbuilt_factored_loads_4,sbc_increase=0.5,reinforcement_factor=1.5,factor_of_safety_overturning=1.5,factor_of_safety_sliding=2.0)

inbuilt_factored_loads_5 = []
inbuilt_factored_loads_5.append(factored_load(1,vessel_load.operating_load))
inbuilt_factored_loads_5.append(factored_load(1,vessel_load.seismic_dbe))
inbuilt_load_combination_5 = load_combination(load_ID="1005",loads=inbuilt_factored_loads_5,sbc_increase=0.5,reinforcement_factor=1.5,factor_of_safety_overturning=1.5,factor_of_safety_sliding=2.0)

inbuilt_factored_loads_6 = []
inbuilt_factored_loads_6.append(factored_load(1,vessel_load.operating_load))
inbuilt_factored_loads_6.append(factored_load(1,vessel_load.seismic_mce))
inbuilt_load_combination_6 = load_combination(load_ID="1006",loads=inbuilt_factored_loads_6,sbc_increase=1,reinforcement_factor=1.5,factor_of_safety_overturning=1.0,factor_of_safety_sliding=1.0)

inbuilt_factored_loads_7 = []
inbuilt_factored_loads_7.append(factored_load(1,vessel_load.operating_load))
inbuilt_factored_loads_7.append(factored_load(0.25,vessel_load.wind_load))
inbuilt_load_combination_7 = load_combination(load_ID="1007",loads=inbuilt_factored_loads_7,sbc_increase=0,reinforcement_factor=1.5,factor_of_safety_overturning=1.5,factor_of_safety_sliding=2.0)

inbuilt_load_combinations = []
inbuilt_load_combinations.append(inbuilt_load_combination_1)
inbuilt_load_combinations.append(inbuilt_load_combination_2)
inbuilt_load_combinations.append(inbuilt_load_combination_3)
inbuilt_load_combinations.append(inbuilt_load_combination_4)
inbuilt_load_combinations.append(inbuilt_load_combination_5)
inbuilt_load_combinations.append(inbuilt_load_combination_6)
inbuilt_load_combinations.append(inbuilt_load_combination_7)

report_html_list.append(markdown2.markdown("###LOAD COMBINATIONS AND CALCULATIONS"))
report_lc_list = []
width_table = [50,300,100,100,100,100,100,100,100]
report_lc_list.append("| Load ID | Loads | Axial | Shear | Moment | SBC Increase| R/F Factor | FOSO | FOSS |")
report_lc_list.append("".join(map(lambda wid: "|:---:", width_table))+"|")
report_lc_list.append("".join(map(lambda wid: "|<img width=" + str(wid) + "/>", width_table))+"|")
for inbuilt_combination_x in inbuilt_load_combinations : 
    inbuilt_combination_x.calculate_total_load()
    report_lc_list.extend(inbuilt_combination_x.property())
report_html_list.extend(markdown2.markdown(text="\n".join(report_lc_list), extras=["tables"]))

print_octagon_diameter_nomograph()
print_octagon_diagonal_nomograph()

report_html_list.append(markdown2.markdown("##NOMOGRAPHS"))
report_html_list.append(markdown2.markdown("###DIAMETER"))
report_html_list.append(markdown2.markdown("![Nomograph](nomograph_diameter.png)"))
report_html_list.append(markdown2.markdown("###DIAGONAL"))
report_html_list.append(markdown2.markdown("![Nomograph](nomograph_diagonal.png)"))

#FOOTING SIZE CHECK _ DIAMETER OF THE FOOTING USED
report_html_list.append(markdown2.markdown("##OUTPUT"))
report_html_list.append(markdown2.markdown("###FOOTING SIZE CHECK"))

report_html_list_i_1 = []
report_html_list_i_1.append("| Load ID | Axial | Shear | Moment | E/D | L | k | PMax | PMin | SBC Gross | FOS(Overturning) | FOS(Sliding) | Contact Area | Overall |" )
width_table = [100,75,75,75,75,75,75,75,75,75,125,125,75,75]
report_html_list_i_1.append("".join(map(lambda wid: "|:---:", width_table)) + "|") 
report_html_list_i_1.append("".join(map(lambda wid: "|<img width=" + str(wid) + "/>", width_table)) + "|") 

for i in range(len(inbuilt_load_combinations)): 

    inbuilt_load_combinations_i : load_combination = inbuilt_load_combinations[i] 
    sbc_gross_i = calculate_sbc_gross(sbc_net,surroundings.natural_ground_level,openFoundation.foundation.bottom_elevation,surroundings.water_level,soil.density,soil.sub_water_density,inbuilt_load_combinations_i.sbc_increase)
    axial_i = inbuilt_load_combinations_i.factored_loads_total.axial + weight_total
    shear_i = inbuilt_load_combinations_i.factored_loads_total.shear
    moment_i = inbuilt_load_combinations_i.factored_loads_total.moment + abs(shear_i * shear_lever)
    eccentricity_i = moment_i/axial_i
    e_dividedBy_D_i = eccentricity_i/foundation_diagonal    #DOUBT:PIP SAYS USE DIAGONAL

    L_i,k_i,within_nomograph = nomomgraph_value_octagon_diameter(e_dividedBy_D_i)
    pmax_i = axial_i / foundation_area + moment_i / foundation_section_modulus_major
    pmin_i = axial_i / foundation_area - moment_i / foundation_section_modulus_major

    if(pmin_i<0):
        pmax_i = L_i * axial_i / foundation_area
        pmin_i = 0

    sbc_check = False
    if(sbc_gross_i > pmax_i and sbc_gross_i > pmin_i) :
        sbc_check = True

    FOSS_i : float
    FOSO_i : float
    if(shear_i > 0):
        FOSS_i = axial_i * soil.property.coeff_friction / shear_i
    else :
        FOSS_i = 10000

    if(moment_i > 0):
        FOSO_i = axial_i * foundation_diameter / 2 / moment_i
    else :
        FOSO_i = 10000

    FOSO_i_check = False
    FOSS_i_check = False
    if(FOSO_i > inbuilt_load_combinations_i.factor_of_safety_overturning) :
        FOSO_i_check = True
    if(FOSS_i > inbuilt_load_combinations_i.factor_of_safety_sliding) :
        FOSS_i_check = True

    contact_area_check = False  
    if(k_i<shape_octagon.diagonal_diameter_factor/2):
        contact_area_check = True

    # CHECKS IMPLEMENTED
    # WITHIN NOMOGRAPH CHECK, FOSS CHECK, FOSO CHECK , CONTACT AREA CHECK
    # TO BE IMPLEMENTED : NO TENSION CHECK

    overall_i_check = False
    if(within_nomograph and FOSO_i_check and FOSS_i_check and contact_area_check and sbc_check) :
        overall_i_check = True

    report_html_list_i_1.append( "|" + inbuilt_load_combinations_i.load_ID + \
                               "|" + roundOff(axial_i) + " |" + roundOff(shear_i) + " |" + roundOff(moment_i) + \
                               "|" + roundOff(e_dividedBy_D_i) + "|" + roundOff(L_i) + "|" + roundOff(k_i) + \
                               "|" + roundOff(pmax_i) + "|" + roundOff(pmin_i) + \
                               "|" + roundOff(sbc_gross_i) + pass_fail(sbc_check)  +\
                               "|" + roundOff(FOSO_i) + pass_fail(FOSO_i_check) + \
                               "|" + roundOff(FOSS_i) + pass_fail(FOSS_i_check) + \
                               "|" + pass_fail(contact_area_check) + \
                               "|" + pass_fail(overall_i_check) + " |")

report_html_list.append(markdown2.markdown(text="\n".join(report_html_list_i_1), extras=["tables"]))

#MOMENT RF CHECK _ DIAGONAL OF THE SHAPE USED
report_html_list.append(markdown2.markdown("###MOMENT R/F CHECK"))
discrete_pixel = 1024*10
equivalent_square_pedestal_side = math.sqrt(pedestal_area)
soil_pressure = weight_of_soil / (soil_area)
self_weight_pressure = weight_of_footing / (foundation_area)
length_of_strips = calculate_length_of_strips(openFoundation.foundation.shape_name,foundation_side,discrete_pixel)

xubyD = calculate_xu_byD(steel.property.fy)
fsc_flexure = calculate_fsc_flexure(steel.property.fy)
rf_depth_bottom = (openFoundation.foundation.top_elevation - openFoundation.foundation.bottom_elevation) - openFoundation.foundation_cover.top_cover
rf_depth_top = (openFoundation.foundation.top_elevation - openFoundation.foundation.bottom_elevation) - openFoundation.foundation_cover.bottom_cover
rf_width = foundation_diagonal - 2 * openFoundation.foundation_cover.side_cover
muLim_top = calculate_mu_lim(xubyD,rf_width,rf_depth_top,concrete.property.fck,steel.property.fy)
muLim_bottom = calculate_mu_lim(xubyD,rf_width,rf_depth_bottom,concrete.property.fck,steel.property.fy)
reinforcement_minimum = reinforcement(perecentageRF=(calculate_min_rf(steel.property.fy)))
reinforcement_maximum = reinforcement(perecentageRF=4)

report_html_list.append(markdown2.markdown("#####CALCULATED VALUES"))
report_html_list_i_1 = []
report_html_list_i_1.append("| Property | Value |" )
width_table = [300,200]
report_html_list_i_1.append("".join(map(lambda wid: "|:---:", width_table)) + "|") 
report_html_list_i_1.append("".join(map(lambda wid: "|<img width=" + str(wid) + "/>", width_table)) + "|") 
report_html_list_i_1.append( "| Equivalent Pedestal Square |" + roundOff(equivalent_square_pedestal_side)+ "|") 
report_html_list_i_1.append( "| Self Weight Pressure |" + roundOff(self_weight_pressure)+ "|") 
report_html_list_i_1.append( "| Soil Pressure |" + roundOff(soil_pressure)+ "|") 
report_html_list_i_1.append( "| (x<sub>u</sub>/D)<sub>limit</sub> |" + roundOff(xubyD)+ "|") 
report_html_list_i_1.append( "| RF Depth<sub>bottom</sub> |" + roundOff(rf_depth_bottom)+ "|") 
report_html_list_i_1.append( "| RF Depth<sub>top</sub> |" + roundOff(rf_depth_top)+ "|") 
report_html_list_i_1.append( "| RF Width |" + roundOff(rf_width)+ "|") 
report_html_list_i_1.append( "| f<sub>y</sub> |" + roundOff(steel.property.fy)+ "|") 
report_html_list_i_1.append( "| (f<sub>sc</sub>)<sub>flexure</sub> |" + roundOff(fsc_flexure)+ "|") 
report_html_list_i_1.append( "| (M<sub>uLim</sub>)<sub>bottom</sub> |" + roundOff(muLim_bottom)+ "|") 
report_html_list_i_1.append( "| M<sub>uLim</sub><sub>top</sub>|" + roundOff(muLim_top)+ "|") 
report_html_list_i_1.append( "| RF<sub>min</sub>(%)|" + roundOff(reinforcement_minimum.percentageRF)+ "|") 
report_html_list_i_1.append( "| RF<sub>max</sub>(%)|" + roundOff(reinforcement_maximum.percentageRF)+ "|") 
report_html_list.append(markdown2.markdown(text="\n".join(report_html_list_i_1), extras=["tables"]))

report_html_list.append(markdown2.markdown("#####R/F VALUES"))
report_html_list_i_1 = []
report_html_list_i_1.append("| Load ID | Axial | Shear | Moment | E/D | L | k | PMax | PMin | Moment 1 | Moment 2| R/F<sub>bottom</sub> | R/F<sub>top</sub> |" )
width_table = [100,75,75,75,75,75,75,75,75,125,125,100,100]
report_html_list_i_1.append("".join(map(lambda wid: "|:---:", width_table)) + "|") 
report_html_list_i_1.append("".join(map(lambda wid: "|<img width=" + str(wid) + "/>", width_table)) + "|") 

for i in range(len(inbuilt_load_combinations)): 
    inbuilt_load_combinations_i : load_combination = inbuilt_load_combinations[i] 
    axial_i = inbuilt_load_combinations_i.factored_loads_total.axial + weight_total
    shear_i = inbuilt_load_combinations_i.factored_loads_total.shear
    moment_i = inbuilt_load_combinations_i.factored_loads_total.moment + abs(shear_i * shear_lever)
    eccentricity_i = moment_i/axial_i
    e_dividedBy_D_i = eccentricity_i/foundation_diagonal
    L_i,k_i,within_nomograph = nomomgraph_value_octagon_diagonal(e_dividedBy_D_i)
    pmax_i = axial_i / foundation_area + moment_i / foundation_section_modulus_minor
    pmin_i = axial_i / foundation_area - moment_i / foundation_section_modulus_minor

    if(pmin_i<0):
        pmax_i = L_i * axial_i / foundation_area
        pmin_i = 0

    pressure_strip = calculate_pressure_in_strips(pmax_i,pmin_i,self_weight_pressure,soil_pressure,k_i,discrete_pixel)
    moments_i = calculate_moment_face(equivalent_square_pedestal_side,foundation_diameter,pressure_strip,length_of_strips,discrete_pixel)
    
    if(moments_i[1]>0 and moments_i[0]>0):
        design_moment = max(moments_i)
        main_rf = calculate_rf_single(design_moment*1000,inbuilt_load_combinations_i.reinforcement_factor,rf_width,rf_depth_bottom,concrete.property.fck,steel.property.fy)
    else:
        continue
                
    report_html_list_i_1.append( "|" + inbuilt_load_combinations_i.load_ID + \
                                 "|" + roundOff(axial_i) + " |" + roundOff(shear_i) + " |" + roundOff(moment_i) + \
                                 "|" + roundOff(e_dividedBy_D_i) + "|" + roundOff(L_i) + "|" + roundOff(k_i) + \
                                 "|" + roundOff(pmax_i) + "|" + roundOff(pmin_i) + \
                                 "|" + roundOff(float(moments_i[0])) + " |" + roundOff(float(moments_i[1]))+ \
                                 "|" + str(round(main_rf,3)) + " |" + roundOff(0) + "|")

    
    #CALCULATE FACE LOCATIONS IN PIXELS AND CALCULATE MOMENT

report_html_list.append(markdown2.markdown(text="\n".join(report_html_list_i_1), extras=["tables"]))

report_html_list.append("</html></body>")
report_html.writelines(report_html_list)
report_html.close()

open(report_file)