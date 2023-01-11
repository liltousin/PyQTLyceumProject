from sqlite3 import Connection

from PyQt5.QtWidgets import QListWidgetItem, QWidget

from akk_status_funcs import check_akk_status, check_ban_status
from sql_functions import set_akk_status
from status_colors import STATUS_COLORS, get_status_from_color
from Ui_akk_info_form import Ui_AkkInfoForm


class AkkInfoForm(QWidget, Ui_AkkInfoForm):
    def __init__(self, con: Connection) -> None:
        super().__init__()
        self.setupUi(self)
        self.connection = con
        self.cancel_btn.clicked.connect(self.close)
        self.check_status_btn.clicked.connect(self.check_status)

    def check_status(self):
        self.error_label.setText('')
        try:
            if self.status_label.text() == 'banned':
                status = check_ban_status(self.phone_label.text())
            else:
                status = check_akk_status(self.phone_label.text())
            set_akk_status(self.connection, status, self.phone_label.text())
            self.status_label.setText(status)
            self.status_label.setStyleSheet(
                f'color: {STATUS_COLORS[status].name()}'
            )
        except ConnectionError:
            self.error_label.setText('Нет подключения к интернету!')

    def set_akk(self, akk: QListWidgetItem):
        self.error_label.setText('')
        self.phone_label.setText(akk.text())
        color = akk.background().color()
        status = get_status_from_color(color)
        self.status_label.setText(status)
        self.status_label.setStyleSheet(f'color: {color.name()}')
        self.show()
