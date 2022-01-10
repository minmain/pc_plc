
from pyModbusTCP.client import ModbusClient
c = ModbusClient(host="192.168.1.30", port=502, auto_open=True)
regs = c.read_holding_registers(0,3)
if regs:
        """print(regs[0],regs[1], regs[2] ,sep='\n')"""
else:
      print("ㅠㅠ")

c.close()


import sys
from PyQt5.QtWidgets import *

from PyQt5 import uic
from PyQt5.QAxContainer import *
from PyQt5.QtGui import *

from_class = uic.loadUiType("ui.ui")[0]

class Mywindow(QMainWindow, from_class):
    def __init__(self):
        super().__init__()
        self.setUI()

        self.textEdit.setText("데이타를 가져왔습니다")
        print(self.textEdit.toPlainText())

    def setUI(self):
        self.setupUi(self)
        self.pushButton.clicked.connect(self.buttonClick)  # 1.푸쉬버튼을 클릭하면

    def buttonClick(self):
         print(regs[1])                       # 2.버튼클릭을 프린트 ex : Reg[1.2.3] 값으로 변경해보기


if __name__ == "__main__":
    print("Hello Word");

    app = QApplication(sys.argv)
    myApp = Mywindow()
    myApp.show()
    app.exec_()

