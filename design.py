# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uxdesign.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(502, 586)
        Form.setMinimumSize(QtCore.QSize(502, 586))
        Form.setMaximumSize(QtCore.QSize(504, 586))
        Form.setBaseSize(QtCore.QSize(502, 586))
        Form.setFocusPolicy(QtCore.Qt.NoFocus)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("wifi_PNG12.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_1 = QtWidgets.QWidget()
        self.tab_1.setObjectName("tab_1")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab_1)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox = QtWidgets.QGroupBox(self.tab_1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setBaseSize(QtCore.QSize(458, 257))
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setStyleSheet("background-color: rgb(157, 216, 255);")
        self.label.setFrameShape(QtWidgets.QFrame.Panel)
        self.label.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.comboBox_1 = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_1.setObjectName("comboBox_1")
        self.gridLayout_2.addWidget(self.comboBox_1, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setStyleSheet("background-color: rgb(157, 216, 255);")
        self.label_2.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)
        self.comboBox_2 = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_2.setObjectName("comboBox_2")
        self.gridLayout_2.addWidget(self.comboBox_2, 1, 1, 1, 1)
        self.pushButton_1 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_1.setObjectName("pushButton_1")
        self.gridLayout_2.addWidget(self.pushButton_1, 2, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_2.addWidget(self.pushButton_2, 2, 1, 1, 1)
        self.P_REFRESH = QtWidgets.QPushButton(self.groupBox)
        self.P_REFRESH.setObjectName("P_REFRESH")
        self.gridLayout_2.addWidget(self.P_REFRESH, 3, 0, 1, 1)
        self.horizontalLayout_2.addLayout(self.gridLayout_2)
        self.groupBox_4 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.textBrowser_1 = QtWidgets.QTextBrowser(self.groupBox_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser_1.sizePolicy().hasHeightForWidth())
        self.textBrowser_1.setSizePolicy(sizePolicy)
        self.textBrowser_1.setMinimumSize(QtCore.QSize(209, 146))
        self.textBrowser_1.setBaseSize(QtCore.QSize(209, 146))
        self.textBrowser_1.setObjectName("textBrowser_1")
        self.verticalLayout_4.addWidget(self.textBrowser_1)
        self.horizontalLayout_2.addWidget(self.groupBox_4)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_1)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.L_ATGMR = QtWidgets.QLabel(self.groupBox_2)
        self.L_ATGMR.setStyleSheet("background-color: rgb(157, 216, 255);")
        self.L_ATGMR.setFrameShape(QtWidgets.QFrame.Panel)
        self.L_ATGMR.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.L_ATGMR.setAlignment(QtCore.Qt.AlignCenter)
        self.L_ATGMR.setObjectName("L_ATGMR")
        self.gridLayout.addWidget(self.L_ATGMR, 1, 0, 1, 1)
        self.L_AT = QtWidgets.QLabel(self.groupBox_2)
        self.L_AT.setStyleSheet("background-color: rgb(157, 216, 255);")
        self.L_AT.setFrameShape(QtWidgets.QFrame.Panel)
        self.L_AT.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.L_AT.setAlignment(QtCore.Qt.AlignCenter)
        self.L_AT.setObjectName("L_AT")
        self.gridLayout.addWidget(self.L_AT, 0, 0, 1, 1)
        self.L_ATRST = QtWidgets.QLabel(self.groupBox_2)
        self.L_ATRST.setStyleSheet("background-color: rgb(157, 216, 255);")
        self.L_ATRST.setFrameShape(QtWidgets.QFrame.Panel)
        self.L_ATRST.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.L_ATRST.setAlignment(QtCore.Qt.AlignCenter)
        self.L_ATRST.setObjectName("L_ATRST")
        self.gridLayout.addWidget(self.L_ATRST, 2, 0, 1, 1)
        self.L_ATCWLAP = QtWidgets.QLabel(self.groupBox_2)
        self.L_ATCWLAP.setStyleSheet("background-color: rgb(157, 216, 255);")
        self.L_ATCWLAP.setFrameShape(QtWidgets.QFrame.Panel)
        self.L_ATCWLAP.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.L_ATCWLAP.setAlignment(QtCore.Qt.AlignCenter)
        self.L_ATCWLAP.setObjectName("L_ATCWLAP")
        self.gridLayout.addWidget(self.L_ATCWLAP, 3, 0, 1, 1)
        self.P_ATCWJAPE = QtWidgets.QPushButton(self.groupBox_2)
        self.P_ATCWJAPE.setObjectName("P_ATCWJAPE")
        self.gridLayout.addWidget(self.P_ATCWJAPE, 5, 3, 1, 1)
        self.L_ATCWJAPQ = QtWidgets.QLabel(self.groupBox_2)
        self.L_ATCWJAPQ.setStyleSheet("background-color: rgb(157, 216, 255);")
        self.L_ATCWJAPQ.setFrameShape(QtWidgets.QFrame.Panel)
        self.L_ATCWJAPQ.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.L_ATCWJAPQ.setAlignment(QtCore.Qt.AlignCenter)
        self.L_ATCWJAPQ.setObjectName("L_ATCWJAPQ")
        self.gridLayout.addWidget(self.L_ATCWJAPQ, 4, 0, 1, 1)
        self.B_ATCWJAP_1 = QtWidgets.QLineEdit(self.groupBox_2)
        self.B_ATCWJAP_1.setObjectName("B_ATCWJAP_1")
        self.gridLayout.addWidget(self.B_ATCWJAP_1, 5, 1, 1, 1)
        self.L_ATCWJAPE = QtWidgets.QLabel(self.groupBox_2)
        self.L_ATCWJAPE.setStyleSheet("background-color: rgb(157, 216, 255);")
        self.L_ATCWJAPE.setFrameShape(QtWidgets.QFrame.Panel)
        self.L_ATCWJAPE.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.L_ATCWJAPE.setAlignment(QtCore.Qt.AlignCenter)
        self.L_ATCWJAPE.setObjectName("L_ATCWJAPE")
        self.gridLayout.addWidget(self.L_ATCWJAPE, 5, 0, 1, 1)
        self.B_ATCWJAP_2 = QtWidgets.QLineEdit(self.groupBox_2)
        self.B_ATCWJAP_2.setObjectName("B_ATCWJAP_2")
        self.gridLayout.addWidget(self.B_ATCWJAP_2, 5, 2, 1, 1)
        self.P_ATCWJAPQ = QtWidgets.QPushButton(self.groupBox_2)
        self.P_ATCWJAPQ.setObjectName("P_ATCWJAPQ")
        self.gridLayout.addWidget(self.P_ATCWJAPQ, 4, 1, 1, 1)
        self.P_ATCWLAP = QtWidgets.QPushButton(self.groupBox_2)
        self.P_ATCWLAP.setObjectName("P_ATCWLAP")
        self.gridLayout.addWidget(self.P_ATCWLAP, 3, 1, 1, 1)
        self.P_ATRST = QtWidgets.QPushButton(self.groupBox_2)
        self.P_ATRST.setObjectName("P_ATRST")
        self.gridLayout.addWidget(self.P_ATRST, 2, 1, 1, 1)
        self.P_ATGMR = QtWidgets.QPushButton(self.groupBox_2)
        self.P_ATGMR.setObjectName("P_ATGMR")
        self.gridLayout.addWidget(self.P_ATGMR, 1, 1, 1, 1)
        self.P_AT = QtWidgets.QPushButton(self.groupBox_2)
        self.P_AT.setObjectName("P_AT")
        self.gridLayout.addWidget(self.P_AT, 0, 1, 1, 1)
        self.verticalLayout_7.addLayout(self.gridLayout)
        self.verticalLayout_3.addWidget(self.groupBox_2)
        self.tabWidget.addTab(self.tab_1, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setEnabled(True)
        self.tab_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser_2.sizePolicy().hasHeightForWidth())
        self.textBrowser_2.setSizePolicy(sizePolicy)
        self.textBrowser_2.setBaseSize(QtCore.QSize(300, 300))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.verticalLayout_6.addWidget(self.textBrowser_2)
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.B_ATCWSAP_2 = QtWidgets.QLineEdit(self.groupBox_3)
        self.B_ATCWSAP_2.setObjectName("B_ATCWSAP_2")
        self.gridLayout_5.addWidget(self.B_ATCWSAP_2, 1, 2, 1, 1)
        self.B_ATCIPSEND_1 = QtWidgets.QLineEdit(self.groupBox_3)
        self.B_ATCIPSEND_1.setObjectName("B_ATCIPSEND_1")
        self.gridLayout_5.addWidget(self.B_ATCIPSEND_1, 6, 1, 1, 1)
        self.B_ATCIPSTART_2 = QtWidgets.QLineEdit(self.groupBox_3)
        self.B_ATCIPSTART_2.setObjectName("B_ATCIPSTART_2")
        self.gridLayout_5.addWidget(self.B_ATCIPSTART_2, 5, 2, 1, 1)
        self.P_ATCIPSTART = QtWidgets.QPushButton(self.groupBox_3)
        self.P_ATCIPSTART.setObjectName("P_ATCIPSTART")
        self.gridLayout_5.addWidget(self.P_ATCIPSTART, 5, 4, 1, 1)
        self.P_ATCWSAPE = QtWidgets.QPushButton(self.groupBox_3)
        self.P_ATCWSAPE.setObjectName("P_ATCWSAPE")
        self.gridLayout_5.addWidget(self.P_ATCWSAPE, 1, 3, 1, 1)
        self.B_ATCIPSTART_3 = QtWidgets.QLineEdit(self.groupBox_3)
        self.B_ATCIPSTART_3.setObjectName("B_ATCIPSTART_3")
        self.gridLayout_5.addWidget(self.B_ATCIPSTART_3, 5, 3, 1, 1)
        self.P_ATCWSAPQ = QtWidgets.QPushButton(self.groupBox_3)
        self.P_ATCWSAPQ.setObjectName("P_ATCWSAPQ")
        self.gridLayout_5.addWidget(self.P_ATCWSAPQ, 0, 1, 1, 1)
        self.L_ATCWSAPE = QtWidgets.QLabel(self.groupBox_3)
        self.L_ATCWSAPE.setStyleSheet("background-color: rgb(157, 216, 255);")
        self.L_ATCWSAPE.setFrameShape(QtWidgets.QFrame.Panel)
        self.L_ATCWSAPE.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.L_ATCWSAPE.setAlignment(QtCore.Qt.AlignCenter)
        self.L_ATCWSAPE.setObjectName("L_ATCWSAPE")
        self.gridLayout_5.addWidget(self.L_ATCWSAPE, 1, 0, 1, 1)
        self.P_ATCIPSTATUS = QtWidgets.QPushButton(self.groupBox_3)
        self.P_ATCIPSTATUS.setObjectName("P_ATCIPSTATUS")
        self.gridLayout_5.addWidget(self.P_ATCIPSTATUS, 4, 1, 1, 1)
        self.L_ATCWSAPQ = QtWidgets.QLabel(self.groupBox_3)
        self.L_ATCWSAPQ.setStyleSheet("background-color: rgb(157, 216, 255);")
        self.L_ATCWSAPQ.setFrameShape(QtWidgets.QFrame.Panel)
        self.L_ATCWSAPQ.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.L_ATCWSAPQ.setAlignment(QtCore.Qt.AlignCenter)
        self.L_ATCWSAPQ.setObjectName("L_ATCWSAPQ")
        self.gridLayout_5.addWidget(self.L_ATCWSAPQ, 0, 0, 1, 1)
        self.L_ATCIPSTART = QtWidgets.QLabel(self.groupBox_3)
        self.L_ATCIPSTART.setStyleSheet("background-color: rgb(157, 216, 255);")
        self.L_ATCIPSTART.setFrameShape(QtWidgets.QFrame.Panel)
        self.L_ATCIPSTART.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.L_ATCIPSTART.setAlignment(QtCore.Qt.AlignCenter)
        self.L_ATCIPSTART.setObjectName("L_ATCIPSTART")
        self.gridLayout_5.addWidget(self.L_ATCIPSTART, 5, 0, 1, 1)
        self.L_ATCIPSTATUS = QtWidgets.QLabel(self.groupBox_3)
        self.L_ATCIPSTATUS.setStyleSheet("background-color: rgb(157, 216, 255);")
        self.L_ATCIPSTATUS.setFrameShape(QtWidgets.QFrame.Panel)
        self.L_ATCIPSTATUS.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.L_ATCIPSTATUS.setAlignment(QtCore.Qt.AlignCenter)
        self.L_ATCIPSTATUS.setObjectName("L_ATCIPSTATUS")
        self.gridLayout_5.addWidget(self.L_ATCIPSTATUS, 4, 0, 1, 1)
        self.L_ATCIPSEND = QtWidgets.QLabel(self.groupBox_3)
        self.L_ATCIPSEND.setStyleSheet("background-color: rgb(157, 216, 255);")
        self.L_ATCIPSEND.setFrameShape(QtWidgets.QFrame.Panel)
        self.L_ATCIPSEND.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.L_ATCIPSEND.setAlignment(QtCore.Qt.AlignCenter)
        self.L_ATCIPSEND.setObjectName("L_ATCIPSEND")
        self.gridLayout_5.addWidget(self.L_ATCIPSEND, 6, 0, 1, 1)
        self.L_ATCIFSR = QtWidgets.QLabel(self.groupBox_3)
        self.L_ATCIFSR.setStyleSheet("background-color: rgb(157, 216, 255);")
        self.L_ATCIFSR.setFrameShape(QtWidgets.QFrame.Panel)
        self.L_ATCIFSR.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.L_ATCIFSR.setAlignment(QtCore.Qt.AlignCenter)
        self.L_ATCIFSR.setObjectName("L_ATCIFSR")
        self.gridLayout_5.addWidget(self.L_ATCIFSR, 3, 0, 1, 1)
        self.B_ATCWSAP_1 = QtWidgets.QLineEdit(self.groupBox_3)
        self.B_ATCWSAP_1.setObjectName("B_ATCWSAP_1")
        self.gridLayout_5.addWidget(self.B_ATCWSAP_1, 1, 1, 1, 1)
        self.P_ATCIFSR = QtWidgets.QPushButton(self.groupBox_3)
        self.P_ATCIFSR.setObjectName("P_ATCIFSR")
        self.gridLayout_5.addWidget(self.P_ATCIFSR, 3, 1, 1, 1)
        self.P_ATCWQAP = QtWidgets.QPushButton(self.groupBox_3)
        self.P_ATCWQAP.setObjectName("P_ATCWQAP")
        self.gridLayout_5.addWidget(self.P_ATCWQAP, 2, 1, 1, 1)
        self.P_ATCIPSEND = QtWidgets.QPushButton(self.groupBox_3)
        self.P_ATCIPSEND.setObjectName("P_ATCIPSEND")
        self.gridLayout_5.addWidget(self.P_ATCIPSEND, 6, 2, 1, 1)
        self.L_ATCWQAP = QtWidgets.QLabel(self.groupBox_3)
        self.L_ATCWQAP.setStyleSheet("background-color: rgb(157, 216, 255);")
        self.L_ATCWQAP.setFrameShape(QtWidgets.QFrame.Panel)
        self.L_ATCWQAP.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.L_ATCWQAP.setAlignment(QtCore.Qt.AlignCenter)
        self.L_ATCWQAP.setObjectName("L_ATCWQAP")
        self.gridLayout_5.addWidget(self.L_ATCWQAP, 2, 0, 1, 1)
        self.B_ATCIPSTART_1 = QtWidgets.QLineEdit(self.groupBox_3)
        self.B_ATCIPSTART_1.setObjectName("B_ATCIPSTART_1")
        self.gridLayout_5.addWidget(self.B_ATCIPSTART_1, 5, 1, 1, 1)
        self.P_ATCWMODEQ = QtWidgets.QPushButton(self.groupBox_3)
        self.P_ATCWMODEQ.setObjectName("P_ATCWMODEQ")
        self.gridLayout_5.addWidget(self.P_ATCWMODEQ, 7, 1, 1, 1)
        self.L_ATCWMODEQ = QtWidgets.QLabel(self.groupBox_3)
        self.L_ATCWMODEQ.setStyleSheet("background-color: rgb(157, 216, 255);")
        self.L_ATCWMODEQ.setFrameShape(QtWidgets.QFrame.Panel)
        self.L_ATCWMODEQ.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.L_ATCWMODEQ.setAlignment(QtCore.Qt.AlignCenter)
        self.L_ATCWMODEQ.setObjectName("L_ATCWMODEQ")
        self.gridLayout_5.addWidget(self.L_ATCWMODEQ, 7, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.groupBox_3)
        self.label_4.setStyleSheet("background-color: rgb(157, 216, 255);")
        self.label_4.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout_5.addWidget(self.label_4, 8, 0, 1, 1)
        self.P_ATCWMODEE = QtWidgets.QPushButton(self.groupBox_3)
        self.P_ATCWMODEE.setObjectName("P_ATCWMODEE")
        self.gridLayout_5.addWidget(self.P_ATCWMODEE, 8, 2, 1, 1)
        self.B_ATCWMODE_1 = QtWidgets.QLineEdit(self.groupBox_3)
        self.B_ATCWMODE_1.setObjectName("B_ATCWMODE_1")
        self.gridLayout_5.addWidget(self.B_ATCWMODE_1, 8, 1, 1, 1)
        self.verticalLayout_6.addLayout(self.gridLayout_5)
        self.verticalLayout.addWidget(self.groupBox_3)
        self.tabWidget.addTab(self.tab_2, "")
        self.horizontalLayout.addWidget(self.tabWidget)

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.comboBox_1, self.comboBox_2)
        Form.setTabOrder(self.comboBox_2, self.pushButton_1)
        Form.setTabOrder(self.pushButton_1, self.pushButton_2)
        Form.setTabOrder(self.pushButton_2, self.P_REFRESH)
        Form.setTabOrder(self.P_REFRESH, self.textBrowser_1)
        Form.setTabOrder(self.textBrowser_1, self.tabWidget)
        Form.setTabOrder(self.tabWidget, self.textBrowser_2)
        Form.setTabOrder(self.textBrowser_2, self.P_ATCWSAPQ)
        Form.setTabOrder(self.P_ATCWSAPQ, self.B_ATCWSAP_1)
        Form.setTabOrder(self.B_ATCWSAP_1, self.B_ATCWSAP_2)
        Form.setTabOrder(self.B_ATCWSAP_2, self.P_ATCWSAPE)
        Form.setTabOrder(self.P_ATCWSAPE, self.P_ATCWQAP)
        Form.setTabOrder(self.P_ATCWQAP, self.P_ATCIFSR)
        Form.setTabOrder(self.P_ATCIFSR, self.P_ATCIPSTATUS)
        Form.setTabOrder(self.P_ATCIPSTATUS, self.B_ATCIPSTART_1)
        Form.setTabOrder(self.B_ATCIPSTART_1, self.B_ATCIPSTART_2)
        Form.setTabOrder(self.B_ATCIPSTART_2, self.B_ATCIPSTART_3)
        Form.setTabOrder(self.B_ATCIPSTART_3, self.P_ATCIPSTART)
        Form.setTabOrder(self.P_ATCIPSTART, self.B_ATCIPSEND_1)
        Form.setTabOrder(self.B_ATCIPSEND_1, self.P_ATCIPSEND)
        Form.setTabOrder(self.P_ATCIPSEND, self.P_ATCWMODEQ)
        Form.setTabOrder(self.P_ATCWMODEQ, self.B_ATCWMODE_1)
        Form.setTabOrder(self.B_ATCWMODE_1, self.P_ATCWMODEE)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Esp8266Debugger"))
        self.groupBox.setTitle(_translate("Form", "Serial Port Setup"))
        self.label.setText(_translate("Form", "  Port  "))
        self.label_2.setText(_translate("Form", "  Baud  "))
        self.pushButton_1.setText(_translate("Form", "Connect"))
        self.pushButton_2.setText(_translate("Form", "Disconnect"))
        self.P_REFRESH.setText(_translate("Form", "Refresh"))
        self.groupBox_4.setTitle(_translate("Form", "Messages"))
        self.textBrowser_1.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:5pt;\"><br /></p></body></html>"))
        self.groupBox_2.setTitle(_translate("Form", "Basic Commands"))
        self.L_ATGMR.setText(_translate("Form", "AT+GMR"))
        self.L_AT.setText(_translate("Form", "AT"))
        self.L_ATRST.setText(_translate("Form", "AT+RST"))
        self.L_ATCWLAP.setText(_translate("Form", "AT+CWLAP"))
        self.P_ATCWJAPE.setText(_translate("Form", "OK"))
        self.L_ATCWJAPQ.setText(_translate("Form", "AT+CWJAP?"))
        self.L_ATCWJAPE.setText(_translate("Form", "AT+CWJAP="))
        self.P_ATCWJAPQ.setText(_translate("Form", "OK"))
        self.P_ATCWLAP.setText(_translate("Form", "OK"))
        self.P_ATRST.setText(_translate("Form", "OK"))
        self.P_ATGMR.setText(_translate("Form", "OK"))
        self.P_AT.setText(_translate("Form", "OK"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), _translate("Form", "General"))
        self.groupBox_3.setTitle(_translate("Form", "Advanced Commands"))
        self.P_ATCIPSTART.setText(_translate("Form", "OK"))
        self.P_ATCWSAPE.setText(_translate("Form", "OK"))
        self.P_ATCWSAPQ.setText(_translate("Form", "OK"))
        self.L_ATCWSAPE.setText(_translate("Form", "AT+CWSAP="))
        self.P_ATCIPSTATUS.setText(_translate("Form", "OK"))
        self.L_ATCWSAPQ.setText(_translate("Form", "AT+CWSAP?"))
        self.L_ATCIPSTART.setText(_translate("Form", "AT+CIPSTART"))
        self.L_ATCIPSTATUS.setText(_translate("Form", "AT+CIPSTATUS"))
        self.L_ATCIPSEND.setText(_translate("Form", "AT+CIPSEND"))
        self.L_ATCIFSR.setText(_translate("Form", "AT+CIFSR"))
        self.P_ATCIFSR.setText(_translate("Form", "OK"))
        self.P_ATCWQAP.setText(_translate("Form", "OK"))
        self.P_ATCIPSEND.setText(_translate("Form", "OK"))
        self.L_ATCWQAP.setText(_translate("Form", "AT+CWQAP"))
        self.P_ATCWMODEQ.setText(_translate("Form", "OK"))
        self.L_ATCWMODEQ.setText(_translate("Form", "AT+CWMODE?"))
        self.label_4.setText(_translate("Form", "AT+CWMODE="))
        self.P_ATCWMODEE.setText(_translate("Form", "OK"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "Advanced"))

