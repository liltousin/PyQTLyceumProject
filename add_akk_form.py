from PyQt5.QtWidgets import QWidget

from tg_auth_funcions import code_checker, password_checker, try_to_send_code
from Ui_add_akk_form import Ui_AddAkkForm


class AddAkkForm(QWidget, Ui_AddAkkForm):
    def __init__(self, con):
        super().__init__()
        self.setupUi(self)
        self.connection = con
        self.client = None
        self.cancel_btn.clicked.connect(self.close)
        self.phone_line.textChanged.connect(self.check_phone_line)
        self.send_code_btn.clicked.connect(self.send_code)
        self.code_line.textChanged.connect(self.check_code_line)
        self.code_line.installEventFilter(self)
        self.add_akk_btn.clicked.connect(self.add_akk)
        self.pswd_line.textChanged.connect(self.check_pswd_line)

    def check_phone_line(self):
        if self.phone_line.text():
            self.send_code_btn.setEnabled(True)
        else:
            self.send_code_btn.setEnabled(False)
        self.phone_error_label.setText('')
        self.code_line.setEnabled(False)
        self.code_line.setText('')
        self.pswd_widget.setEnabled(False)
        self.pswd_line.setText('')

    def send_code(self):
        response = try_to_send_code(self.phone_line.text())
        if type(response) == str:
            self.phone_error_label.setText(response)
        else:
            self.phone_error_label.setText('')
            self.client = response
            self.code_line.setEnabled(True)
            self.code_line.setText('')

    def check_code_line(self):
        if self.code_line.text():
            self.add_akk_btn.setEnabled(True)
        else:
            self.add_akk_btn.setEnabled(False)
        self.code_error_label.setText('')
        self.pswd_widget.setEnabled(False)
        self.pswd_line.setText('')

    def add_akk(self):
        if not self.pswd_widget.isEnabled():
            response = code_checker(self.client, self.code_line.text())
            if response == 'ok':
                self.close()
            elif type(response) == str:
                self.code_error_label.setText(response)
            else:
                self.code_error_label.setText('')
                self.pswd_widget.setEnabled(True)
                self.pswd_line.setText('')
                self.phone_line.setEnabled(False)
                self.send_code_btn.setEnabled(False)
                self.code_line.setEnabled(False)
                self.add_akk_btn.setEnabled(False)
        else:
            response = password_checker(self.pswd_line.text())

    def check_pswd_line(self):
        if self.pswd_line.text():
            self.add_akk_btn.setEnabled(True)
        else:
            self.add_akk_btn.setEnabled(False)
        self.pswd_error_label.setText('')

    def clean_form(self):
        if self.client:
            self.client.disconnect()
        self.client = None
        self.phone_line.setText('')
        self.code_line.setText('')
        self.pswd_line.setText('')
        self.phone_line.setEnabled(True)
        self.send_code_btn.setEnabled(False)
        self.code_line.setEnabled(False)
        self.add_akk_btn.setEnabled(False)
        self.pswd_widget.setEnabled(False)

    # def eventFilter(self, a0: 'QObject', a1: 'QEvent') -> bool:
    #     return super().eventFilter(a0, a1)
