# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gis.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(435, 462)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.shapefileinput = QtWidgets.QLineEdit(self.groupBox)
        self.shapefileinput.setObjectName("shapefileinput")
        self.verticalLayout_2.addWidget(self.shapefileinput)
        self.inputFeatue1 = QtWidgets.QToolButton(self.groupBox)
        self.inputFeatue1.setObjectName("inputFeatue1")
        self.verticalLayout_2.addWidget(self.inputFeatue1)
        self.shapefileinput2 = QtWidgets.QLineEdit(self.groupBox)
        self.shapefileinput2.setObjectName("shapefileinput2")
        self.verticalLayout_2.addWidget(self.shapefileinput2)
        self.inputFeature2 = QtWidgets.QToolButton(self.groupBox)
        self.inputFeature2.setObjectName("inputFeature2")
        self.verticalLayout_2.addWidget(self.inputFeature2)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.shapefileoutput = QtWidgets.QLineEdit(self.groupBox_2)
        self.shapefileoutput.setObjectName("shapefileoutput")
        self.verticalLayout_3.addWidget(self.shapefileoutput)
        self.outputFeature = QtWidgets.QToolButton(self.groupBox_2)
        self.outputFeature.setObjectName("outputFeature")
        self.verticalLayout_3.addWidget(self.outputFeature)
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.comboBox = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox.setObjectName("comboBox")
        self.verticalLayout_3.addWidget(self.comboBox)
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.comboBox_2 = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox_2.setObjectName("comboBox_2")
        self.verticalLayout_3.addWidget(self.comboBox_2)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.runTask = QtWidgets.QPushButton(self.groupBox_3)
        self.runTask.setObjectName("runTask")
        self.verticalLayout_4.addWidget(self.runTask)
        self.verticalLayout.addWidget(self.groupBox_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 435, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.toolBar.addAction(self.actionExit)

        self.retranslateUi(MainWindow)
        self.actionExit.triggered.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Gis program"))
        self.groupBox.setTitle(_translate("MainWindow", "Input features"))
        self.inputFeatue1.setText(_translate("MainWindow", "..."))
        self.inputFeature2.setText(_translate("MainWindow", "..."))
        self.groupBox_2.setTitle(_translate("MainWindow", "Output features"))
        self.outputFeature.setText(_translate("MainWindow", "..."))
        self.label.setText(_translate("MainWindow", "Country:"))
        self.label_2.setText(_translate("MainWindow", "feature type"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Processing"))
        self.runTask.setText(_translate("MainWindow", "Run"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionExit.setToolTip(_translate("MainWindow", "Exit Program"))


