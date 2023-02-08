from sqlite3 import Connection

from PyQt5.QtWidgets import QListWidgetItem, QWidget

from akk_status_funcs import check_akk_status, check_nofile_status
from sql_functions import del_akk_in_db, set_akk_status
from tg_auth_funcions import code_checker, password_checker, try_to_send_code
from Ui_auth_akk_form import Ui_AuthAkkForm


class AuthAkkForm(QWidget, Ui_AuthAkkForm):
    def __init__(self, con: Connection) -> None:
        super().__init__()
        self.setupUi(self)
        self.connection = con
        self.client = None
        self.endflag = False
        self.pswd_widget.setEnabled(False)
        self.cancel_btn.clicked.connect(self.close)
        self.send_code_btn.clicked.connect(self.send_code)
        self.code_line.textChanged.connect(self.check_code_line)
        self.code_line.returnPressed.connect(self.auth_akk)
        self.auth_akk_btn.clicked.connect(self.auth_akk)
        self.pswd_line.textChanged.connect(self.check_pswd_line)
        self.pswd_line.returnPressed.connect(self.auth_akk)

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
            if response == 'Номер заблокирован!':
                set_akk_status(
                    self.connection,
                    'banned',
                    self.phone_label.text(),
                )
                self.endflag = True
            elif response == 'Неверный формат номера!':
                del_akk_in_db(self.connection, self.phone_label.text())
        else:
            self.phone_error_label.setText('')
            if self.client:
                if self.client.session.filename != response.session.filename:
                    self.client.session.delete()
            self.client = response
            self.code_line.setEnabled(True)
            self.code_line.setText('')
            self.code_line.setFocus()

    def check_code_line(self):
        for i in set(self.code_line.text()):
            if not i.isdecimal():
                self.code_line.setText(self.code_line.text().replace(i, ''))

        self.auth_akk_btn.setEnabled(bool(self.code_line.text()))
        self.code_error_label.setText('')
        self.pswd_widget.setEnabled(False)
        self.pswd_line.setText('')

    # TODO подредач функцию чтобы на этой формочке все работало
    def auth_akk(self):
        if self.auth_akk_btn.isEnabled():
            if not self.pswd_widget.isEnabled():
                response = code_checker(self.client, self.code_line.text())
                if response == 'ok':
                    set_akk_status(
                        self.connection, 'ok', self.phone_label.text()
                    )
                    self.endflag = True
                    self.close()
                elif type(response) == str:
                    self.code_error_label.setText(response)
                    self.auth_akk_btn.setEnabled(False)
                else:
                    self.code_error_label.setText('')
                    self.pswd_widget.setEnabled(True)
                    self.pswd_line.setText('')
                    self.send_code_btn.setEnabled(False)
                    self.code_line.setEnabled(False)
                    self.auth_akk_btn.setEnabled(False)
                    self.pswd_line.setFocus()
            else:
                response = password_checker(self.client, self.pswd_line.text())
                if response == 'ok':
                    set_akk_status(
                        self.connection, 'ok', self.phone_label.text()
                    )
                    self.endflag = True
                    self.close()
                else:
                    self.pswd_error_label.setText(response)
                    self.auth_akk_btn.setEnabled(False)

    def check_pswd_line(self):
        self.auth_akk_btn.setEnabled(bool(self.pswd_line.text()))
        self.pswd_error_label.setText('')

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
