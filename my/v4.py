# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'v4.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 680)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 800, 680))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.frame.setEnabled(True)
        self.frame.setStyleSheet("background-image: url(./background.jpeg);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.w_time_signalture = QtWidgets.QComboBox(self.frame)
        self.w_time_signalture.setGeometry(QtCore.QRect(360, 220, 111, 21))
        self.w_time_signalture.setObjectName("w_time_signalture")
        self.w_time_signalture.addItem("")
        self.w_time_signalture.addItem("")
        self.w_mode = QtWidgets.QComboBox(self.frame)
        self.w_mode.setGeometry(QtCore.QRect(360, 140, 111, 21))
        self.w_mode.setObjectName("w_mode")
        self.w_mode.addItem("")
        self.w_mode.addItem("")
        self.w_mode.addItem("")
        self.w_mode.addItem("")
        self.w_mode.addItem("")
        self.w_mode.addItem("")
        self.w_mode.addItem("")
        self.w_mode.addItem("")
        self.w_mode.addItem("")
        self.w_bass = QtWidgets.QComboBox(self.frame)
        self.w_bass.setGeometry(QtCore.QRect(360, 300, 111, 21))
        self.w_bass.setObjectName("w_bass")
        self.w_bass.addItem("")
        self.w_bass.addItem("")
        self.w_bass.addItem("")
        self.w_bass.addItem("")
        self.w_bass.addItem("")
        self.w_bass.addItem("")
        self.w_bass.addItem("")
        self.w_bass.addItem("")
        self.w_accompany = QtWidgets.QComboBox(self.frame)
        self.w_accompany.setGeometry(QtCore.QRect(360, 260, 111, 21))
        self.w_accompany.setObjectName("w_accompany")
        self.w_accompany.addItem("")
        self.w_accompany.addItem("")
        self.w_accompany.addItem("")
        self.w_accompany.addItem("")
        self.w_accompany.addItem("")
        self.w_accompany.addItem("")
        self.w_key = QtWidgets.QComboBox(self.frame)
        self.w_key.setEnabled(True)
        self.w_key.setGeometry(QtCore.QRect(360, 100, 111, 21))
        self.w_key.setMaxVisibleItems(7)
        self.w_key.setObjectName("w_key")
        self.w_key.addItem("")
        self.w_key.addItem("")
        self.w_key.addItem("")
        self.w_key.addItem("")
        self.w_key.addItem("")
        self.w_key.addItem("")
        self.w_key.addItem("")
        self.verticalLayout_3.addWidget(self.frame)
        self.verticalLayout_2.addLayout(self.verticalLayout_3)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(190, 340, 141, 31))
        self.label.setObjectName("label")
        self.w_play = QtWidgets.QPushButton(self.centralwidget)
        self.w_play.setGeometry(QtCore.QRect(360, 490, 93, 28))
        self.w_play.setAutoDefault(False)
        self.w_play.setDefault(False)
        self.w_play.setFlat(False)
        self.w_play.setObjectName("w_play")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(190, 380, 121, 31))
        self.label_7.setObjectName("label_7")
        self.w_intensity = QtWidgets.QSlider(self.centralwidget)
        self.w_intensity.setGeometry(QtCore.QRect(340, 430, 160, 22))
        self.w_intensity.setMaximum(100)
        self.w_intensity.setSingleStep(1)
        self.w_intensity.setOrientation(QtCore.Qt.Horizontal)
        self.w_intensity.setObjectName("w_intensity")
        self.w_repeat = QtWidgets.QLineEdit(self.centralwidget)
        self.w_repeat.setGeometry(QtCore.QRect(360, 380, 113, 21))
        self.w_repeat.setInputMask("")
        self.w_repeat.setMaxLength(32767)
        self.w_repeat.setObjectName("w_repeat")
        self.w_bpm = QtWidgets.QLineEdit(self.centralwidget)
        self.w_bpm.setGeometry(QtCore.QRect(360, 180, 113, 21))
        self.w_bpm.setObjectName("w_bpm")
        self.w_chord_progression = QtWidgets.QLineEdit(self.centralwidget)
        self.w_chord_progression.setGeometry(QtCore.QRect(360, 340, 113, 21))
        self.w_chord_progression.setObjectName("w_chord_progression")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(190, 180, 121, 31))
        self.label_6.setObjectName("label_6")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(190, 100, 121, 31))
        self.label_5.setObjectName("label_5")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(190, 420, 121, 31))
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(190, 220, 121, 31))
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(190, 140, 121, 31))
        self.label_4.setObjectName("label_4")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(190, 260, 121, 31))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(190, 300, 121, 31))
        self.label_9.setObjectName("label_9")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(630, 430, 91, 19))
        self.checkBox.setObjectName("checkBox")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 798, 26))
        self.menubar.setObjectName("menubar")
        self.menusetting = QtWidgets.QMenu(self.menubar)
        self.menusetting.setObjectName("menusetting")
        self.menuhelp = QtWidgets.QMenu(self.menubar)
        self.menuhelp.setObjectName("menuhelp")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionsetting = QtWidgets.QAction(MainWindow)
        self.actionsetting.setObjectName("actionsetting")
        self.actionexit = QtWidgets.QAction(MainWindow)
        self.actionexit.setObjectName("actionexit")
        self.actiondocument_2 = QtWidgets.QAction(MainWindow)
        self.actiondocument_2.setObjectName("actiondocument_2")
        self.actionabout = QtWidgets.QAction(MainWindow)
        self.actionabout.setObjectName("actionabout")
        self.menusetting.addSeparator()
        self.menusetting.addAction(self.actionsetting)
        self.menusetting.addSeparator()
        self.menusetting.addAction(self.actionexit)
        self.menuhelp.addAction(self.actiondocument_2)
        self.menuAbout.addAction(self.actionabout)
        self.menubar.addAction(self.menusetting.menuAction())
        self.menubar.addAction(self.menuhelp.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        self.w_key.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.w_time_signalture.setItemText(0, _translate("MainWindow", "4/4"))
        self.w_time_signalture.setItemText(1, _translate("MainWindow", "3/4"))
        self.w_mode.setItemText(0, _translate("MainWindow", "major"))
        self.w_mode.setItemText(1, _translate("MainWindow", "dorian"))
        self.w_mode.setItemText(2, _translate("MainWindow", "phrygian"))
        self.w_mode.setItemText(3, _translate("MainWindow", "lydian"))
        self.w_mode.setItemText(4, _translate("MainWindow", "mixolydian"))
        self.w_mode.setItemText(5, _translate("MainWindow", "minor"))
        self.w_mode.setItemText(6, _translate("MainWindow", "locrian"))
        self.w_mode.setItemText(7, _translate("MainWindow", "major pentatonic"))
        self.w_mode.setItemText(8, _translate("MainWindow", "minor pentatonic"))
        self.w_bass.setItemText(0, _translate("MainWindow", "None"))
        self.w_bass.setItemText(1, _translate("MainWindow", "1"))
        self.w_bass.setItemText(2, _translate("MainWindow", "2"))
        self.w_bass.setItemText(3, _translate("MainWindow", "3"))
        self.w_bass.setItemText(4, _translate("MainWindow", "4"))
        self.w_bass.setItemText(5, _translate("MainWindow", "5"))
        self.w_bass.setItemText(6, _translate("MainWindow", "6"))
        self.w_bass.setItemText(7, _translate("MainWindow", "7"))
        self.w_accompany.setItemText(0, _translate("MainWindow", "1"))
        self.w_accompany.setItemText(1, _translate("MainWindow", "2"))
        self.w_accompany.setItemText(2, _translate("MainWindow", "3"))
        self.w_accompany.setItemText(3, _translate("MainWindow", "4"))
        self.w_accompany.setItemText(4, _translate("MainWindow", "5"))
        self.w_accompany.setItemText(5, _translate("MainWindow", "6"))
        self.w_key.setCurrentText(_translate("MainWindow", "C"))
        self.w_key.setItemText(0, _translate("MainWindow", "C"))
        self.w_key.setItemText(1, _translate("MainWindow", "D"))
        self.w_key.setItemText(2, _translate("MainWindow", "E"))
        self.w_key.setItemText(3, _translate("MainWindow", "F"))
        self.w_key.setItemText(4, _translate("MainWindow", "G"))
        self.w_key.setItemText(5, _translate("MainWindow", "A"))
        self.w_key.setItemText(6, _translate("MainWindow", "B"))
        self.label.setText(_translate("MainWindow", "Chord progression"))
        self.w_play.setText(_translate("MainWindow", "GO"))
        self.label_7.setText(_translate("MainWindow", "repeat"))
        self.w_repeat.setText(_translate("MainWindow", "1"))
        self.w_bpm.setText(_translate("MainWindow", "120"))
        self.w_chord_progression.setText(_translate("MainWindow", "4321"))
        self.label_6.setText(_translate("MainWindow", "bpm"))
        self.label_5.setText(_translate("MainWindow", "key"))
        self.label_3.setText(_translate("MainWindow", "intensity"))
        self.label_2.setText(_translate("MainWindow", "Time signalture"))
        self.label_4.setText(_translate("MainWindow", "mode"))
        self.label_8.setText(_translate("MainWindow", "accompany"))
        self.label_9.setText(_translate("MainWindow", "bass"))
        self.checkBox.setText(_translate("MainWindow", "silent"))
        self.menusetting.setTitle(_translate("MainWindow", "Menu"))
        self.menuhelp.setTitle(_translate("MainWindow", "Help"))
        self.menuAbout.setTitle(_translate("MainWindow", "About"))
        self.actionsetting.setText(_translate("MainWindow", "setting"))
        self.actionexit.setText(_translate("MainWindow", "exit"))
        self.actiondocument_2.setText(_translate("MainWindow", "document"))
        self.actionabout.setText(_translate("MainWindow", "about"))
