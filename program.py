from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication

app = QApplication([])
a = int(input('Первое число: '))
b = int(input('Второе число: '))
c = a + b
print('Сумма первого и второго числа: ', c)
h = int(input('Третье число: '))
k = c * h
print('Произведение суммы первых двух чисел и третьего: ', k)
app.exec_()