import sqlite3
import sys
from random import choice

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QEvent
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import (
    QAction,
    QApplication,
    QListWidgetItem,
    QMainWindow,
    QMenu,
    QWidget,
)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(660, 500)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        spacerItem = QtWidgets.QSpacerItem(
            40,
            20,
            QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Minimum,
        )
        self.horizontalLayout_9.addItem(spacerItem)
        self.task_label = QtWidgets.QLabel(self.centralwidget)
        self.task_label.setTextFormat(QtCore.Qt.AutoText)
        self.task_label.setAlignment(QtCore.Qt.AlignCenter)
        self.task_label.setObjectName("task_label")
        self.horizontalLayout_9.addWidget(self.task_label)
        spacerItem1 = QtWidgets.QSpacerItem(
            40,
            20,
            QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Minimum,
        )
        self.horizontalLayout_9.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.add_task_btn = QtWidgets.QPushButton(self.centralwidget)
        self.add_task_btn.setObjectName("add_task_btn")
        self.horizontalLayout_6.addWidget(self.add_task_btn)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.list_of_task_widget = QtWidgets.QListWidget(self.centralwidget)
        self.list_of_task_widget.setMinimumSize(QtCore.QSize(0, 0))
        self.list_of_task_widget.setObjectName("list_of_task_widget")
        self.verticalLayout.addWidget(self.list_of_task_widget)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem2 = QtWidgets.QSpacerItem(
            40,
            20,
            QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Minimum,
        )
        self.horizontalLayout_8.addItem(spacerItem2)
        self.import_tasks_btn = QtWidgets.QPushButton(self.centralwidget)
        self.import_tasks_btn.setObjectName("import_tasks_btn")
        self.horizontalLayout_8.addWidget(self.import_tasks_btn)
        self.export_tasks_btn = QtWidgets.QPushButton(self.centralwidget)
        self.export_tasks_btn.setEnabled(False)
        self.export_tasks_btn.setObjectName("export_tasks_btn")
        self.horizontalLayout_8.addWidget(self.export_tasks_btn)
        spacerItem3 = QtWidgets.QSpacerItem(
            40,
            20,
            QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Minimum,
        )
        self.horizontalLayout_8.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        spacerItem4 = QtWidgets.QSpacerItem(
            40,
            20,
            QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Minimum,
        )
        self.horizontalLayout_10.addItem(spacerItem4)
        self.akks_label = QtWidgets.QLabel(self.centralwidget)
        self.akks_label.setAlignment(QtCore.Qt.AlignCenter)
        self.akks_label.setObjectName("akks_label")
        self.horizontalLayout_10.addWidget(self.akks_label)
        spacerItem5 = QtWidgets.QSpacerItem(
            40,
            20,
            QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Minimum,
        )
        self.horizontalLayout_10.addItem(spacerItem5)
        self.verticalLayout_2.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.add_akk_btn = QtWidgets.QPushButton(self.centralwidget)
        self.add_akk_btn.setObjectName("add_akk_btn")
        self.horizontalLayout_3.addWidget(self.add_akk_btn)
        self.del_nwork_akks_btn = QtWidgets.QPushButton(self.centralwidget)
        self.del_nwork_akks_btn.setEnabled(False)
        self.del_nwork_akks_btn.setObjectName("del_nwork_akks_btn")
        self.horizontalLayout_3.addWidget(self.del_nwork_akks_btn)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.list_of_akks_widget = QtWidgets.QListWidget(self.centralwidget)
        self.list_of_akks_widget.setMinimumSize(QtCore.QSize(0, 0))
        self.list_of_akks_widget.setEditTriggers(
            QtWidgets.QAbstractItemView.DoubleClicked
            | QtWidgets.QAbstractItemView.EditKeyPressed
        )
        self.list_of_akks_widget.setObjectName("list_of_akks_widget")
        self.verticalLayout_2.addWidget(self.list_of_akks_widget)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem6 = QtWidgets.QSpacerItem(
            40,
            20,
            QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Minimum,
        )
        self.horizontalLayout_2.addItem(spacerItem6)
        self.import_akks_btn = QtWidgets.QPushButton(self.centralwidget)
        self.import_akks_btn.setObjectName("import_akks_btn")
        self.horizontalLayout_2.addWidget(self.import_akks_btn)
        self.export_akks_btn = QtWidgets.QPushButton(self.centralwidget)
        self.export_akks_btn.setEnabled(False)
        self.export_akks_btn.setObjectName("export_akks_btn")
        self.horizontalLayout_2.addWidget(self.export_akks_btn)
        spacerItem7 = QtWidgets.QSpacerItem(
            40,
            20,
            QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Minimum,
        )
        self.horizontalLayout_2.addItem(spacerItem7)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.run_tasks_btn = QtWidgets.QPushButton(self.centralwidget)
        self.run_tasks_btn.setObjectName("run_tasks_btn")
        self.horizontalLayout_5.addWidget(self.run_tasks_btn)
        self.stop_tasks_btn = QtWidgets.QPushButton(self.centralwidget)
        self.stop_tasks_btn.setEnabled(False)
        self.stop_tasks_btn.setObjectName("stop_tasks_btn")
        self.horizontalLayout_5.addWidget(self.stop_tasks_btn)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(
            _translate("MainWindow", "Рассылка по чатам")
        )
        self.task_label.setText(_translate("MainWindow", "Список тасков"))
        self.add_task_btn.setText(_translate("MainWindow", "Добавить"))
        self.import_tasks_btn.setText(
            _translate("MainWindow", "Импортировать")
        )
        self.export_tasks_btn.setText(
            _translate("MainWindow", "Экспортировать")
        )
        self.akks_label.setText(_translate("MainWindow", "Список аккаунтов"))
        self.add_akk_btn.setText(_translate("MainWindow", "Добавить"))
        self.del_nwork_akks_btn.setText(
            _translate("MainWindow", "Удалить нерабочие")
        )
        self.import_akks_btn.setText(_translate("MainWindow", "Импортировать"))
        self.export_akks_btn.setText(
            _translate("MainWindow", "Экспортировать")
        )
        self.run_tasks_btn.setText(_translate("MainWindow", "Запуск"))
        self.stop_tasks_btn.setText(_translate("MainWindow", "Стоп"))


