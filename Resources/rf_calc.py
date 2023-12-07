import sys

from PyQt5.QtWidgets import (
    QApplication,
    QDialog,
)

from ui import *
from base import *

class Dialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("RF Calculator")

        form_data = []
        form_data.append(ui_form_base("design_moment","Design Moment(kN-m)",default_data="9817.6"))
        form_data.append(ui_form_base("rf_width","R/F Width(m)","2"))
        form_data.append(ui_form_base("rf_depth","R/F Depth(m)","1"))
        form_data.append(ui_form_base("fck","Fck(MPa)","30"))
        form_data.append(ui_form_base("fy","Fy(MPa)","500"))

        form_controls = {}
        form_controls = makeAForm(self,form_data)

        def clickMethod(self):
            design_moment = kNMtoNm(getFloatFromEditText(form_controls["design_moment"]))
            rf_width = getFloatFromEditText(form_controls["rf_width"])
            rf_depth = getFloatFromEditText(form_controls["rf_depth"])
            fck = MPaToPa(getFloatFromEditText(form_controls["fck"]))
            fy = MPaToPa(getFloatFromEditText(form_controls["fy"]))
            result = round(calculate_rf(design_moment,1,rf_width,rf_depth,fck,fy),5)
            setStringToEditText(form_controls["result"],str(result))

        form_controls["submit"].clicked.connect(clickMethod)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlg = Dialog()
    dlg.show()
    sys.exit(app.exec_())