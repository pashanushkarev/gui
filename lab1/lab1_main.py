from PyQt5 import QtCore, QtGui, QtWidgets
from ui import Ui_Dialog
import sys
import random

app = QtWidgets.QApplication(sys.argv)

Dialog = QtWidgets.QDialog()
ui = Ui_Dialog()
ui.setupUi(Dialog)
Dialog.show()
#start logic

def bp(): #нажатие кнопки   
    a=ui.textEdit.toPlainText()
    b=ui.textEdit_2.toPlainText()
    rnd = random.randint(int(a),int(b))
    ui.label.setText(str(rnd))
    
ui.pushButton.clicked.connect(bp)

#end logic

sys.exit(app.exec_())