from sqlite3 import Connection

from PyQt5.QtWidgets import QWidget

from sql_functions import add_akk_in_db, is_akk_in_db, set_akk_status
from tg_auth_funcions import code_checker, password_checker, try_to_send_code
from Ui_add_akk_form import Ui_AddAkkForm


class AddAkkForm(QWidget, Ui_AddAkkForm):
    def __init__(self, con: Connection):
        super().__init__()
        self.setupUi(self)
        self.connection = con
        self.client = None
        self.endflag = False
        self.cancel_btn.clicked.connect(self.close)
        self.phone_line.textChanged.connect(self.check_phone_line)
        self.phone_line.returnPressed.connect(self.send_code)
        self.send_code_btn.clicked.connect(self.send_code)
        self.code_line.textChanged.connect(self.check_code_line)
        self.code_line.returnPressed.connect(self.add_akk)
        self.add_akk_btn.clicked.connect(self.add_akk)
        self.pswd_line.textChanged.connect(self.check_pswd_line)
        self.pswd_line.returnPressed.connect(self.add_akk)

    def check_phone_line(self):
        for i in set(self.phone_line.text()):
            if not i.isdecimal():
                self.phone_line.setText(self.phone_line.text().replace(i, ''))

        self.send_code_btn.setEnabled(bool(self.phone_line.text()))
        self.phone_error_label.setText('')
        self.code_line.setEnabled(False)
        self.code_line.setText('')
        self.pswd_widget.setEnabled(False)
        self.pswd_line.setText('')

    def send_code(self):
        if self.send_code_btn.isEnabled():
            response = try_to_send_code(
                self.phone_line.text(),
                not is_akk_in_db(self.connection, self.phone_line.text()),
            )
            self.send_code_btn.setEnabled(False)
            if type(response) == str:
                self.phone_error_label.setText(response)
                if response == 'Клиент уже авторизован!':
                    if self.client:
                        self.client.session.delete()
                    add_akk_in_db(self.connection, self.phone_line.text())
                elif response == 'Номер заблокирован!' and is_akk_in_db(
                    self.connection, self.phone_line.text()
                ):
                    if self.client:
                        self.client.session.delete()
                    set_akk_status(
                        self.connection,
                        'banned',
                        self.phone_line.text(),
                    )

            else:
                self.phone_error_label.setText('')
                if self.client:
                    if (
                        self.client.session.filename
                        != response.session.filename
                    ):
                        self.client.session.delete()
                self.client = response
                self.code_line.setEnabled(True)
                self.code_line.setText('')
                self.code_line.setFocus()
        else:
            if self.phone_error_label.text() == 'Клиент уже авторизован!':
                self.endflag = True
                self.close()

    def check_code_line(self):
        for i in set(self.code_line.text()):
            if not i.isdecimal():
                self.code_line.setText(self.code_line.text().replace(i, ''))
        self.add_akk_btn.setEnabled(bool(self.code_line.text()))
        self.code_error_label.setText('')
        self.pswd_widget.setEnabled(False)
        self.pswd_line.setText('')

    def add_akk(self):
        if self.add_akk_btn.isEnabled():
            if not self.pswd_widget.isEnabled():
                response = code_checker(self.client, self.code_line.text())
                if response == 'ok':
                    add_akk_in_db(self.connection, self.phone_line.text())
                    self.endflag = True
                    self.close()
                elif type(response) == str:
                    self.code_error_label.setText(response)
                    self.add_akk_btn.setEnabled(False)
                else:
                    self.code_error_label.setText('')
                    self.pswd_widget.setEnabled(True)
                    self.pswd_line.setText('')
                    self.phone_line.setEnabled(False)
                    self.send_code_btn.setEnabled(False)
                    self.code_line.setEnabled(False)
                    self.add_akk_btn.setEnabled(False)
                    self.pswd_line.setFocus()
            else:
                response = password_checker(self.client, self.pswd_line.text())
                if response == 'ok':
                    add_akk_in_db(self.connection, self.phone_line.text())
                    self.endflag = True
                    self.close()
                else:
                    self.pswd_error_label.setText(response)
                    self.add_akk_btn.setEnabled(False)

    def check_pswd_line(self):
        self.add_akk_btn.setEnabled(bool(self.pswd_line.text()))
        self.pswd_error_label.setText('')

    def clean_form(self):
        if self.client:
            self.client.disconnect()
            if not self.endflag:
                self.client.session.delete()
        self.endflag = False
        self.client = None
        self.phone_line.setText('')
        self.code_line.setText('')
        self.pswd_line.setText('')
        self.phone_line.setEnabled(True)
        self.send_code_btn.setEnabled(False)
        self.code_line.setEnabled(False)
        self.add_akk_btn.setEnabled(False)
        self.pswd_widget.setEnabled(False)
