from enum import Enum
from PyQt5.QtGui import (QFont)
from PyQt5.QtWidgets import (
    QApplication,
    QDialog,
    QLineEdit,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QLabel
)
from numpy import var

def getFont(fontSize):
    font = QFont("Arial")
    font.setPointSize(fontSize)
    font.styleHint = QFont.Monospace
    return font
    

def getLabel(name:str,width:int,height:int,fontSize:int):
    label = QLabel(name)
    label.setFixedWidth(width)
    label.setFixedHeight(height)
    label.setFont(getFont(fontSize))
    return label    


def getEditor(width:int,height:int,fontSize:int):
    editor = QLineEdit()
    editor.setFixedWidth(width)
    editor.setFixedHeight(height)
    editor.setFont(getFont(fontSize))
    return editor

def getStringFromEditText(editor:QLineEdit):
    return str(editor.text())

def setStringToEditText(editor:QLineEdit,string:str):
    editor.setText(string)

def getFloatFromEditText(editor:QLineEdit):
    data = getStringFromEditText(editor)
    if(data!=''):
        return float(data)
    return 0

def getButton(name:str,fontSize:int):
    button = QPushButton()
    button.setText(name)
    button.setFixedWidth(500)
    font = QFont()
    font.setPointSize(fontSize)
    button.setFont(getFont(fontSize))
    return button

def getRow(name:str="variable",default:str="0",columnSize=[100,200],rowSize=30,fontSize:int=15):
    horizontalStackPanel = QHBoxLayout()
    label = getLabel(name,columnSize[0],rowSize,fontSize)
    editor = getEditor(columnSize[1],rowSize,fontSize)
    setStringToEditText(editor,str(default))
    horizontalStackPanel.addWidget(label)
    horizontalStackPanel.addWidget(editor)
    return horizontalStackPanel,editor

def getResultRow(columnSize=[100,200],rowSize=30,fontSize:int=15):
    horizontalStackPanel = QHBoxLayout()
    label = getLabel("Result",columnSize[0],rowSize,fontSize)
    editor = getEditor(columnSize[1],rowSize,fontSize)
    horizontalStackPanel.addWidget(label)
    horizontalStackPanel.addWidget(editor)
    return horizontalStackPanel,editor

def getButtonRow(name:str,fontSize:int):
    horizontalStackPanel = QHBoxLayout()
    button = getButton(name,fontSize)
    horizontalStackPanel.addWidget(button)
    return horizontalStackPanel,button

def getVerticalLayout(items):
    verticalStackPanel = QVBoxLayout()
    for item in items:
        verticalStackPanel.addItem(item)
    return verticalStackPanel

class Input_type(Enum):
    EditBox = QLineEdit

class ui_form_base:
    display_data : str
    variable_name : str
    default_value : str
    input_type : Input_type

    def __init__(self,variable_name:str="variable_name",display_data:str="display_name",default_data:str="0",input_type:Input_type=QLineEdit):
        self.display_data = display_data
        self.variable_name = variable_name
        self.default_value = default_data
        self.input_type = input_type

def makeAForm(formWindow:QDialog,items):
    ui_rows = []    
    columnSize = [500,500]
    rowSize = 40

    form_controls = {}

    for item in items :
        data_row = getRow(name=item.display_data,default=item.default_value,columnSize=columnSize,rowSize=rowSize,fontSize=12)
        form_controls[item.variable_name] = data_row[1]
        ui_rows.append(data_row[0])

    result_row = getResultRow(columnSize=columnSize,rowSize=rowSize,fontSize=12)
    submit_button_row = getButtonRow("Calculate",fontSize=15)

    form_controls["result"] = result_row[1]
    form_controls["submit"] = submit_button_row[1]

    ui_rows.append(result_row[0])
    ui_rows.append(submit_button_row[0])

    stack = getVerticalLayout(ui_rows)
    formWindow.setLayout(stack)

    return form_controls



