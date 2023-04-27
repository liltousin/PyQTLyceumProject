from sqlite3 import Connection

from PyQt5.QtWidgets import QListWidgetItem, QWidget

from akk_status_funcs import check_ban_status
from sql_functions import del_akk_in_db, set_akk_status
from tg_auth_funcions import code_checker, password_checker
from Ui_reauth_akk_form import Ui_ReauthAkkForm


class ReauthAkkForm(QWidget, Ui_ReauthAkkForm):
    def __init__(self, con: Connection):
        super().__init__()
        self.setupUi(self)
        self.connection = con
        self.client = None
        # self.endflag = False
        self.pswd_widget.setEnabled(False)
        self.cancel_btn.clicked.connect(self.close)
        self.code_line.textChanged.connect(self.check_code_line)

        self.code_line.returnPressed.connect(self.reauth_akk)
        self.reauth_akk_btn.clicked.connect(self.reauth_akk)
        self.pswd_line.textChanged.connect(self.check_pswd_line)
        self.pswd_line.returnPressed.connect(self.reauth_akk)

    def set_akk(self, akk: QListWidgetItem):
        status, client = check_ban_status(akk.text(), return_client=True)
        if status == 'notauth':
            self.phone_label.setText(akk.text())
            self.show()
            # TODO: разобраться нужна ли эта фигня
            if self.client:
                if self.client.session.filename != client.session.filename:
                    self.client.session.delete()
            self.client = client
            self.code_line.setEnabled(True)
            self.code_line.setText('')
            self.code_line.setFocus()
        else:
            set_akk_status(
                self.connection, status, akk.text()
            )

    def check_code_line(self):
        for i in set(self.code_line.text()):
            if not i.isdecimal():
                self.code_line.setText(self.code_line.text().replace(i, ''))

        self.reauth_akk_btn.setEnabled(bool(self.code_line.text()))
        self.code_error_label.setText('')
        self.pswd_widget.setEnabled(False)
        self.pswd_line.setText('')

    def reauth_akk(self):
        if self.reauth_akk_btn.isEnabled():
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
                    self.reauth_akk_btn.setEnabled(False)
                else:
                    self.code_error_label.setText('')
                    self.pswd_widget.setEnabled(True)
                    self.pswd_line.setText('')
                    self.code_line.setEnabled(False)
                    self.reauth_akk_btn.setEnabled(False)
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
                    self.reauth_akk_btn.setEnabled(False)

    def check_pswd_line(self):
        self.reauth_akk_btn.setEnabled(bool(self.pswd_line.text()))
        self.pswd_error_label.setText('')

    def clean_form(self):
        if self.client:
            self.client.disconnect()
        # TODO: разобраться нужел ли эндфлаг
        # self.endflag = False
        self.client = None
        self.code_line.setText('')
        self.pswd_line.setText('')
        self.code_line.setEnabled(False)
        self.reauth_akk_btn.setEnabled(False)
        self.pswd_widget.setEnabled(False)
