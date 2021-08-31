# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\dev\minerva\forms\mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(803, 642)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnFromFile = QtWidgets.QPushButton(self.centralwidget)
        self.btnFromFile.setObjectName("btnFromFile")
        self.horizontalLayout.addWidget(self.btnFromFile)
        self.btnFromCb = QtWidgets.QPushButton(self.centralwidget)
        self.btnFromCb.setObjectName("btnFromCb")
        self.horizontalLayout.addWidget(self.btnFromCb)
        self.comboBoxLang = QtWidgets.QComboBox(self.centralwidget)
        self.comboBoxLang.setEditable(False)
        self.comboBoxLang.setObjectName("comboBoxLang")
        self.comboBoxLang.addItem("")
        self.comboBoxLang.addItem("")
        self.comboBoxLang.addItem("")
        self.comboBoxLang.addItem("")
        self.comboBoxLang.addItem("")
        self.horizontalLayout.addWidget(self.comboBoxLang)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setObjectName("graphicsView")
        self.horizontalLayout_2.addWidget(self.graphicsView)
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName("textBrowser")
        self.horizontalLayout_2.addWidget(self.textBrowser)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.btnCopy = QtWidgets.QPushButton(self.centralwidget)
        self.btnCopy.setObjectName("btnCopy")
        self.horizontalLayout_3.addWidget(self.btnCopy)
        self.btnSave = QtWidgets.QPushButton(self.centralwidget)
        self.btnSave.setObjectName("btnSave")
        self.horizontalLayout_3.addWidget(self.btnSave)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 803, 23))
        self.menubar.setObjectName("menubar")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionAbout_Minerva = QtWidgets.QAction(MainWindow)
        self.actionAbout_Minerva.setObjectName("actionAbout_Minerva")
        self.menuAbout.addAction(self.actionAbout_Minerva)
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        self.comboBoxLang.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Minerva - Text Getter From Pictures"))
        self.btnFromFile.setText(_translate("MainWindow", "From File"))
        self.btnFromCb.setText(_translate("MainWindow", "From Clipboard"))
        self.comboBoxLang.setItemText(0, _translate("MainWindow", "English"))
        self.comboBoxLang.setItemText(1, _translate("MainWindow", "Chinese, Simplified"))
        self.comboBoxLang.setItemText(2, _translate("MainWindow", "Chinese, Traditional"))
        self.comboBoxLang.setItemText(3, _translate("MainWindow", "Japanese"))
        self.comboBoxLang.setItemText(4, _translate("MainWindow", "Korean"))
        self.btnCopy.setText(_translate("MainWindow", "Copy"))
        self.btnSave.setText(_translate("MainWindow", "Save"))
        self.menuAbout.setTitle(_translate("MainWindow", "About"))
        self.actionAbout_Minerva.setText(_translate("MainWindow", "About Minerva"))