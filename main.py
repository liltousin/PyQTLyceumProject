import sqlite3
import sys

from PyQt5.QtCore import QEvent
from PyQt5.QtWidgets import (
    QAction,
    QApplication,
    QListWidgetItem,
    QMainWindow,
    QMenu,
    QWidget,
)

from Ui_add_akk_form import Ui_AddAkkForm
from Ui_main import Ui_MainWindow


class AddAkkForm(QWidget, Ui_AddAkkForm):
    def __init__(self, con):
        super().__init__()
        self.setupUi(self)
        self.connection = con
        self.cancel_btn.clicked.connect(self.close)
        self.phone_line.textChanged.connect(self.check_phone_line)
        self.send_code_btn.clicked.connect(self.send_code)

    def check_phone_line(self):
        if self.phone_line.text():
            self.send_code_btn.setEnabled(True)
        else:
            self.send_code_btn.setEnabled(False)
        self.phone_error_label.setText('')
        self.code_line.setEnabled(False)

    def send_code(self):
        pass

    def closeEvent(self, event):
        pass


class Program(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.connection = sqlite3.connect("db.sqlite")
        self.setup_db()
        self.add_akk_form = AddAkkForm(self.connection)
        self.add_akk_form.installEventFilter(self)
        self.add_akk_btn.clicked.connect(self.add_akk_form.show)
        self.list_of_akks_widget.installEventFilter(self)
        # self.list_of_akks_widget.itemDoubleClicked.connect(self.show_akk)

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
            akk = source.itemAt(event.pos())

            if self.check_akk(akk) == 'not_auth':
                list_of_actions.append(reauth_akk_action)
            list_of_actions.append(del_akk_action)
            menu.addActions(list_of_actions)

            if action := menu.exec_(event.globalPos()):
                if action == del_akk_action:
                    self.del_akk(akk)
                elif action == reauth_akk_action:
                    self.reauth_akk(akk)
            return True
        elif event.type() == QEvent.Show and source is self.add_akk_form:
            self.setEnabled(False)
            return True
        elif event.type() == QEvent.Close and source is self.add_akk_form:
            self.setEnabled(True)
            self.reload_akks()
            return True
        return super().eventFilter(source, event)

    def reload_akks(self):
        pass

    # def show_akk(self, akk: Akk):
    #     print(akk.text())

    # def reauth_akk(self, akk: Akk):
    #     print(akk.text())

    # def del_akk(self, akk: Akk):
    #     akk.listWidget().takeItem(akk.listWidget().row(akk))

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
