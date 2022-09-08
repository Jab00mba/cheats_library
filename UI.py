# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cheats.ui'
#
# Created by: PyQt5 UI code generator 5.15.5
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Foundation(object):
    def setupUi(self, Cheatlibrary):
        Cheatlibrary.setObjectName("Cheat library")
        Cheatlibrary.resize(1200, 650)
        self.centralwidget = QtWidgets.QWidget(Cheatlibrary)
        self.centralwidget.setObjectName("centralwidget")
        self.home_button = QtWidgets.QPushButton(self.centralwidget)
        self.home_button.setGeometry(QtCore.QRect(0, 10, 70, 40))
        self.home_button.setObjectName("home_button")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(69, -20, 1130, 600))
        self.stackedWidget.setObjectName("stackedWidget")
        self.main_page = QtWidgets.QWidget()
        self.main_page.setObjectName("main_page")
        self.gameplay_button = QtWidgets.QPushButton(self.main_page)
        self.gameplay_button.setGeometry(QtCore.QRect(0, 100, 250, 500))
        font = QtGui.QFont()
        font.setFamily("Pricedown Rus")
        font.setPointSize(40)
        self.gameplay_button.setFont(font)
        self.gameplay_button.setObjectName("gameplay_button")
        self.world_button = QtWidgets.QPushButton(self.main_page)
        self.world_button.setGeometry(QtCore.QRect(270, 100, 250, 500))
        font = QtGui.QFont()
        font.setFamily("Pricedown Rus")
        font.setPointSize(40)
        self.world_button.setFont(font)
        self.world_button.setObjectName("world_button")
        self.weapon_button = QtWidgets.QPushButton(self.main_page)
        self.weapon_button.setGeometry(QtCore.QRect(540, 100, 250, 500))
        font = QtGui.QFont()
        font.setFamily("Pricedown Rus")
        font.setPointSize(40)
        self.weapon_button.setFont(font)
        self.weapon_button.setObjectName("weapon_button")
        self.spawn_button = QtWidgets.QPushButton(self.main_page)
        self.spawn_button.setGeometry(QtCore.QRect(810, 100, 250, 500))
        font = QtGui.QFont()
        font.setFamily("Pricedown Rus")
        font.setPointSize(40)
        self.spawn_button.setFont(font)
        self.spawn_button.setObjectName("spawn_button")
        self.search_label = QtWidgets.QLineEdit(self.main_page)
        self.search_label.setGeometry(QtCore.QRect(210, 40, 560, 30))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.search_label.setFont(font)
        self.search_label.setText("")
        self.search_label.setObjectName("search_label")
        self.search_button = QtWidgets.QPushButton(self.main_page)
        self.search_button.setGeometry(QtCore.QRect(770, 40, 75, 30))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.search_button.setFont(font)
        self.search_button.setObjectName("search_button")
        self.stackedWidget.addWidget(self.main_page)
        self.spawn_page = QtWidgets.QWidget()
        self.spawn_page.setObjectName("spawn_page")
        self.stackedWidget.addWidget(self.spawn_page)
        self.weapon_page = QtWidgets.QWidget()
        self.weapon_page.setObjectName("weapon_page")
        self.stackedWidget.addWidget(self.weapon_page)
        self.world_page = QtWidgets.QWidget()
        self.world_page.setObjectName("world_page")
        self.stackedWidget.addWidget(self.world_page)
        self.gameplay_page = QtWidgets.QWidget()
        self.gameplay_page.setObjectName("gameplay_page")
        self.stackedWidget.addWidget(self.gameplay_page)
        Cheatlibrary.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Cheatlibrary)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 21))
        self.menubar.setObjectName("menubar")
        Cheatlibrary.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Cheatlibrary)
        self.statusbar.setObjectName("statusbar")
        Cheatlibrary.setStatusBar(self.statusbar)

        self.retranslateUi(Cheatlibrary)
        QtCore.QMetaObject.connectSlotsByName(Cheatlibrary)

    def retranslateUi(self, Cheatlibrary):
        _translate = QtCore.QCoreApplication.translate
        Cheatlibrary.setWindowTitle(_translate("Cheatlibrary", "Cheat library"))
        self.home_button.setText(_translate("Cheatlibrary", "Home"))
        self.gameplay_button.setText(_translate("Cheatlibrary", "Gameplay"))
        self.world_button.setText(_translate("Cheatlibrary", "world"))
        self.weapon_button.setText(_translate("Cheatlibrary", "weapon"))
        self.spawn_button.setText(_translate("Cheatlibrary", "spawn"))
        self.search_button.setText(_translate("Cheatlibrary", "search"))