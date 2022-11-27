from PyQt5 import QtCore, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(660, 500)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        spacerItem = QtWidgets.QSpacerItem(
            40,
            20,
            QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Minimum,
        )
        self.horizontalLayout_9.addItem(spacerItem)
        self.task_label = QtWidgets.QLabel(self.centralwidget)
        self.task_label.setTextFormat(QtCore.Qt.AutoText)
        self.task_label.setAlignment(QtCore.Qt.AlignCenter)
        self.task_label.setObjectName("task_label")
        self.horizontalLayout_9.addWidget(self.task_label)
        spacerItem1 = QtWidgets.QSpacerItem(
            40,
            20,
            QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Minimum,
        )
        self.horizontalLayout_9.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.add_task_btn = QtWidgets.QPushButton(self.centralwidget)
        self.add_task_btn.setObjectName("add_task_btn")
        self.horizontalLayout_6.addWidget(self.add_task_btn)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.list_of_task_widget = QtWidgets.QListWidget(self.centralwidget)
        self.list_of_task_widget.setMinimumSize(QtCore.QSize(0, 0))
        self.list_of_task_widget.setObjectName("list_of_task_widget")
        self.verticalLayout.addWidget(self.list_of_task_widget)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem2 = QtWidgets.QSpacerItem(
            40,
            20,
            QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Minimum,
        )
        self.horizontalLayout_8.addItem(spacerItem2)
        self.import_tasks_btn = QtWidgets.QPushButton(self.centralwidget)
        self.import_tasks_btn.setObjectName("import_tasks_btn")
        self.horizontalLayout_8.addWidget(self.import_tasks_btn)
        self.export_tasks_btn = QtWidgets.QPushButton(self.centralwidget)
        self.export_tasks_btn.setEnabled(False)
        self.export_tasks_btn.setObjectName("export_tasks_btn")
        self.horizontalLayout_8.addWidget(self.export_tasks_btn)
        spacerItem3 = QtWidgets.QSpacerItem(
            40,
            20,
            QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Minimum,
        )
        self.horizontalLayout_8.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        spacerItem4 = QtWidgets.QSpacerItem(
            40,
            20,
            QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Minimum,
        )
        self.horizontalLayout_10.addItem(spacerItem4)
        self.akks_label = QtWidgets.QLabel(self.centralwidget)
        self.akks_label.setAlignment(QtCore.Qt.AlignCenter)
        self.akks_label.setObjectName("akks_label")
        self.horizontalLayout_10.addWidget(self.akks_label)
        spacerItem5 = QtWidgets.QSpacerItem(
            40,
            20,
            QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Minimum,
        )
        self.horizontalLayout_10.addItem(spacerItem5)
        self.verticalLayout_2.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.add_akk_btn = QtWidgets.QPushButton(self.centralwidget)
        self.add_akk_btn.setObjectName("add_akk_btn")
        self.horizontalLayout_3.addWidget(self.add_akk_btn)
        self.del_nwork_akks_btn = QtWidgets.QPushButton(self.centralwidget)
        self.del_nwork_akks_btn.setEnabled(False)
        self.del_nwork_akks_btn.setObjectName("del_nwork_akks_btn")
        self.horizontalLayout_3.addWidget(self.del_nwork_akks_btn)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.list_of_akks_widget = QtWidgets.QListWidget(self.centralwidget)
        self.list_of_akks_widget.setMinimumSize(QtCore.QSize(0, 0))
        self.list_of_akks_widget.setEditTriggers(
            QtWidgets.QAbstractItemView.DoubleClicked
            | QtWidgets.QAbstractItemView.EditKeyPressed
        )
        self.list_of_akks_widget.setObjectName("list_of_akks_widget")
        self.verticalLayout_2.addWidget(self.list_of_akks_widget)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem6 = QtWidgets.QSpacerItem(
            40,
            20,
            QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Minimum,
        )
        self.horizontalLayout_2.addItem(spacerItem6)
        self.import_akks_btn = QtWidgets.QPushButton(self.centralwidget)
        self.import_akks_btn.setObjectName("import_akks_btn")
        self.horizontalLayout_2.addWidget(self.import_akks_btn)
        self.export_akks_btn = QtWidgets.QPushButton(self.centralwidget)
        self.export_akks_btn.setEnabled(False)
        self.export_akks_btn.setObjectName("export_akks_btn")
        self.horizontalLayout_2.addWidget(self.export_akks_btn)
        spacerItem7 = QtWidgets.QSpacerItem(
            40,
            20,
            QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Minimum,
        )
        self.horizontalLayout_2.addItem(spacerItem7)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.run_tasks_btn = QtWidgets.QPushButton(self.centralwidget)
        self.run_tasks_btn.setObjectName("run_tasks_btn")
        self.horizontalLayout_5.addWidget(self.run_tasks_btn)
        self.stop_tasks_btn = QtWidgets.QPushButton(self.centralwidget)
        self.stop_tasks_btn.setEnabled(False)
        self.stop_tasks_btn.setObjectName("stop_tasks_btn")
        self.horizontalLayout_5.addWidget(self.stop_tasks_btn)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(
            _translate("MainWindow", "Рассылка по чатам")
        )
        self.task_label.setText(_translate("MainWindow", "Список тасков"))
        self.add_task_btn.setText(_translate("MainWindow", "Добавить"))
        self.import_tasks_btn.setText(
            _translate("MainWindow", "Импортировать")
        )
        self.export_tasks_btn.setText(
            _translate("MainWindow", "Экспортировать")
        )
        self.akks_label.setText(_translate("MainWindow", "Список аккаунтов"))
        self.add_akk_btn.setText(_translate("MainWindow", "Добавить"))
        self.del_nwork_akks_btn.setText(
            _translate("MainWindow", "Удалить нерабочие")
        )
        self.import_akks_btn.setText(_translate("MainWindow", "Импортировать"))
        self.export_akks_btn.setText(
            _translate("MainWindow", "Экспортировать")
        )
        self.run_tasks_btn.setText(_translate("MainWindow", "Запуск"))
        self.stop_tasks_btn.setText(_translate("MainWindow", "Стоп"))
