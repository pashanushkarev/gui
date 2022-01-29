from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(423, 315)
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        Dialog.setFont(font)
        Dialog.setStyleSheet("QPushButton{\n"
"  background-color: white;  \n"
"  border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color:#D6D5D7;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  background-color:#D6D5D7;\n"
"}\n"
"QLabel{\n"
"  border: none;\n"
"}\n"
"\n"
"QLineEdit{\n"
"  border: none;\n"
"}\n"
"QPlainTextEdit{\n"
"  border: none;\n"
"}\n"
"QDialog {\n"
"  background-color: #BFBDC1;\n"
"}")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(330, 80, 75, 21))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pointDeparture = QtWidgets.QLineEdit(Dialog)
        self.pointDeparture.setGeometry(QtCore.QRect(140, 20, 271, 20))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        self.pointDeparture.setFont(font)
        self.pointDeparture.setText("")
        self.pointDeparture.setObjectName("pointDeparture")
        self.pointArrival = QtWidgets.QLineEdit(Dialog)
        self.pointArrival.setGeometry(QtCore.QRect(140, 50, 271, 20))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        self.pointArrival.setFont(font)
        self.pointArrival.setObjectName("pointArrival")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 20, 131, 16))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 121, 16))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(10, 80, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.result = QtWidgets.QPlainTextEdit(Dialog)
        self.result.setGeometry(QtCore.QRect(10, 110, 401, 191))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        self.result.setFont(font)
        self.result.setObjectName("result")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Расчет кратчайшего расстояния между станциями"))
        self.pushButton.setText(_translate("Dialog", "Расчёт"))
        self.label.setText(_translate("Dialog", "Пункт отправления:"))
        self.label_2.setText(_translate("Dialog", "Пункт прибытия:"))
        self.label_3.setText(_translate("Dialog", "Результаты"))
