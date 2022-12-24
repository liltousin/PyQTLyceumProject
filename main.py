import sqlite3
import sys

from PyQt5.QtCore import QEvent
from PyQt5.QtWidgets import (
    QAction,
    QApplication,
    QListWidgetItem,
    QMainWindow,
    QMenu,
)

from add_akk_form import AddAkkForm
from sql_functions import get_akks, setup_db
from status_colors import STATUS_COLORS
from Ui_main import Ui_MainWindow


class Program(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.connection = sqlite3.connect("db.sqlite")
        setup_db(self.connection)
        self.add_akk_form = AddAkkForm(self.connection)
        self.add_akk_form.installEventFilter(self)
        self.add_akk_btn.clicked.connect(self.add_akk_form.show)
        self.list_of_akks_widget.installEventFilter(self)
        # self.list_of_akks_widget.itemDoubleClicked.connect(
        #     self.akk_info_form.show
        # )
        self.update_akks()

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
            list_of_actions = []
            akk = source.itemAt(event.pos())

            if akk.background().color() == STATUS_COLORS['banned']:
                list_of_actions.append(del_akk_action)
            elif akk.background().color() == STATUS_COLORS['notauth']:
                list_of_actions.append(reauth_akk_action)
            elif akk.background().color() == STATUS_COLORS['nofile']:
                list_of_actions.append(auth_akk_action)
            menu.addActions(list_of_actions)

            if action := menu.exec_(event.globalPos()):
                if action == del_akk_action:
                    self.del_akk(akk)
                elif action == reauth_akk_action:
                    self.reauth_akk(akk)
                elif action == auth_akk_action:
                    self.auth_akk(akk)
            return True
        elif (
            event.type() == QEvent.ContextMenu
            and source is self.list_of_akks_widget
        ):
            menu = QMenu()
            update_akks_action = QAction('Обновить все')
            menu.addAction(update_akks_action)

            if action := menu.exec_(event.globalPos()):
                if action == update_akks_action:
                    self.update_akks()
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

    def update_akks(self):

        self.reload_akks()

    def reload_akks(self):
        self.list_of_akks_widget.clear()
        akks = get_akks(self.connection)
        for phone, status_name in akks:
            akk = QListWidgetItem(str(phone))
            akk.setBackground(STATUS_COLORS[status_name])
            self.list_of_akks_widget.addItem(akk)

    def change_akk_status(self):
        pass

    def del_akk(self, akk: QListWidgetItem):
        # check_is_banned(phone)
        self.reload_akks()

    def reauth_akk(self, akk: QListWidgetItem):
        # if not check_is_banned(phone):
        #   reauth_akk_form.phone = phone
        #   reauth_akk_form.show()
        pass

    def auth_akk(self, akk: QListWidgetItem):
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
