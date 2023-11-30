from cProfile import label
import sys
from tkinter import Label

from PyQt5.QtWidgets import (
    QApplication,
    QDialog,
    QLineEdit,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QLabel
)

def getRow(name:str):
    horizontalStackPanel = QHBoxLayout()
    label = QLabel(name)
    editor = QLineEdit()
    label.setFixedWidth(150)
    editor.setFixedWidth(400)
    horizontalStackPanel.addWidget(label)
    horizontalStackPanel.addWidget(editor)
    return horizontalStackPanel

def getButton(name:str):
    button = QPushButton()
    button.setText(name)
    button.setFixedWidth(500)
    return button

def getButtonRow(name:str):
    horizontalStackPanel = QHBoxLayout()
    horizontalStackPanel.addWidget(getButton(name))
    return horizontalStackPanel

class Dialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("RF Calculator")
        verticalStackPanel = QVBoxLayout()
        verticalStackPanel.addItem(getRow(name="Design Moment"))
        verticalStackPanel.addItem(getRow(name="R/F Width"))
        verticalStackPanel.addItem(getRow(name="R/F Depth"))
        verticalStackPanel.addItem(getRow(name="Fck"))
        verticalStackPanel.addItem(getRow(name="Fy"))
        verticalStackPanel.addItem(getButtonRow("Calculate"))
        self.setLayout(verticalStackPanel)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlg = Dialog()
    dlg.show()
    sys.exit(app.exec_())