class Ui_AddAkkForm(object):
    def setupUi(self, AddAkkForm):
        AddAkkForm.setObjectName("AddAkkForm")
        AddAkkForm.resize(400, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(AddAkkForm)
        self.verticalLayout.setObjectName("verticalLayout")
        self.phone_label = QtWidgets.QLabel(AddAkkForm)
        self.phone_label.setObjectName("phone_label")
        self.verticalLayout.addWidget(self.phone_label)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.phone_line = QtWidgets.QLineEdit(AddAkkForm)
        self.phone_line.setMinimumSize(QtCore.QSize(0, 0))
        self.phone_line.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.phone_line.setText("")
        self.phone_line.setObjectName("phone_line")
        self.horizontalLayout_2.addWidget(self.phone_line)
        self.send_code_btn = QtWidgets.QPushButton(AddAkkForm)
        self.send_code_btn.setEnabled(False)
        self.send_code_btn.setObjectName("send_code_btn")
        self.horizontalLayout_2.addWidget(self.send_code_btn)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.phone_error_label = QtWidgets.QLabel(AddAkkForm)
        self.phone_error_label.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.phone_error_label.setFont(font)
        self.phone_error_label.setMouseTracking(True)
        self.phone_error_label.setMidLineWidth(0)
        self.phone_error_label.setTextFormat(QtCore.Qt.RichText)
        self.phone_error_label.setAlignment(
            QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop
        )
        self.phone_error_label.setObjectName("phone_error_label")
        self.verticalLayout.addWidget(self.phone_error_label)
        self.code_label = QtWidgets.QLabel(AddAkkForm)
        self.code_label.setObjectName("code_label")
        self.verticalLayout.addWidget(self.code_label)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.code_line = QtWidgets.QLineEdit(AddAkkForm)
        self.code_line.setEnabled(False)
        self.code_line.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.code_line.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.code_line.setText("")
        self.code_line.setObjectName("code_line")
        self.horizontalLayout_3.addWidget(self.code_line)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.code_error_label = QtWidgets.QLabel(AddAkkForm)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.code_error_label.setFont(font)
        self.code_error_label.setAlignment(
            QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop
        )
        self.code_error_label.setObjectName("code_error_label")
        self.verticalLayout.addWidget(self.code_error_label)
        spacerItem = QtWidgets.QSpacerItem(
            20,
            40,
            QtWidgets.QSizePolicy.Minimum,
            QtWidgets.QSizePolicy.Expanding,
        )
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.cancel_btn = QtWidgets.QPushButton(AddAkkForm)
        self.cancel_btn.setMinimumSize(QtCore.QSize(156, 0))
        self.cancel_btn.setObjectName("cancel_btn")
        self.horizontalLayout.addWidget(self.cancel_btn)
        self.add_akk_btn = QtWidgets.QPushButton(AddAkkForm)
        self.add_akk_btn.setEnabled(False)
        self.add_akk_btn.setObjectName("add_akk_btn")
        self.horizontalLayout.addWidget(self.add_akk_btn)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(AddAkkForm)
        QtCore.QMetaObject.connectSlotsByName(AddAkkForm)

    def retranslateUi(self, AddAkkForm):
        _translate = QtCore.QCoreApplication.translate
        AddAkkForm.setWindowTitle(_translate("AddAkkForm", "Добавить аккаунт"))
        self.phone_label.setText(_translate("AddAkkForm", "Номер телефона:"))
        self.send_code_btn.setText(_translate("AddAkkForm", "Отправить код"))
        self.phone_error_label.setText(
            _translate(
                "AddAkkForm",
                "<html><head/><body><p><span style=\" color:#fc0107;\">"
                "Неправильный номер!</span></p></body></html>",
            )
        )
        self.code_label.setText(_translate("AddAkkForm", "Код:"))
        self.code_error_label.setText(
            _translate(
                "AddAkkForm",
                "<html><head/><body><p><span style=\" color:#fc0107;\">"
                "Неверный код!</span></p></body></html>",
            )
        )
        self.cancel_btn.setText(_translate("AddAkkForm", "Отмена"))
        self.add_akk_btn.setText(_translate("AddAkkForm", "Добавить аккаунт"))


class AddAkkForm(QWidget, Ui_AddAkkForm):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.phone_line.textChanged.connect(self.check_phone_line)

    def check_phone_line(self):
        if self.phone_line.text():
            self.send_code_btn.setEnabled(True)
        else:
            self.send_code_btn.setEnabled(False)
        self.phone_error_label.setText('')


class Program(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.ban_color = QColor(255, 0, 0, 127)
        self.not_auth_color = QColor(255, 255, 0, 127)
        self.auth_color = QColor(0, 255, 0, 127)
        self.setupUi(self)
        self.add_akk_form = AddAkkForm()
        self.add_akk_form.installEventFilter(self)
        self.connection = sqlite3.connect("db.sqlite")
        self.setup_db()
        self.add_akk_btn.clicked.connect(self.add_akk)
        self.list_of_akks_widget.installEventFilter(self)
        self.list_of_akks_widget.itemDoubleClicked.connect(self.show_akk)

    def setup_db(self):
        cur = self.connection.cursor()
        cur.execute(
            '''CREATE TABLE IF NOT EXISTS akks (
    id INTEGER PRIMARY KEY AUTOINCREMENT
        UNIQUE
        NOT NULL,
    phone STRING UNIQUE NOT NULL)'''
        )
        self.connection.commit()

    def eventFilter(self, source, event: QEvent) -> bool:
        if (
            event.type() == QEvent.ContextMenu
            and source is self.list_of_akks_widget
            and type(source.itemAt(event.pos())) is QListWidgetItem
        ):
            menu = QMenu()
            del_akk_action = QAction('Удалить аккаунт')
            reauth_akk_action = QAction('Переавторизовать')
            list_of_actions = []
            if (
                source.itemAt(event.pos()).background().color()
                == self.not_auth_color
            ):
                list_of_actions.append(reauth_akk_action)
            list_of_actions.append(del_akk_action)
            menu.addActions(list_of_actions)
            if action := menu.exec_(event.globalPos()):
                akk = source.itemAt(event.pos())
                if action == del_akk_action:
                    self.del_akk(akk)
                elif action == reauth_akk_action:
                    self.reauth_akk(akk)
            return True
        elif event.type() == QEvent.Show and source is self.add_akk_form:
            self.setDisabled(True)
            return True
        elif event.type() == QEvent.Close and source is self.add_akk_form:
            self.setDisabled(False)
            return True
        return super().eventFilter(source, event)

    def upadte_view(self):
        self.reload_akks()
        self.reload_tasks()

    def load_akks(self):
        pass

    def check_akk(self, akk):
        pass

    def add_akk(self):
        self.add_akk_form.show()
        # test_item = QListWidgetItem(
        #     'akk' + str(self.list_of_akks_widget.count())
        # )
        # test_item.setBackground(
        #     choice((self.ban_color, self.not_auth_color, self.auth_color))
        # )
        # self.list_of_akks_widget.addItem(test_item)

    def show_akk(self, akk: QListWidgetItem):
        print(akk.text())

    def reauth_akk(self, akk: QListWidgetItem):
        print(akk.text())

    def del_akk(self, akk: QListWidgetItem):
        akk.listWidget().takeItem(akk.listWidget().row(akk))

    def load_tasks(self):
        pass

    def closeEvent(self, event):
        self.connection.close()
        if not self.add_akk_form.isHidden():
            self.add_akk_form.close()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    program = Program()
    program.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
