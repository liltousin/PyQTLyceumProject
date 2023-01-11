from sqlite3 import Connection

from PyQt5.QtWidgets import QListWidgetItem, QWidget

from akk_status_funcs import check_akk_status, check_nofile_status
from sql_functions import set_akk_status
from Ui_auth_akk_form import Ui_AuthAkkForm


class AuthAkkForm(QWidget, Ui_AuthAkkForm):
    def __init__(self, con: Connection) -> None:
        super().__init__()
        self.setupUi(self)
        self.connection = con
        self.client = None
        self.endflag = False
        self.cancel_btn.clicked.connect(self.close)
        # self.send_code_btn.clicked.connect(self.send_code)
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
