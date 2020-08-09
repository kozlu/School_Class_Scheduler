# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(800, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(711, 526))
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.tabWidget.setFont(font)
        self.tabWidget.setStyleSheet("")
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setObjectName("tabWidget")
        self.tabInstructors = QtWidgets.QWidget()
        self.tabInstructors.setObjectName("tabInstructors")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tabInstructors)
        self.verticalLayout_2.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox = QtWidgets.QGroupBox(self.tabInstructors)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnInstrAdd = QtWidgets.QPushButton(self.groupBox)
        self.btnInstrAdd.setObjectName("btnInstrAdd")
        self.horizontalLayout.addWidget(self.btnInstrAdd)
        self.btnInstrImport = QtWidgets.QPushButton(self.groupBox)
        self.btnInstrImport.setObjectName("btnInstrImport")
        self.horizontalLayout.addWidget(self.btnInstrImport)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.treeInstr = QtWidgets.QTreeView(self.tabInstructors)
        self.treeInstr.setObjectName("treeInstr")
        self.verticalLayout_2.addWidget(self.treeInstr)
        self.tabWidget.addTab(self.tabInstructors, "")
        self.tabRooms = QtWidgets.QWidget()
        self.tabRooms.setObjectName("tabRooms")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tabRooms)
        self.verticalLayout_3.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tabRooms)
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.btnRoomAdd = QtWidgets.QPushButton(self.groupBox_2)
        self.btnRoomAdd.setObjectName("btnRoomAdd")
        self.horizontalLayout_7.addWidget(self.btnRoomAdd)
        self.btnRoomImport = QtWidgets.QPushButton(self.groupBox_2)
        self.btnRoomImport.setObjectName("btnRoomImport")
        self.horizontalLayout_7.addWidget(self.btnRoomImport)
        self.verticalLayout_3.addWidget(self.groupBox_2)
        self.treeRoom = QtWidgets.QTreeView(self.tabRooms)
        self.treeRoom.setObjectName("treeRoom")
        self.verticalLayout_3.addWidget(self.treeRoom)
        self.tabWidget.addTab(self.tabRooms, "")
        self.tabSubjects = QtWidgets.QWidget()
        self.tabSubjects.setObjectName("tabSubjects")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tabSubjects)
        self.verticalLayout_4.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.groupBox_3 = QtWidgets.QGroupBox(self.tabSubjects)
        self.groupBox_3.setObjectName("groupBox_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btnSubjAdd = QtWidgets.QPushButton(self.groupBox_3)
        self.btnSubjAdd.setObjectName("btnSubjAdd")
        self.horizontalLayout_2.addWidget(self.btnSubjAdd)
        self.btnSubjImport = QtWidgets.QPushButton(self.groupBox_3)
        self.btnSubjImport.setObjectName("btnSubjImport")
        self.horizontalLayout_2.addWidget(self.btnSubjImport)
        self.verticalLayout_4.addWidget(self.groupBox_3)
        self.treeSubj = QtWidgets.QTreeView(self.tabSubjects)
        self.treeSubj.setObjectName("treeSubj")
        self.verticalLayout_4.addWidget(self.treeSubj)
        self.tabWidget.addTab(self.tabSubjects, "")
        self.tabSections = QtWidgets.QWidget()
        self.tabSections.setObjectName("tabSections")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.tabSections)
        self.verticalLayout_5.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.groupBox_4 = QtWidgets.QGroupBox(self.tabSections)
        self.groupBox_4.setObjectName("groupBox_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.btnSecAdd = QtWidgets.QPushButton(self.groupBox_4)
        self.btnSecAdd.setObjectName("btnSecAdd")
        self.horizontalLayout_3.addWidget(self.btnSecAdd)
        self.verticalLayout_5.addWidget(self.groupBox_4)
        self.treeSec = QtWidgets.QTreeView(self.tabSections)
        self.treeSec.setObjectName("treeSec")
        self.verticalLayout_5.addWidget(self.treeSec)
        self.tabWidget.addTab(self.tabSections, "")
        self.tabScenario = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabScenario.sizePolicy().hasHeightForWidth())
        self.tabScenario.setSizePolicy(sizePolicy)
        self.tabScenario.setObjectName("tabScenario")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.tabScenario)
        self.verticalLayout_6.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_6.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.groupBox_5 = QtWidgets.QGroupBox(self.tabScenario)
        self.groupBox_5.setObjectName("groupBox_5")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.groupBox_5)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.btnScenGenerate = QtWidgets.QPushButton(self.groupBox_5)
        self.btnScenGenerate.setObjectName("btnScenGenerate")
        self.horizontalLayout_4.addWidget(self.btnScenGenerate)
        self.btnScenResult = QtWidgets.QPushButton(self.groupBox_5)
        self.btnScenResult.setObjectName("btnScenResult")
        self.horizontalLayout_4.addWidget(self.btnScenResult)
        self.verticalLayout_6.addWidget(self.groupBox_5)
        self.groupBox_6 = QtWidgets.QGroupBox(self.tabScenario)
        self.groupBox_6.setObjectName("groupBox_6")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.groupBox_7 = QtWidgets.QGroupBox(self.groupBox_6)
        self.groupBox_7.setStyleSheet("border: none")
        self.groupBox_7.setTitle("")
        self.groupBox_7.setFlat(False)
        self.groupBox_7.setCheckable(False)
        self.groupBox_7.setChecked(False)
        self.groupBox_7.setObjectName("groupBox_7")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.groupBox_7)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(10)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.radioLunchYes = QtWidgets.QRadioButton(self.groupBox_7)
        self.radioLunchYes.setChecked(True)
        self.radioLunchYes.setObjectName("radioLunchYes")
        self.horizontalLayout_5.addWidget(self.radioLunchYes)
        self.radioLunchNo = QtWidgets.QRadioButton(self.groupBox_7)
        self.radioLunchNo.setObjectName("radioLunchNo")
        self.horizontalLayout_5.addWidget(self.radioLunchNo)
        self.gridLayout_2.addWidget(self.groupBox_7, 2, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.groupBox_6)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 2, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.groupBox_6)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 0, 0, 1, 1)
        self.timeStarting = QtWidgets.QTimeEdit(self.groupBox_6)
        self.timeStarting.setCurrentSection(QtWidgets.QDateTimeEdit.HourSection)
        self.timeStarting.setTime(QtCore.QTime(8, 0, 0))
        self.timeStarting.setObjectName("timeStarting")
        self.gridLayout_2.addWidget(self.timeStarting, 0, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.groupBox_6)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 1, 0, 1, 1)
        self.timeEnding = QtWidgets.QTimeEdit(self.groupBox_6)
        self.timeEnding.setCalendarPopup(True)
        self.timeEnding.setTime(QtCore.QTime(18, 0, 0))
        self.timeEnding.setObjectName("timeEnding")
        self.gridLayout_2.addWidget(self.timeEnding, 1, 1, 1, 1)
        self.verticalLayout_6.addWidget(self.groupBox_6)
        self.groupBox_8 = QtWidgets.QGroupBox(self.tabScenario)
        self.groupBox_8.setObjectName("groupBox_8")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_8)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_20 = QtWidgets.QLabel(self.groupBox_8)
        self.label_20.setObjectName("label_20")
        self.gridLayout_3.addWidget(self.label_20, 2, 3, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.groupBox_8)
        self.label_21.setObjectName("label_21")
        self.gridLayout_3.addWidget(self.label_21, 3, 3, 1, 1)
        self.editDev = QtWidgets.QSpinBox(self.groupBox_8)
        self.editDev.setMaximum(100)
        self.editDev.setProperty("value", 55)
        self.editDev.setObjectName("editDev")
        self.gridLayout_3.addWidget(self.editDev, 3, 5, 1, 1)
        self.editMaxPop = QtWidgets.QSpinBox(self.groupBox_8)
        self.editMaxPop.setMinimum(50)
        self.editMaxPop.setMaximum(10000)
        self.editMaxPop.setProperty("value", 100)
        self.editMaxPop.setObjectName("editMaxPop")
        self.gridLayout_3.addWidget(self.editMaxPop, 1, 1, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.groupBox_8)
        self.label_12.setObjectName("label_12")
        self.gridLayout_3.addWidget(self.label_12, 1, 3, 1, 1)
        self.editElite = QtWidgets.QSpinBox(self.groupBox_8)
        self.editElite.setMaximum(100)
        self.editElite.setProperty("value", 5)
        self.editElite.setObjectName("editElite")
        self.gridLayout_3.addWidget(self.editElite, 2, 5, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem1, 0, 7, 1, 1)
        self.editMaxGen = QtWidgets.QSpinBox(self.groupBox_8)
        self.editMaxGen.setMinimum(50)
        self.editMaxGen.setMaximum(10000)
        self.editMaxGen.setObjectName("editMaxGen")
        self.gridLayout_3.addWidget(self.editMaxGen, 2, 1, 1, 1)
        self.editMaxFit = QtWidgets.QSpinBox(self.groupBox_8)
        self.editMaxFit.setMaximum(100)
        self.editMaxFit.setProperty("value", 90)
        self.editMaxFit.setObjectName("editMaxFit")
        self.gridLayout_3.addWidget(self.editMaxFit, 1, 5, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.groupBox_8)
        self.label_11.setObjectName("label_11")
        self.gridLayout_3.addWidget(self.label_11, 0, 3, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.groupBox_8)
        self.label_10.setObjectName("label_10")
        self.gridLayout_3.addWidget(self.label_10, 3, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.groupBox_8)
        self.label_9.setObjectName("label_9")
        self.gridLayout_3.addWidget(self.label_9, 2, 0, 1, 1)
        self.editMaxCreation = QtWidgets.QSpinBox(self.groupBox_8)
        self.editMaxCreation.setMinimum(1500)
        self.editMaxCreation.setMaximum(30000)
        self.editMaxCreation.setObjectName("editMaxCreation")
        self.gridLayout_3.addWidget(self.editMaxCreation, 3, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.groupBox_8)
        self.label_7.setObjectName("label_7")
        self.gridLayout_3.addWidget(self.label_7, 0, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.groupBox_8)
        self.label_8.setObjectName("label_8")
        self.gridLayout_3.addWidget(self.label_8, 1, 0, 1, 1)
        self.editMinPop = QtWidgets.QSpinBox(self.groupBox_8)
        self.editMinPop.setMinimum(50)
        self.editMinPop.setMaximum(10000)
        self.editMinPop.setObjectName("editMinPop")
        self.gridLayout_3.addWidget(self.editMinPop, 0, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem2, 0, 11, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem3, 0, 10, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem4, 0, 2, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem5, 0, 9, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem6, 0, 8, 1, 1)
        self.editMut = QtWidgets.QDoubleSpinBox(self.groupBox_8)
        self.editMut.setMaximum(100.0)
        self.editMut.setSingleStep(0.01)
        self.editMut.setProperty("value", 0.08)
        self.editMut.setObjectName("editMut")
        self.gridLayout_3.addWidget(self.editMut, 0, 5, 1, 1)
        self.verticalLayout_6.addWidget(self.groupBox_8)
        self.groupBox_9 = QtWidgets.QGroupBox(self.tabScenario)
        self.groupBox_9.setObjectName("groupBox_9")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_9)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_15 = QtWidgets.QLabel(self.groupBox_9)
        self.label_15.setObjectName("label_15")
        self.gridLayout_4.addWidget(self.label_15, 2, 0, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.groupBox_9)
        self.label_18.setObjectName("label_18")
        self.gridLayout_4.addWidget(self.label_18, 3, 0, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.groupBox_9)
        self.label_19.setObjectName("label_19")
        self.gridLayout_4.addWidget(self.label_19, 5, 0, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.groupBox_9)
        self.label_17.setObjectName("label_17")
        self.gridLayout_4.addWidget(self.label_17, 7, 0, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.groupBox_9)
        self.label_16.setObjectName("label_16")
        self.gridLayout_4.addWidget(self.label_16, 4, 0, 1, 1)
        self.editSbj = QtWidgets.QSpinBox(self.groupBox_9)
        self.editSbj.setMaximum(100)
        self.editSbj.setProperty("value", 70)
        self.editSbj.setObjectName("editSbj")
        self.gridLayout_4.addWidget(self.editSbj, 0, 1, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.groupBox_9)
        self.label_13.setObjectName("label_13")
        self.gridLayout_4.addWidget(self.label_13, 0, 0, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.groupBox_9)
        self.label_14.setObjectName("label_14")
        self.gridLayout_4.addWidget(self.label_14, 1, 0, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem7, 0, 2, 1, 1)
        self.editLun = QtWidgets.QSpinBox(self.groupBox_9)
        self.editLun.setMaximum(100)
        self.editLun.setProperty("value", 5)
        self.editLun.setObjectName("editLun")
        self.gridLayout_4.addWidget(self.editLun, 1, 1, 1, 1)
        self.editSec = QtWidgets.QSpinBox(self.groupBox_9)
        self.editSec.setMaximum(100)
        self.editSec.setProperty("value", 5)
        self.editSec.setObjectName("editSec")
        self.gridLayout_4.addWidget(self.editSec, 2, 1, 1, 1)
        self.editInstrRest = QtWidgets.QSpinBox(self.groupBox_9)
        self.editInstrRest.setMaximum(100)
        self.editInstrRest.setProperty("value", 5)
        self.editInstrRest.setObjectName("editInstrRest")
        self.gridLayout_4.addWidget(self.editInstrRest, 4, 1, 1, 1)
        self.editInstrLoad = QtWidgets.QSpinBox(self.groupBox_9)
        self.editInstrLoad.setMaximum(100)
        self.editInstrLoad.setProperty("value", 5)
        self.editInstrLoad.setObjectName("editInstrLoad")
        self.gridLayout_4.addWidget(self.editInstrLoad, 5, 1, 1, 1)
        self.editIdle = QtWidgets.QSpinBox(self.groupBox_9)
        self.editIdle.setMaximum(100)
        self.editIdle.setProperty("value", 5)
        self.editIdle.setObjectName("editIdle")
        self.gridLayout_4.addWidget(self.editIdle, 3, 1, 1, 1)
        self.editMeet = QtWidgets.QSpinBox(self.groupBox_9)
        self.editMeet.setMaximum(100)
        self.editMeet.setProperty("value", 5)
        self.editMeet.setObjectName("editMeet")
        self.gridLayout_4.addWidget(self.editMeet, 7, 1, 1, 1)
        self.lblTotal = QtWidgets.QLabel(self.groupBox_9)
        self.lblTotal.setObjectName("lblTotal")
        self.gridLayout_4.addWidget(self.lblTotal, 8, 0, 1, 1)
        self.verticalLayout_6.addWidget(self.groupBox_9)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem8)
        self.tabWidget.addTab(self.tabScenario, "")
        self.verticalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionSave_As = QtWidgets.QAction(MainWindow)
        self.actionSave_As.setObjectName("actionSave_As")
        self.actionSettings = QtWidgets.QAction(MainWindow)
        self.actionSettings.setObjectName("actionSettings")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionAdd_Instructor = QtWidgets.QAction(MainWindow)
        self.actionAdd_Instructor.setObjectName("actionAdd_Instructor")
        self.actionView_Instructors = QtWidgets.QAction(MainWindow)
        self.actionView_Instructors.setObjectName("actionView_Instructors")
        self.actionAdd_Room = QtWidgets.QAction(MainWindow)
        self.actionAdd_Room.setObjectName("actionAdd_Room")
        self.actionView_Rooms = QtWidgets.QAction(MainWindow)
        self.actionView_Rooms.setObjectName("actionView_Rooms")
        self.actionAdd_Subject = QtWidgets.QAction(MainWindow)
        self.actionAdd_Subject.setObjectName("actionAdd_Subject")
        self.actionView_Subjects = QtWidgets.QAction(MainWindow)
        self.actionView_Subjects.setObjectName("actionView_Subjects")
        self.actionAdd_Sections = QtWidgets.QAction(MainWindow)
        self.actionAdd_Sections.setObjectName("actionAdd_Sections")
        self.actionView_Sections = QtWidgets.QAction(MainWindow)
        self.actionView_Sections.setObjectName("actionView_Sections")
        self.actionImport = QtWidgets.QAction(MainWindow)
        self.actionImport.setObjectName("actionImport")
        self.actionExport = QtWidgets.QAction(MainWindow)
        self.actionExport.setObjectName("actionExport")
        self.actionView_Results = QtWidgets.QAction(MainWindow)
        self.actionView_Results.setObjectName("actionView_Results")
        self.actionGenerate = QtWidgets.QAction(MainWindow)
        self.actionGenerate.setObjectName("actionGenerate")
        self.actionImport_2 = QtWidgets.QAction(MainWindow)
        self.actionImport_2.setObjectName("actionImport_2")
        self.actionExport_2 = QtWidgets.QAction(MainWindow)
        self.actionExport_2.setObjectName("actionExport_2")
        self.actionScenario_Summary = QtWidgets.QAction(MainWindow)
        self.actionScenario_Summary.setObjectName("actionScenario_Summary")
        self.actionGenerate_2 = QtWidgets.QAction(MainWindow)
        self.actionGenerate_2.setObjectName("actionGenerate_2")
        self.actionView_Results_2 = QtWidgets.QAction(MainWindow)
        self.actionView_Results_2.setObjectName("actionView_Results_2")
        self.actionInstructions = QtWidgets.QAction(MainWindow)
        self.actionInstructions.setObjectName("actionInstructions")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave_As)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSettings)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionInstructions)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(4)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Ders Çizelgesi Hazırlama"))
        self.tabInstructors.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.groupBox.setTitle(_translate("MainWindow", "İşlem"))
        self.btnInstrAdd.setText(_translate("MainWindow", "Öğretmen Ekle"))
        self.btnInstrImport.setText(_translate("MainWindow", "CSV Dosyasından Al"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabInstructors), _translate("MainWindow", "Öğretmenler"))
        self.groupBox_2.setTitle(_translate("MainWindow", "İşlem"))
        self.btnRoomAdd.setText(_translate("MainWindow", "Mekan Ekle"))
        self.btnRoomImport.setText(_translate("MainWindow", "CSV Dosyasından Al"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabRooms), _translate("MainWindow", "Mekanlar"))
        self.groupBox_3.setTitle(_translate("MainWindow", "İşlem"))
        self.btnSubjAdd.setText(_translate("MainWindow", "Ders Ekle"))
        self.btnSubjImport.setText(_translate("MainWindow", "CSV Dosyasından Al"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabSubjects), _translate("MainWindow", "Dersler"))
        self.groupBox_4.setTitle(_translate("MainWindow", "İşlem"))
        self.btnSecAdd.setText(_translate("MainWindow", "Grup Ekle"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabSections), _translate("MainWindow", "Gruplar"))
        self.groupBox_5.setTitle(_translate("MainWindow", "İşlem"))
        self.btnScenGenerate.setText(_translate("MainWindow", "Çizelgeyi Oluştur"))
        self.btnScenResult.setText(_translate("MainWindow", "Sonuçları İncele"))
        self.groupBox_6.setTitle(_translate("MainWindow", "Okul İşlem Ayarları"))
        self.radioLunchYes.setText(_translate("MainWindow", "Evet"))
        self.radioLunchNo.setText(_translate("MainWindow", "Hayır"))
        self.label_6.setToolTip(_translate("MainWindow", "Gruplar için Öğle Yemeği Molası"))
        self.label_6.setText(_translate("MainWindow", "Öğle Yemeği Molası"))
        self.label_4.setToolTip(_translate("MainWindow", "Okul açılış saati"))
        self.label_4.setText(_translate("MainWindow", "İşlem başlangıç saati"))
        self.timeStarting.setDisplayFormat(_translate("MainWindow", "h AP"))
        self.label_5.setToolTip(_translate("MainWindow", "Okul kapanış saati"))
        self.label_5.setText(_translate("MainWindow", "İşlem bitiş saati"))
        self.timeEnding.setDisplayFormat(_translate("MainWindow", "h AP"))
        self.groupBox_8.setTitle(_translate("MainWindow", "Genetik Algoritma Ayarları"))
        self.label_20.setToolTip(_translate("MainWindow", "Elit nüfus yüzdesi"))
        self.label_20.setText(_translate("MainWindow", "Elit Nüfusu"))
        self.label_21.setToolTip(_translate("MainWindow", "Maksimum sigma kontrolü"))
        self.label_21.setText(_translate("MainWindow", "Sapma Toleransı"))
        self.label_12.setToolTip(_translate("MainWindow", "Bir kromozom bununla karşılaştığında nesli durdurur"))
        self.label_12.setText(_translate("MainWindow", "Maksimum Uygunluk"))
        self.label_11.setToolTip(_translate("MainWindow",
                                            "<html><head/><body><p>Ortalama uygunluk farkı belirtilen düzeye düştüğünde mutasyon oranı değişikliğini tetikler</p></body></html>"))
        self.label_11.setText(_translate("MainWindow", "Mutasyon Oranı Ayar Tetikleyicisi"))
        self.label_10.setToolTip(_translate("MainWindow", "Geçerli bir kromozom oluşturmak için maksimum deneme sayısı"))
        self.label_10.setText(_translate("MainWindow", "Maksimum Oluşturma Denemesi"))
        self.label_9.setToolTip(
            _translate("MainWindow", "Çözüm oluşturmak için kullanılacak maksimum nesil sayısı"))
        self.label_9.setText(_translate("MainWindow", "Maksimum Nesil Sayısı"))
        self.label_7.setToolTip(
            _translate("MainWindow", "Genetik algoritma için başlangıç ve maksimum nüfus sayısı"))
        self.label_7.setText(_translate("MainWindow", "Minimum Nüfus Sayısı"))
        self.label_8.setToolTip(_translate("MainWindow", "Genetik algoritma için maksimum nüfus sayısı"))
        self.label_8.setText(_translate("MainWindow", "Maksimum Nüfus Sayısı"))
        self.groupBox_9.setTitle(_translate("MainWindow", "Değerlendirme Matrisi"))
        self.label_15.setToolTip(_translate("MainWindow",
                                            "Ders molası ağırlığı (Her ardışık 3 ders için bir mola olmalıdır)"))
        self.label_15.setText(_translate("MainWindow", "Ders Molası"))
        self.label_18.setToolTip(_translate("MainWindow", "Ders boşta kalma süresini azaltma ağırlığı"))
        self.label_18.setText(_translate("MainWindow", "Ders Boşta Kalma Süresi"))
        self.label_19.setToolTip(
            _translate("MainWindow", "Tüm öğretmenlerin normalleştirilmiş öğretim yüküne sahip olmasının ağırlığı"))
        self.label_19.setText(_translate("MainWindow", "Öğretmen Ders Yükü Dengesi"))
        self.label_17.setToolTip(
            _translate("MainWindow", "Ders yerleştirme için doğru sıra düzenine sahip olmanın ağırlığı"))
        self.label_17.setText(_translate("MainWindow", "Ders Devamlılığı"))
        self.label_16.setToolTip(_translate("MainWindow",
                                            "Öğretmen molası ağırlığı (Her ardışık 3 ders için bir mola olmalıdır)"))
        self.label_16.setText(_translate("MainWindow", "Öğretmen Molası"))
        self.label_13.setToolTip(_translate("MainWindow", "Ders yerleşimlerinin ağırlığı"))
        self.label_13.setText(_translate("MainWindow", "Ders Yerleşimi"))
        self.label_14.setToolTip(_translate("MainWindow", "Öğle yemeği molasının ağırlığı"))
        self.label_14.setText(_translate("MainWindow", "Öğle Yemeği Molası"))
        self.lblTotal.setText(_translate("MainWindow", "Toplam: "))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabScenario),
                                  _translate("MainWindow", "Genel Ayarlar"))
        self.menuFile.setTitle(_translate("MainWindow", "Dosya"))
        self.menuHelp.setTitle(_translate("MainWindow", "Yardım"))
        self.actionNew.setText(_translate("MainWindow", "Yeni..."))
        self.actionOpen.setText(_translate("MainWindow", "Aç..."))
        self.actionSave.setText(_translate("MainWindow", "Kaydet"))
        self.actionSave_As.setText(_translate("MainWindow", "Farklı Kaydet..."))
        self.actionSettings.setText(_translate("MainWindow", "Ayarlar"))
        self.actionExit.setText(_translate("MainWindow", "Çıkış"))
        self.actionAdd_Instructor.setText(_translate("MainWindow", "Öğretmen Ekle"))
        self.actionView_Instructors.setText(_translate("MainWindow", "Öğretmeleri Gör"))
        self.actionAdd_Room.setText(_translate("MainWindow", "Mekan Ekle"))
        self.actionView_Rooms.setText(_translate("MainWindow", "Mekanları Gör"))
        self.actionAdd_Subject.setText(_translate("MainWindow", "Ders Ekle"))
        self.actionView_Subjects.setText(_translate("MainWindow", "Dersleri Gör"))
        self.actionAdd_Sections.setText(_translate("MainWindow", "Grup Ekle"))
        self.actionView_Sections.setText(_translate("MainWindow", "Grupları Gör"))
        self.actionImport.setText(_translate("MainWindow", "Al..."))
        self.actionExport.setText(_translate("MainWindow", "Ver..."))
        self.actionView_Results.setText(_translate("MainWindow", "Sonuçları İncele"))
        self.actionGenerate.setText(_translate("MainWindow", "Çizelgeyi Oluştur"))
        self.actionImport_2.setText(_translate("MainWindow", "Al..."))
        self.actionExport_2.setText(_translate("MainWindow", "Ver..."))
        self.actionScenario_Summary.setText(_translate("MainWindow", "Genel Ayarlar"))
        self.actionGenerate_2.setText(_translate("MainWindow", "Çizelgeyi Oluştur"))
        self.actionView_Results_2.setText(_translate("MainWindow", "Sonuçları İncele"))
        self.actionInstructions.setText(_translate("MainWindow", "Bilgilendirme"))
        self.actionAbout.setText(_translate("MainWindow", "Hakkımızda"))
