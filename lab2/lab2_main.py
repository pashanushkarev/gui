import sys
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtCore import Qt, QPoint, QRect
from PyQt5.QtGui import QPixmap, QPen, QPainter
from PyQt5.QtWidgets import QApplication, QFileDialog, QPushButton

class RectanglePainter(QtWidgets.QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.begin = QPoint()
        self.end = QPoint()
        self.setGeometry(0, 0, 0, 0)
        self.pixmap = None
        self.rectangles = []
        self.pen = QPen(Qt.green, 2, Qt.SolidLine)
        self.show()

    def paintEvent(self, event):
        if self.pixmap is not None:
            qp = QPainter(self)
            qp.drawPixmap(0, 0, self.pixmap)
            if self.begin != self.end:
                qp.setPen(self.pen)
                qp.drawRect(QRect(self.begin, self.end))

    def mousePressEvent(self, event):
        self.begin = event.pos()
        self.end = event.pos()
        self.update()

    def mouseMoveEvent(self, event):
        self.end = event.pos()
        self.update()

    def mouseReleaseEvent(self, event):
        self.end = event.pos()
        self.drawRect()
        self.rectangles.append(QRect(self.begin, event.pos()))
        self.update()

    def setPixmap(self, pm: QPixmap):
        self.pixmap = pm

    def drawRect(self):
        if self.pixmap is not None:
            qp = QtGui.QPainter(self.pixmap)
            qp.setPen(self.pen)
            qp.drawRect(QtCore.QRect(self.begin, self.end))


MAX_WIDTH = 800.0
MAX_HEIGHT = 600.0

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 650

IMAGE_START_X = 0
IMAGE_START_Y = 50

IMAGE_FILTER = "Image Files (*.png *.jpg *.bmp)"
RECT_FILE_SUFFIX = "-rectangles.txt"


class Screen(QtWidgets.QMainWindow):
    def __init__(self):
        super(Screen, self).__init__()

        self.resize(WINDOW_WIDTH, WINDOW_HEIGHT)

        self.imageContainer = RectanglePainter(self)

        self.loadImage = QPushButton(self)
        self.loadImage.setText("Загрузить")
        self.loadImage.setGeometry(QRect(10, 10, 130, 25))
        
        self.saveImage = QPushButton(self)
        self.saveImage.setGeometry(QRect(150, 10, 130, 25))
        self.saveImage.setText("Сохранить")

        self.loadImage.clicked.connect(self.load_image)
        self.saveImage.clicked.connect(self.save_image)

        self.show()

    def load_image(self):
        file_name = QFileDialog.getOpenFileName(self, caption="Open file", filter=IMAGE_FILTER)[0]
        if file_name is None or len(file_name) == 0:
            return
        pixmap = QPixmap(file_name)

        w = pixmap.width()
        h = pixmap.height()

        image_position = Screen.calc_image_position(w, h)

        scaled_width = image_position.width()
        scaled_height = image_position.height()

        pixmap = pixmap.scaled(scaled_width, scaled_height)

        self.imageContainer.setGeometry(image_position)
        self.imageContainer.setPixmap(pixmap)

    def save_image(self):
        file_name = QFileDialog.getSaveFileName(self, "Save File", filter=IMAGE_FILTER)[0]
        if file_name is None or len(file_name) == 0:
            return
        self.imageContainer.pixmap.save(file_name)
        rect_file_name = file_name + RECT_FILE_SUFFIX
        rect_file = open(rect_file_name, mode='w')
        for r in self.imageContainer.rectangles:
            center = r.center()
            rect_file.write(
                "[{}, {}]\n".format(center.x(), center.y())
            )
        rect_file.close()

    @staticmethod
    def calc_image_position(width, height) -> QRect:
        width_cf = Screen.get_scale_coefficient(width, MAX_WIDTH)
        height_cf = Screen.get_scale_coefficient(height, MAX_HEIGHT)
        max_cf = float(max(width_cf, height_cf))

        scaled_width = round(float(width) / max_cf)
        scaled_height = round(float(height) / max_cf)

        return QRect(
            round(IMAGE_START_X + (MAX_WIDTH - scaled_width) // 2),
            round(IMAGE_START_Y + (MAX_HEIGHT - scaled_height) // 2),
            scaled_width,
            scaled_height
        )

    @staticmethod
    def get_scale_coefficient(value, max_value) -> float:
        coefficient = 1
        if value > max_value:
            coefficient = float(value) / max_value
        return float(coefficient)


if __name__ == '__main__':
    application = QApplication(sys.argv)
    ex = Screen()
    sys.exit(application.exec_())


