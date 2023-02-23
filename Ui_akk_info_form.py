from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AkkInfoForm(object):
    def setupUi(self, AkkInfoForm):
        AkkInfoForm.setObjectName("AkkInfoForm")
        AkkInfoForm.resize(350, 280)
        self.verticalLayout = QtWidgets.QVBoxLayout(AkkInfoForm)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_1 = QtWidgets.QLabel(AkkInfoForm)
        self.label_1.setAlignment(
            QtCore.Qt.AlignRight
            | QtCore.Qt.AlignTrailing
            | QtCore.Qt.AlignVCenter
        )
        self.label_1.setObjectName("label_1")
        self.horizontalLayout.addWidget(self.label_1)
        self.phone_label = QtWidgets.QLabel(AkkInfoForm)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.phone_label.setFont(font)
        self.phone_label.setStyleSheet("")
        self.phone_label.setText("")
        self.phone_label.setObjectName("phone_label")
        self.horizontalLayout.addWidget(self.phone_label)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(AkkInfoForm)
        self.label_3.setAlignment(
            QtCore.Qt.AlignRight
            | QtCore.Qt.AlignTrailing
            | QtCore.Qt.AlignVCenter
        )
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.status_label = QtWidgets.QLabel(AkkInfoForm)
        self.status_label.setStyleSheet("")
        self.status_label.setText("")
        self.status_label.setObjectName("status_label")
        self.horizontalLayout_2.addWidget(self.status_label)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.error_label = QtWidgets.QLabel(AkkInfoForm)
        self.error_label.setStyleSheet("color: red")
        self.error_label.setText("")
        self.error_label.setAlignment(QtCore.Qt.AlignCenter)
        self.error_label.setObjectName("error_label")
        self.verticalLayout.addWidget(self.error_label)
        spacerItem = QtWidgets.QSpacerItem(
            20,
            40,
            QtWidgets.QSizePolicy.Minimum,
            QtWidgets.QSizePolicy.Expanding,
        )
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.cancel_btn = QtWidgets.QPushButton(AkkInfoForm)
        self.cancel_btn.setObjectName("cancel_btn")
        self.horizontalLayout_3.addWidget(self.cancel_btn)
        self.check_status_btn = QtWidgets.QPushButton(AkkInfoForm)
        self.check_status_btn.setObjectName("check_status_btn")
        self.horizontalLayout_3.addWidget(self.check_status_btn)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.retranslateUi(AkkInfoForm)
        QtCore.QMetaObject.connectSlotsByName(AkkInfoForm)

    def retranslateUi(self, AkkInfoForm):
        _translate = QtCore.QCoreApplication.translate
        AkkInfoForm.setWindowTitle(_translate("AkkInfoForm", "Аккаунт"))
        self.label_1.setText(_translate("AkkInfoForm", "Номер телефона:"))
        self.label_3.setText(_translate("AkkInfoForm", "Статус:"))
        self.cancel_btn.setText(_translate("AkkInfoForm", "Назад"))
        self.check_status_btn.setText(
            _translate("AkkInfoForm", "Проверить статус")
        )
