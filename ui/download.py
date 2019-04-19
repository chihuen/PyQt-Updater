# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'download.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form_download(object):
    def setupUi(self, Form_download):
        Form_download.setObjectName("Form_download")
        Form_download.setEnabled(True)
        Form_download.resize(282, 211)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form_download.sizePolicy().hasHeightForWidth())
        Form_download.setSizePolicy(sizePolicy)
        Form_download.setMaximumSize(QtCore.QSize(282, 211))
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Form_download)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_current_version_header = QtWidgets.QLabel(Form_download)
        self.label_current_version_header.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_current_version_header.setObjectName("label_current_version_header")
        self.gridLayout.addWidget(self.label_current_version_header, 0, 0, 1, 1)
        self.label_current_version = QtWidgets.QLabel(Form_download)
        self.label_current_version.setObjectName("label_current_version")
        self.gridLayout.addWidget(self.label_current_version, 0, 1, 1, 1)
        self.label_latest_version_header = QtWidgets.QLabel(Form_download)
        self.label_latest_version_header.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_latest_version_header.setObjectName("label_latest_version_header")
        self.gridLayout.addWidget(self.label_latest_version_header, 1, 0, 1, 1)
        self.label_latest_version = QtWidgets.QLabel(Form_download)
        self.label_latest_version.setObjectName("label_latest_version")
        self.gridLayout.addWidget(self.label_latest_version, 1, 1, 1, 1)
        self.horizontalLayout_2.addLayout(self.gridLayout)
        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 7)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.plainTextEdit_update_log = QtWidgets.QPlainTextEdit(Form_download)
        self.plainTextEdit_update_log.setEnabled(True)
        self.plainTextEdit_update_log.setObjectName("plainTextEdit_update_log")
        self.verticalLayout.addWidget(self.plainTextEdit_update_log)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.pushButton_update = QtWidgets.QPushButton(Form_download)
        self.pushButton_update.setObjectName("pushButton_update")
        self.horizontalLayout.addWidget(self.pushButton_update)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.progressBar_update = QtWidgets.QProgressBar(Form_download)
        self.progressBar_update.setProperty("value", 0)
        self.progressBar_update.setObjectName("progressBar_update")
        self.verticalLayout.addWidget(self.progressBar_update)
        self.label_tips = QtWidgets.QLabel(Form_download)
        self.label_tips.setText("")
        self.label_tips.setObjectName("label_tips")
        self.verticalLayout.addWidget(self.label_tips)
        self.verticalLayout.setStretch(0, 2)
        self.verticalLayout.setStretch(2, 2)
        self.verticalLayout.setStretch(4, 1)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Form_download)
        QtCore.QMetaObject.connectSlotsByName(Form_download)

    def retranslateUi(self, Form_download):
        _translate = QtCore.QCoreApplication.translate
        Form_download.setWindowTitle(_translate("Form_download", "Update"))
        self.label_current_version_header.setText(_translate("Form_download", "Current version:"))
        self.label_current_version.setText(_translate("Form_download", "0.0.0"))
        self.label_latest_version_header.setText(_translate("Form_download", "The latest version:"))
        self.label_latest_version.setText(_translate("Form_download", "0.0.0"))
        self.pushButton_update.setText(_translate("Form_download", "Download"))


