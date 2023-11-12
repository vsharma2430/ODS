from object_threeD import object_3d
from material import concrete
from misc import roundOff
import markdown2

# FOUNDATION CONFIGURATION 
# 1. PEDESTAL
# 2. FOUNDATION
# 3. PILES

# SURROUNDINGS CONFIG
# 1. GROUND (HPP AND NGL)
# 2. WATER LEVEL 

class surroundings :
    highest_pavement_point : float
    natural_ground_level : float
    water_level : float

    def __init__(self,highest_pavement_point,natural_ground_level,water_level):
        self.highest_pavement_point = highest_pavement_point
        self.natural_ground_level = natural_ground_level
        self.water_level = water_level

    def properties_report(self):
        report_html_list = []
        width_table = [300,200]
        report_html_list.append("| Property | Value |")
        report_html_list.append("|:---|:---:|")
        report_html_list.append("".join(map(lambda wid: "|<img width=" + str(wid) + "/>", width_table)))
        report_html_list.append("| HPP | " + roundOff(self.highest_pavement_point) + "|")
        report_html_list.append("| NGL | " + roundOff(self.natural_ground_level) + "|")
        report_html_list.append("| Water Level | " + roundOff(self.water_level) + "|")
        return markdown2.markdown(text="\n".join(report_html_list), extras=["tables"])

class cover_thickness : 
    top_cover:float
    bottom_cover:float
    side_cover:float

    def __init__(self,top_cover,bottom_cover,side_cover):
        self.top_cover = top_cover
        self.bottom_cover = bottom_cover
        self.side_cover = side_cover

    def properties_report(self):
        report_html_list = []
        width_table = [300,200]
        report_html_list.append("| Property | Value |")
        report_html_list.append("|:---|:---:|")
        report_html_list.append("".join(map(lambda wid: "|<img width=" + str(wid) + "/>", width_table)))
        report_html_list.append("| Top Cover | " + roundOff(self.top_cover) + "|")
        report_html_list.append("| Bottom Cover | " + roundOff(self.bottom_cover) + "|")
        report_html_list.append("| Side Cover | " + roundOff(self.side_cover) + "|")
        return markdown2.markdown(text="\n".join(report_html_list), extras=["tables"])

class open_foundation : 
    pedestal : object_3d
    foundation : object_3d
    foundation_cover : cover_thickness

    def __init__(self,pedestal,foundation,cover):
        self.pedestal = pedestal
        self.foundation = foundation
        self.foundation_cover = cover