from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AddAkkForm(object):
    def setupUi(self, AddAkkForm):
        AddAkkForm.setObjectName("AddAkkForm")
        AddAkkForm.resize(400, 350)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(AddAkkForm)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.phone_label = QtWidgets.QLabel(AddAkkForm)
        self.phone_label.setObjectName("phone_label")
        self.verticalLayout_5.addWidget(self.phone_label)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.phone_line = QtWidgets.QLineEdit(AddAkkForm)
        self.phone_line.setMinimumSize(QtCore.QSize(0, 0))
        self.phone_line.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.phone_line.setText("")
        self.phone_line.setObjectName("phone_line")
        self.horizontalLayout_2.addWidget(self.phone_line)
        self.send_code_btn = QtWidgets.QPushButton(AddAkkForm)
        self.send_code_btn.setEnabled(False)
        self.send_code_btn.setObjectName("send_code_btn")
        self.horizontalLayout_2.addWidget(self.send_code_btn)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.phone_error_label = QtWidgets.QLabel(AddAkkForm)
        self.phone_error_label.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.phone_error_label.setFont(font)
        self.phone_error_label.setMouseTracking(True)
        self.phone_error_label.setStyleSheet("color : red;")
        self.phone_error_label.setMidLineWidth(0)
        self.phone_error_label.setText("")
        self.phone_error_label.setTextFormat(QtCore.Qt.RichText)
        self.phone_error_label.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.phone_error_label.setObjectName("phone_error_label")
        self.verticalLayout.addWidget(self.phone_error_label)
        self.verticalLayout_5.addLayout(self.verticalLayout)
        self.code_label = QtWidgets.QLabel(AddAkkForm)
        self.code_label.setObjectName("code_label")
        self.verticalLayout_5.addWidget(self.code_label)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.code_line = QtWidgets.QLineEdit(AddAkkForm)
        self.code_line.setEnabled(False)
        self.code_line.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.code_line.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.code_line.setText("")
        self.code_line.setObjectName("code_line")
        self.verticalLayout_3.addWidget(self.code_line)
        self.code_error_label = QtWidgets.QLabel(AddAkkForm)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.code_error_label.setFont(font)
        self.code_error_label.setStyleSheet("color : red;")
        self.code_error_label.setText("")
        self.code_error_label.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.code_error_label.setObjectName("code_error_label")
        self.verticalLayout_3.addWidget(self.code_error_label)
        self.verticalLayout_5.addLayout(self.verticalLayout_3)
        self.pswd_widget = QtWidgets.QWidget(AddAkkForm)
        self.pswd_widget.setEnabled(True)
        self.pswd_widget.setObjectName("pswd_widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.pswd_widget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pswd_label = QtWidgets.QLabel(self.pswd_widget)
        self.pswd_label.setEnabled(True)
        self.pswd_label.setObjectName("pswd_label")
        self.verticalLayout_2.addWidget(self.pswd_label)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.pswd_line = QtWidgets.QLineEdit(self.pswd_widget)
        self.pswd_line.setEnabled(True)
        self.pswd_line.setObjectName("pswd_line")
        self.verticalLayout_4.addWidget(self.pswd_line)
        self.pswd_error_label = QtWidgets.QLabel(self.pswd_widget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pswd_error_label.setFont(font)
        self.pswd_error_label.setStyleSheet("color : red;")
        self.pswd_error_label.setText("")
        self.pswd_error_label.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.pswd_error_label.setObjectName("pswd_error_label")
        self.verticalLayout_4.addWidget(self.pswd_error_label)
        self.verticalLayout_2.addLayout(self.verticalLayout_4)
        self.verticalLayout_5.addWidget(self.pswd_widget)
        spacerItem = QtWidgets.QSpacerItem(
            20,
            40,
            QtWidgets.QSizePolicy.Minimum,
            QtWidgets.QSizePolicy.Expanding,
        )
        self.verticalLayout_5.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.cancel_btn = QtWidgets.QPushButton(AddAkkForm)
        self.cancel_btn.setMinimumSize(QtCore.QSize(156, 0))
        self.cancel_btn.setObjectName("cancel_btn")
        self.horizontalLayout.addWidget(self.cancel_btn)
        self.add_akk_btn = QtWidgets.QPushButton(AddAkkForm)
        self.add_akk_btn.setEnabled(False)
        self.add_akk_btn.setObjectName("add_akk_btn")
        self.horizontalLayout.addWidget(self.add_akk_btn)
        self.verticalLayout_5.addLayout(self.horizontalLayout)

        self.retranslateUi(AddAkkForm)
        QtCore.QMetaObject.connectSlotsByName(AddAkkForm)

    def retranslateUi(self, AddAkkForm):
        _translate = QtCore.QCoreApplication.translate
        AddAkkForm.setWindowTitle(_translate("AddAkkForm", "Добавить аккаунт"))
        self.phone_label.setText(_translate("AddAkkForm", "Номер телефона:"))
        self.send_code_btn.setText(_translate("AddAkkForm", "Отправить код"))
        self.code_label.setText(_translate("AddAkkForm", "Код:"))
        self.pswd_label.setText(_translate("AddAkkForm", "Пароль:"))
        self.cancel_btn.setText(_translate("AddAkkForm", "Отмена"))
        self.add_akk_btn.setText(_translate("AddAkkForm", "Добавить"))