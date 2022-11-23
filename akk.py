from PyQt5.QtWidgets import QListWidgetItem


class Akk(QListWidgetItem):
    def __init__(self, phone, *args, **kwargs) -> None:
        super().__init__(phone, *args, **kwargs)
        self.phone = phone
