from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLCDNumber, QLabel, QLineEdit
import sys


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(150, 150, 400, 400)
        self.setWindowTitle('Первая программа')

        self.btn = QPushButton('Пуск', self)
        self.btn.move(20, 60)
        self.btn.clicked.connect(self.run)

        self.first_input = QLineEdit(self)
        self.first_input.move(20, 20)

        self.second_input = QLineEdit(self)
        self.second_input.move(180, 20)

        self.summa = QLabel(self)
        self.summa.setText("Сумма:")
        self.summa.move(20, 100)

        self.summ = QLCDNumber(self)
        self.summ.move(100, 100)

        self.raznost = QLabel(self)
        self.raznost.setText("Разность:")
        self.raznost.move(20, 140)

        self.ras = QLCDNumber(self)
        self.ras.move(100, 140)

        self.chastnoe = QLabel(self)
        self.chastnoe.setText("Частное:")
        self.chastnoe.move(20, 180)

        self.chas = QLCDNumber(self)
        self.chas.move(100, 180)

        self.proisvedenie = QLabel(self)
        self.proisvedenie.setText("Произведение:")
        self.proisvedenie.move(20, 220)

        self.prois = QLCDNumber(self)
        self.prois.move(100, 220)

    def run(self):
        x = int(self.first_input.text())
        y = int(self.second_input.text())
        self.summ.display(x + y)
        self.ras.display(x - y)
        try:
            self.chas.display(x / y)
        except:
            self.chas.display("Error")
        self.prois.display(x * y)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
