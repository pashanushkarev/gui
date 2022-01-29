from PyQt5 import QtCore, QtGui, QtWidgets
from ui import Ui_Dialog
import sys
import numpy as np

app = QtWidgets.QApplication(sys.argv)

Dialog = QtWidgets.QDialog()
ui = Ui_Dialog()
ui.setupUi(Dialog)
Dialog.show()
#start logic

def StationInNum(unit): #Нумерация станций
        if unit == 'Черниговка':
            return 0
        if unit == 'Саранск':
            return 1
        if unit == 'Инза':
            return 2
        if unit == 'Ульяновск':
            return 3
        if unit == 'Тольятти':
            return 4
        if unit == 'Самара':
            return 5
        if unit == 'Кинель':
            return 6
        if unit == 'Бузулук':
            return 7
        if unit == 'Пенза':
            return 8
        if unit == 'Кузнецк':
            return 9
        if unit == 'Сызрань':
            return 10
        if unit == 'Саратов':
            return 11
        if unit == 'Сенная':
            return 12
        if unit == 'Балаково':
            return 13
        if unit == 'Пугачевск':
            return 14

def NumInStation(unit): #Возврат названия станции из номера
        if unit == 0:
            return 'Черниговка'
        if unit == 1:
            return 'Саранск'
        if unit == 2:
            return 'Инза'
        if unit == 3:
            return 'Ульяновск'
        if unit == 4:
            return 'Тольятти'
        if unit == 5:
            return 'Самара'
        if unit == 6:
            return 'Кинель'
        if unit == 7:
            return 'Бузулук'
        if unit == 8:
            return 'Пенза'
        if unit == 9:
            return 'Кузнецк'
        if unit == 10:
            return 'Сызрань'
        if unit == 11:
            return 'Саратов'
        if unit == 12:
            return 'Сенная'
        if unit == 13:
            return 'Балаково'
        if unit == 14:
            return 'Пугачевск'   

d = np.loadtxt('weight.txt') #матрица весов
prev = np.loadtxt('weight.txt')#Матрица предков 
n=len(d)  #число вершин
inf = float('inf')  
for u in range (n) :
    for v in range (n) :
        if prev[u][v]==inf:
            prev[u][v]=-1
        else:
            prev[u][v]=u

def bp(): #нажатие кнопки    
    pointDeparture=ui.pointDeparture.text()
    station1= StationInNum(pointDeparture)
    pointArrival=ui.pointArrival.text()
    station2= StationInNum(pointArrival)
    #Алгоритм Флойда
    for k in range ( n) :
      for u in range (n) :
        for v in range (n) :
          if d[u][v] > d[u][k] + d[k][v] :
            d[u][v] = d[u][k] + d[k][v]
            prev[u][v] = prev[k][v]

    distance=d[station1][station2] # кратчайшее расстояние

    path=[] #список восстановления
    while station2 != station1 :
        path.append(station2)
        station2 = prev[int(station1)][int(station2)]
    path.append(station1)
    path.reverse()

    speed=75 #средняя скорость локомотива(км\ч)    
    time=distance/speed #время в пути

    ui.result.clear()
    ui.result.appendPlainText(f'Минимальное расстояние между станцией {pointDeparture} и станцией {pointArrival}= {distance} км')
    ui.result.appendPlainText(f'Путь будет проходить через следующие станции:')
    for i in range(len(path)):
        ui.result.appendPlainText(f'{i+1} станция: {NumInStation(path[i])}')
    ui.result.appendPlainText(f'Примерное время в пути: {"{0:.2f}".format(time)} часа')
 
ui.pushButton.clicked.connect(bp)

#end logic

sys.exit(app.exec_())