from sqlite3 import Connection

from PyQt5.QtWidgets import QListWidgetItem, QWidget

from akk_status_funcs import check_akk_status, check_nofile_status
from sql_functions import set_akk_status
from tg_auth_funcions import code_checker, password_checker, try_to_send_code
from Ui_auth_akk_form import Ui_AuthAkkForm


class AuthAkkForm(QWidget, Ui_AuthAkkForm):
    def __init__(self, con: Connection) -> None:
        super().__init__()
        self.setupUi(self)
        self.connection = con
        self.client = None
        self.endflag = False
        self.cancel_btn.clicked.connect(self.close)
        self.send_code_btn.clicked.connect(self.send_code)
        # self.code_line.textChanged.connect(self.check_code_line)
        # self.code_line.returnPressed.connect(self.add_akk)
        # self.auth_akk_btn.clicked.connect(self.add_akk)
        # self.pswd_line.textChanged.connect(self.check_pswd_line)
        # self.pswd_line.returnPressed.connect(self.add_akk)

    def set_akk(self, akk: QListWidgetItem):
        if check_nofile_status(akk.text()):
            self.phone_label.setText(akk.text())
            self.show()
        else:
            set_akk_status(
                self.connection, check_akk_status(akk.text()), akk.text()
            )

    def send_code(self):
        response = try_to_send_code(
            self.phone_label.text(), delete_session_if_banned=False
        )
        self.send_code_btn.setEnabled(False)
        if type(response) == str:
            self.phone_error_label.setText(response)
            # TODO: разобраться с файлами сессион
            if response == 'Номер заблокирован!':
                set_akk_status(
                    self.connection,
                    'banned',
                    self.phone_label.text(),
                )
                self.endflag = True
            # TODO сделать удаление из бд если неверный формат номера
        else:
            self.phone_error_label.setText('')
            if self.client:
                if self.client.session.filename != response.session.filename:
                    self.client.session.delete()
            self.client = response
            self.code_line.setEnabled(True)
            self.code_line.setText('')
            self.code_line.setFocus()

    def clean_form(self):
        if self.client:
            self.client.disconnect()
            if not self.endflag:
                self.client.session.delete()
        self.endflag = False
        self.client = None
        self.phone_error_label.setText('')
        self.code_line.setText('')
        self.pswd_line.setText('')
        self.send_code_btn.setEnabled(True)
        self.code_line.setEnabled(False)
        self.auth_akk_btn.setEnabled(False)
        self.pswd_widget.setEnabled(False)
