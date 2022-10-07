#!/usr/bin/env python3
# coding=utf-8
import random
import sys

from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi


class Main(QDialog):
    def __init__(self):
        super(Main, self).__init__()
        loadUi('main.ui', self)

        self.setWindowTitle('Работа с визуальными табличными данными в Python')

        self.btn_random_number.clicked.connect(self.fill_random_numbers)
        self.btn_solve.clicked.connect(self.solve)

    def fill_random_numbers(self):

        row = 0
        col = 0

        while row < self.tableWidget.rowCount():
            while col < self.tableWidget.columnCount():
                random_num = random.randrange(-20, 21, 1)
                self.tableWidget.setItem(row, col, QTableWidgetItem(str(random_num)))
                col += 1
            row += 1
            col = 0

        list_information_max_num = finder(self.tableWidget)

        if not list_information_max_num:
            self.label_error.setText('Введены неправильные данные!')
        else:
            self.label_max.setText(
                'Максимальный элемент: ' + str(list_information_max_num[0]) + ' [' +
                str(list_information_max_num[1] + 1) + ';' + str(list_information_max_num[2] + 1) + '],\n' +
                'число нулей - ' + str(list_information_max_num[3]) + ', ' +
                'число положительных чисел - ' + str(list_information_max_num[4]))

    def solve(self):
        list_information_max_num = finder(self.tableWidget)

        if not list_information_max_num:
            self.label_error.setText('Введены некорректные данные!')
            return
        else:
            self.label_max.setText(
                'Максимальный элемент: ' + str(list_information_max_num[0]) + ' [' +
                str(list_information_max_num[1] + 1) + ';' + str(list_information_max_num[2] + 1) + '],\n' +
                'число нулей - ' + str(list_information_max_num[3]) + ', ' +
                'число положительных чисел - ' + str(list_information_max_num[4]))

        count_zero = list_information_max_num[3]
        count_pos = list_information_max_num[4]

        if count_zero <= 5 or count_pos <= 3:
            self.label_answer.setText(
                'Число нулей в таблице(' + str(count_zero) + ') не больше пяти\n'
                'или число положительных чисел (' + str(count_pos) + ') не больше трех\n'
                'Задание не будет выполнено.'
            )
        else:
            max = list_information_max_num[0] * 2
            self.label_answer.setText(
                'Количество нулей в таблице больше пяти и число положительных чисел больше трех.\n' +
                'Макс. элемент таблицы был увеличен в два раза.'
            )
            self.tableWidget.setItem(list_information_max_num[1], list_information_max_num[2], QTableWidgetItem(str(max)))

        self.label_error.setText('')


def finder(table_widget):

    row_max_number = 0
    col_max_number = 0
    try:
        max_num = int(table_widget.item(row_max_number, col_max_number).text())
    except Exception:
        return None

    row = 0
    col = 0
    count_zero = 0
    count_pos = 0

    try:
        while row < table_widget.rowCount():
            while col < table_widget.columnCount():
                number = int(table_widget.item(row, col).text())
                if number > max_num:
                    max_num = number
                    row_max_number = row
                    col_max_number = col
                if number == 0:
                    count_zero += 1
                if number >= 0:
                    count_pos += 1
                col += 1
            row += 1
            col = 0
        return [max_num, row_max_number, col_max_number, count_zero, count_pos]
    except Exception:
        return None


def main():
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
