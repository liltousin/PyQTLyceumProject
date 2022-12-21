import sqlite3
import sys

from PyQt5.QtCore import QEvent
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import (
    QAction,
    QApplication,
    QListWidgetItem,
    QMainWindow,
    QMenu,
)

from add_akk_form import AddAkkForm
from Ui_main import Ui_MainWindow


class Program(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.colors = {
            'ok': QColor(0, 255, 0, 127),
            'nofile': QColor(255, 255, 0, 127),
            'notauth': QColor(255, 127, 0, 127),
            'banned': QColor(255, 0, 0, 127),
        }
        self.setupUi(self)
        self.connection = sqlite3.connect("db.sqlite")
        self.setup_db()
        self.add_akk_form = AddAkkForm(self.connection)
        self.add_akk_form.installEventFilter(self)
        self.add_akk_btn.clicked.connect(self.add_akk_form.show)
        self.list_of_akks_widget.installEventFilter(self)
        self.list_of_akks_widget.itemDoubleClicked.connect(self.check_akk)
        self.load_akks()

    def setup_db(self):
        cur = self.connection.cursor()
        cur.execute(
            '''
CREATE TABLE IF NOT EXISTS Statuses (
    StatusId INTEGER PRIMARY KEY AUTOINCREMENT
                     NOT NULL
                     UNIQUE,
    Name     STRING  UNIQUE
                     NOT NULL
)'''
        )
        self.connection.commit()
        cur.execute(
            '''INSERT OR IGNORE INTO Statuses (Name) VALUES
                ('ok'), ('nofile'), ('notauth'), ('banned')'''
        )
        self.connection.commit()
        cur.execute(
            '''
CREATE TABLE IF NOT EXISTS Akks (
    AkkId    INTEGER PRIMARY KEY AUTOINCREMENT
                     UNIQUE
                     NOT NULL,
    Phone    STRING  UNIQUE
                     NOT NULL,
    StatusId INTEGER NOT NULL
                     REFERENCES Statuses (StatusId) ON DELETE NO ACTION
                                                    ON UPDATE NO ACTION
)'''
        )
        self.connection.commit()

    def eventFilter(self, source, event: QEvent) -> bool:
        if (
            event.type() == QEvent.ContextMenu
            and source is self.list_of_akks_widget
            and type(source.itemAt(event.pos())) is QListWidgetItem
        ):
            menu = QMenu()
            del_akk_action = QAction('Удалить')
            reauth_akk_action = QAction('Переавторизовать')
            auth_akk_action = QAction('Авторизовать')
            check_akk_action = QAction('Проверить аккаунт')
            list_of_actions = []
            akk = source.itemAt(event.pos())

            list_of_actions.append(check_akk_action)
            if akk.background().color() == self.colors['banned']:
                list_of_actions.append(del_akk_action)
            elif akk.background().color() == self.colors['notauth']:
                list_of_actions.append(reauth_akk_action)
            elif akk.background().color() == self.colors['nofile']:
                list_of_actions.append(auth_akk_action)
            list_of_actions.append(del_akk_action)
            menu.addActions(list_of_actions)

            if action := menu.exec_(event.globalPos()):
                if action == del_akk_action:
                    self.del_akk(akk.text())
                elif action == reauth_akk_action:
                    self.reauth_akk(akk.text())
                elif action == auth_akk_action:
                    self.auth_akk(akk.text())
                elif action == check_akk_action:
                    self.check_akk(akk.text())
            return True
        elif event.type() == QEvent.Show and source is self.add_akk_form:
            self.setEnabled(False)
            return True
        elif event.type() == QEvent.Close and source is self.add_akk_form:
            self.setEnabled(True)
            self.add_akk_form.clean_form()
            self.reload_akks()
            return True
        return super().eventFilter(source, event)

    def load_akks(self):
        # for phone in cur.fetchall():
        #   status = check_status(str(phone)
        self.reload_akks()

    def reload_akks(self):
        self.list_of_akks_widget.clear()
        cur = self.connection.cursor()
        cur.execute(
            '''
        SELECT Akks.Phone, Statuses.Name FROM Akks
        INNER JOIN Statuses ON Akks.StatusId = Statuses.StatusId'''
        )
        for phone, status_name in cur.fetchall():
            akk = QListWidgetItem(str(phone))
            akk.setBackground(self.colors[status_name])
            self.list_of_akks_widget.addItem(akk)

    def check_akk(self, phone: str):
        # check_status(phone)
        self.reload_akks()

    def del_akk(self, phone: str):
        # check_is_banned(phone)
        self.reload_akks()

    def reauth_akk(self, phone: str):
        # if not check_is_banned(phone):
        #   reauth_akk_form.phone = phone
        #   reauth_akk_form.show()
        pass

    def auth_akk(self, phone: str):
        # check_staus(phone)
        pass

    def load_tasks(self):
        pass

    def closeEvent(self, event):
        if not self.add_akk_form.isHidden():
            self.add_akk_form.close()
        self.connection.close()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    program = Program()
    program.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
