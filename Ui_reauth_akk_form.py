from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ReauthAkkForm(object):
    def setupUi(self, ReauthAkkForm):
        ReauthAkkForm.setObjectName("ReauthAkkForm")
        ReauthAkkForm.resize(400, 300)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        ReauthAkkForm.setFont(font)
        self.verticalLayout = QtWidgets.QVBoxLayout(ReauthAkkForm)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(ReauthAkkForm)
        self.label.setAlignment(
            QtCore.Qt.AlignLeading
            | QtCore.Qt.AlignLeft
            | QtCore.Qt.AlignVCenter
        )
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.phone_label = QtWidgets.QLabel(ReauthAkkForm)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.phone_label.setFont(font)
        self.phone_label.setText("")
        self.phone_label.setAlignment(
            QtCore.Qt.AlignLeading
            | QtCore.Qt.AlignLeft
            | QtCore.Qt.AlignVCenter
        )
        self.phone_label.setObjectName("phone_label")
        self.horizontalLayout_2.addWidget(self.phone_label)
        self.empty_label = QtWidgets.QLabel(ReauthAkkForm)
        self.empty_label.setText("")
        self.empty_label.setObjectName("empty_label")
        self.horizontalLayout_2.addWidget(self.empty_label)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.code_label = QtWidgets.QLabel(ReauthAkkForm)
        self.code_label.setObjectName("code_label")
        self.verticalLayout.addWidget(self.code_label)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.code_line = QtWidgets.QLineEdit(ReauthAkkForm)
        self.code_line.setEnabled(False)
        self.code_line.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.code_line.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.code_line.setText("")
        self.code_line.setObjectName("code_line")
        self.verticalLayout_3.addWidget(self.code_line)
        self.code_error_label = QtWidgets.QLabel(ReauthAkkForm)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.code_error_label.setFont(font)
        self.code_error_label.setStyleSheet("color: red")
        self.code_error_label.setText("")
        self.code_error_label.setAlignment(
            QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop
        )
        self.code_error_label.setObjectName("code_error_label")
        self.verticalLayout_3.addWidget(self.code_error_label)
        self.verticalLayout.addLayout(self.verticalLayout_3)
        self.pswd_widget = QtWidgets.QWidget(ReauthAkkForm)
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
        self.pswd_error_label.setStyleSheet("color: red")
        self.pswd_error_label.setText("")
        self.pswd_error_label.setAlignment(
            QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop
        )
        self.pswd_error_label.setObjectName("pswd_error_label")
        self.verticalLayout_4.addWidget(self.pswd_error_label)
        self.verticalLayout_2.addLayout(self.verticalLayout_4)
        self.verticalLayout.addWidget(self.pswd_widget)
        spacerItem = QtWidgets.QSpacerItem(
            20,
            40,
            QtWidgets.QSizePolicy.Minimum,
            QtWidgets.QSizePolicy.Expanding,
        )
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.cancel_btn = QtWidgets.QPushButton(ReauthAkkForm)
        self.cancel_btn.setMinimumSize(QtCore.QSize(156, 0))
        self.cancel_btn.setObjectName("cancel_btn")
        self.horizontalLayout.addWidget(self.cancel_btn)
        self.reauth_akk_btn = QtWidgets.QPushButton(ReauthAkkForm)
        self.reauth_akk_btn.setEnabled(False)
        self.reauth_akk_btn.setObjectName("reauth_akk_btn")
        self.horizontalLayout.addWidget(self.reauth_akk_btn)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(ReauthAkkForm)
        QtCore.QMetaObject.connectSlotsByName(ReauthAkkForm)

    def retranslateUi(self, ReauthAkkForm):
        _translate = QtCore.QCoreApplication.translate
        ReauthAkkForm.setWindowTitle(
            _translate("ReauthAkkForm", "Переавторизовать аккаунт")
        )
        self.label.setText(_translate("ReauthAkkForm", "Номер телефона:"))
        self.code_label.setText(_translate("ReauthAkkForm", "Код:"))
        self.pswd_label.setText(_translate("ReauthAkkForm", "Пароль:"))
        self.cancel_btn.setText(_translate("ReauthAkkForm", "Отмена"))
        self.reauth_akk_btn.setText(
            _translate("ReauthAkkForm", "Переавторизовать")
        )
