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
from akk_info_form import AkkInfoForm
from akk_status_funcs import check_akk_and_update
from auth_akk_form import AuthAkkForm
from reauth_akk_form import ReauthAkkForm
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
        self.akk_info_form = AkkInfoForm(self.connection)
        self.akk_info_form.installEventFilter(self)
        self.auth_akk_form = AuthAkkForm(self.connection)
        self.auth_akk_form.installEventFilter(self)
        self.reauth_akk_form = ReauthAkkForm(self.connection)
        self.reauth_akk_form.installEventFilter(self)
        self.add_akk_btn.clicked.connect(self.add_akk_form.show)
        self.list_of_akks_widget.installEventFilter(self)
        self.list_of_akks_widget.itemDoubleClicked.connect(
            self.show_akk_info_form
        )
        self.update_akks()

    def eventFilter(self, source, event):
        if (
            event.type() == QEvent.ContextMenu
            and source is self.list_of_akks_widget
            and type(source.itemAt(event.pos())) is QListWidgetItem
            and self.isEnabled()
        ):
            self.reload_akks()
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
            and self.isEnabled()
        ):
            menu = QMenu()
            update_akks_action = QAction('Обновить все')
            menu.addAction(update_akks_action)

            if action := menu.exec_(event.globalPos()):
                if action == update_akks_action:
                    self.update_akks()
            return True

        elif event.type() == QEvent.Show and (
            source is self.add_akk_form
            or source is self.akk_info_form
            or source is self.auth_akk_form
            or source is self.reauth_akk_form
        ):
            self.setEnabled(False)
            return True

        elif event.type() == QEvent.Close and (
            source is self.add_akk_form
            or source is self.akk_info_form
            or source is self.auth_akk_form
            or source is self.reauth_akk_form
        ):
            self.setEnabled(True)
            if source is not self.akk_info_form:
                source.clean_form()
            self.reload_akks()
            return True

        return super().eventFilter(source, event)

    def update_akks(self):
        self.statusBar.clearMessage()
        akks = get_akks(self.connection)
        for phone, db_status in akks:
            try:
                check_akk_and_update(phone, db_status, self.connection)
            except ConnectionError:
                self.statusBar().showMessage('Нет подключения к интернету!')
        self.reload_akks()

    def reload_akks(self):
        self.list_of_akks_widget.clear()
        akks = get_akks(self.connection)
        there_is_banned = False
        for phone, status_name in akks:
            akk = QListWidgetItem(str(phone))
            akk.setBackground(STATUS_COLORS[status_name])
            self.list_of_akks_widget.addItem(akk)
            if status_name == 'banned':
                there_is_banned = True
        self.del_nwork_akks_btn.setEnabled(there_is_banned)

    def show_akk_info_form(self, akk: QListWidgetItem):
        self.akk_info_form.set_akk(akk)

    def change_akk_status(self):
        pass

    def del_akk(self, akk: QListWidgetItem):
        # check_is_banned(phone)
        self.reload_akks()

    def reauth_akk(self, akk: QListWidgetItem):
        self.statusBar.clearMessage()
        try:
            self.reauth_akk_form.set_akk(akk)
        except ConnectionError:
            self.statusBar.showMessage('Нет подключения к интернету!')
        self.reload_akks()

    def auth_akk(self, akk: QListWidgetItem):
        self.statusBar.clearMessage()
        try:
            self.auth_akk_form.set_akk(akk)
        except ConnectionError:
            self.statusBar.showMessage('Нет подключения к интернету!')
        self.reload_akks()

    def load_tasks(self):
        pass

    def closeEvent(self, event):
        self.add_akk_form.close()
        self.akk_info_form.close()
        self.auth_akk_form.close()
        self.connection.close()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    program = Program()
    program.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
