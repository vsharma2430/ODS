import markdown2
from .misc import roundOff

class load_data:
    name : str
    axial : float
    moment : float
    shear : float
    axial_factor : float
    moment_factor : float
    shear_factor : float

    def __init__(self,name="load",axial=1.0,shear=1.0,moment=1.0,axial_factor=1.0,moment_factor = 1.0,shear_factor=1.0):
        self.name = name
        self.axial = axial
        self.shear = shear
        self.moment = moment
        self.axial_factor = axial_factor
        self.moment_factor = moment_factor
        self.shear_factor = shear_factor

    def report(self):
        report_html_list = []
        width_table = [150,250,100]
        report_html_list.append("| Type | Value | Factor")
        report_html_list.append("|:---|:---:|:---:|")
        report_html_list.append("".join(map(lambda wid: "|<img width=" + str(wid) + "/>", width_table)))
        report_html_list.append("| Name | " + self.name + "| |")
        report_html_list.append("| Axial | " + roundOff(self.axial) + "|" + roundOff(self.axial_factor) + "|")
        report_html_list.append("| Shear | " + roundOff(self.shear) + "|" + roundOff(self.shear_factor) + "|")
        report_html_list.append("| Moment | " + roundOff(self.moment) + "|" + roundOff(self.moment_factor) + "|")
        return markdown2.markdown(text="\n".join(report_html_list), extras=["tables"])
    
    def print(self):
        return roundOff(self.axial) + " " + roundOff(self.shear) + " " + roundOff(self.moment)
    

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

    def report(self):
        report_html_list = []
        report_html_list.append(markdown2.markdown("####EMPTY LOAD"))
        report_html_list.extend(self.empty_load.report())

        report_html_list.append(markdown2.markdown("####ERECTION LOAD"))
        report_html_list.extend(self.erection_load.report())

        report_html_list.append(markdown2.markdown("####OPERATING LOAD"))
        report_html_list.extend(self.operating_load.report())

        report_html_list.append(markdown2.markdown("####TESTING LOAD"))
        report_html_list.extend(self.testing_load.report())

        report_html_list.append(markdown2.markdown("####WIND LOAD"))
        report_html_list.extend(self.wind_load.report())

        report_html_list.append(markdown2.markdown("####SEISMIC DBE LOAD"))
        report_html_list.extend(self.seismic_dbe.report())

        report_html_list.append(markdown2.markdown("####SEISMIC MCE LOAD"))
        report_html_list.extend(self.seismic_mce.report())

        return report_html_list



    