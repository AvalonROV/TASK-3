import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(30, 30, 1000, 1000)
        

    def paintEvent(self, event):
        painter = QPainter(self)
        pixmap = QPixmap("Task3.png")
        painter.drawPixmap(10, 20, 777, 278, pixmap)
        pen = QPen(Qt.red, 3)
        painter.setPen(pen)
        painter.drawLine(10, 40, self.rect().width() -10 , 10)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())