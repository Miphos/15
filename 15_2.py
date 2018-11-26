from PyQt5.QtWidgets import QApplication, QWidget,QPushButton, QLineEdit,QLabel
from PyQt5.QtGui import QPixmap
import sys

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 1000, 900)
        self.setWindowTitle('15_2')

        self.btn = QPushButton('Вывести картинку', self)
        self.btn.move(20, 20)
        self.btn.clicked.connect(self.run)

        self.file_name = QLineEdit(self)
        self.file_name.move(150, 20)

        self.pixmap = QPixmap()
        self.image = QLabel(self)
        self.image.move(80,60)
        self.image.resize(950,750)
        self.image.setPixmap(self.pixmap)



    def run(self):
        self.pixmap.load(self.file_name.text())
        self.image.setPixmap(self.pixmap)

        self.image.resize(self.pixmap.width(),self.pixmap.height())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())