# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt6 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QCursor
from PyQt6.QtCore import Qt
from PyQt6 import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(650, 900)
        # MainWindow.setMinim
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.mainFrame = QtWidgets.QFrame(self.centralwidget)
        # self.mainFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        # self.mainFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mainFrame.setObjectName("mainFrame")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.mainFrame)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.topFrame = QtWidgets.QFrame(self.mainFrame)
        self.topFrame.setEnabled(True)
        # self.topFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        # self.topFrame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.topFrame.setObjectName("topFrame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.topFrame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem = QtWidgets.QSpacerItem(50,20) #(50, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(50,20) #(50, 0, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 0, 2, 1, 1)
        self.lbl_artwork = QtWidgets.QLabel(self.topFrame)
        self.lbl_artwork.setFixedSize(QtCore.QSize(300, 300))
        self.lbl_artwork.setText("")
        self.lbl_artwork.setPixmap(QtGui.QPixmap(":/icons/images/list-music.png"))
        self.lbl_artwork.setScaledContents(True)
        self.lbl_artwork.setObjectName("lbl_artwork")
        self.gridLayout_2.addWidget(self.lbl_artwork, 1, 1, 1, 1)
        self.gridLayout_6.addWidget(self.topFrame, 0, 0, 1, 1)
        self.frameMiddle = QtWidgets.QFrame(self.mainFrame)

        self.frameMiddle.setObjectName("frameMiddle")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frameMiddle)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.frameSlider = QtWidgets.QFrame(self.frameMiddle)

        self.frameSlider.setObjectName("frameSlider")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frameSlider)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.horizontalSlider = QtWidgets.QSlider(Qt.Orientation.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.horizontalSlider.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.horizontalSlider.setEnabled(False)
        self.gridLayout_3.addWidget(self.horizontalSlider, 0, 1, 1, 1)
        self.remaining_time = QtWidgets.QLabel(self.topFrame)
        self.remaining_time.setText("--:--")
        self.elapsed_time = QtWidgets.QLabel(self.topFrame)
        self.elapsed_time.setText("--:--")
        self.gridLayout_3.addWidget(self.elapsed_time, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.remaining_time, 0, 2, 1, 1)
        self.lbl_song = QtWidgets.QLabel(self.frameSlider)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setKerning(True)
        self.lbl_song.setFont(font)
        self.lbl_song.setScaledContents(True)
        self.lbl_song.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lbl_song.setObjectName("lbl_song")
        self.gridLayout_3.addWidget(self.lbl_song, 1, 0, 1, 3)
        self.lbl_artist = QtWidgets.QLabel(self.frameSlider)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setKerning(True)
        self.lbl_artist.setFont(font)
        self.lbl_artist.setScaledContents(True)
        self.lbl_artist.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lbl_artist.setObjectName("lbl_artist")
        self.gridLayout_3.addWidget(self.lbl_artist, 2, 0, 1, 3)
        self.gridLayout_4.addWidget(self.frameSlider, 0, 0, 1, 1)
        self.frameButtons = QtWidgets.QFrame(self.frameMiddle)

        self.frameButtons.setObjectName("frameButtons")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frameButtons)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_open_file = QtWidgets.QPushButton(self.frameButtons)
        self.btn_open_file.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/images/folder-open.png")), #QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_open_file.setIcon(icon)
        self.btn_open_file.setIconSize(QtCore.QSize(30, 30))
        self.btn_open_file.setCheckable(False)
        self.btn_open_file.setObjectName("btn_back")
        self.horizontalLayout.addWidget(self.btn_open_file)
        self.btn_back = QtWidgets.QPushButton(self.frameButtons)
        self.btn_back.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/images/rewind.png")), #QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_back.setIcon(icon)
        self.btn_back.setIconSize(QtCore.QSize(30, 30))
        self.btn_back.setCheckable(False)
        self.btn_back.setObjectName("btn_back")
        self.horizontalLayout.addWidget(self.btn_back)
        self.btn_stop = QtWidgets.QPushButton(self.frameButtons)
        self.btn_stop.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/images/stop.png")), #QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_stop.setIcon(icon1)
        self.btn_stop.setIconSize(QtCore.QSize(30, 30))
        self.btn_stop.setObjectName("btn_stop")
        self.horizontalLayout.addWidget(self.btn_stop)
        self.btn_playpause = QtWidgets.QPushButton(self.frameButtons)
        self.btn_playpause.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/images/play-pause.png")), #QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_playpause.setIcon(icon2)
        self.btn_playpause.setIconSize(QtCore.QSize(30, 30))
        self.btn_playpause.setObjectName("btn_playpause")
        self.horizontalLayout.addWidget(self.btn_playpause)
        self.btn_forward = QtWidgets.QPushButton(self.frameButtons)
        self.btn_forward.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/images/forward.png")), #QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_forward.setIcon(icon3)
        self.btn_forward.setIconSize(QtCore.QSize(30, 30))
        self.btn_forward.setObjectName("btn_forward")
        self.horizontalLayout.addWidget(self.btn_forward)
        self.btn_shuffle = QtWidgets.QPushButton(self.frameButtons)
        self.btn_shuffle.setText("")
        self.btn_shuffle.setBaseSize(60,46)
        self.btn_shuffle.setIconSize(QtCore.QSize(10, 10))
        self.btn_shuffle.setCheckable(False)
        self.btn_shuffle.setObjectName("btn_back")
        self.horizontalLayout.addWidget(self.btn_shuffle)
        self.slider_volume = QtWidgets.QSlider(self.frameButtons)
        self.slider_volume.setValue(100)
        self.slider_volume.setMaximumSize(QtCore.QSize(150, 16777215))
        self.slider_volume.setMaximum(100)
        self.slider_volume.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.slider_volume.setObjectName("slider_volume")
        self.slider_volume.setTickPosition(QtWidgets.QSlider.TickPosition.TicksLeft)
        self.slider_volume.setMinimumWidth(60)
        self.horizontalLayout.addWidget(self.slider_volume)
        self.gridLayout_4.addWidget(self.frameButtons, 1, 0, 1, 1)
        self.gridLayout_6.addWidget(self.frameMiddle, 1, 0, 1, 1)
        self.frameDown = QtWidgets.QFrame(self.mainFrame)
        # self.frameDown.setFrameShape(QtWidgets.QFrame.NoFrame)
        # self.frameDown.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameDown.setObjectName("frameDown")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.frameDown)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.table_songs = QtWidgets.QTableWidget(self.frameDown)
        self.table_songs.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectionBehavior.SelectRows)  # انتخاب کل ردیف
        self.table_songs.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)  # غیرفعال کردن ویرایش محتوای سلول

        # self.table_songs.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.table_songs.setTabletTracking(False)
        # self.table_songs.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        # self.table_songs.setTextElideMode(QtCore.Qt.ElideLeft)
        self.table_songs.setShowGrid(True)
        # self.table_songs.setGridStyle(QtCore.Qt.DashDotDotLine)
        self.table_songs.setWordWrap(True)
        self.table_songs.setCornerButtonEnabled(False)
        self.table_songs.setObjectName("table_songs")
        self.table_songs.setColumnCount(4)
        # self.table_songs.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.table_songs.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_songs.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_songs.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_songs.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_songs.setHorizontalHeaderItem(3, item)
        
        item = QtWidgets.QTableWidgetItem()
        self.table_songs.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_songs.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_songs.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_songs.setItem(0, 3, item)
        self.table_songs.horizontalHeader().setVisible(False)
        self.table_songs.horizontalHeader().setCascadingSectionResizes(False)
        # self.table_songs.horizontalHeader().setDefaultSectionSize(100)
        self.table_songs.horizontalHeader().setHighlightSections(True)
        self.table_songs.horizontalHeader().setSortIndicatorShown(False)
        self.table_songs.horizontalHeader().setStretchLastSection(True)
        self.table_songs.verticalHeader().setStretchLastSection(False)
        self.table_songs.verticalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
        self.gridLayout_5.addWidget(self.table_songs, 0, 0, 1, 1)
        self.gridLayout_6.addWidget(self.frameDown, 2, 0, 1, 1)
        self.gridLayout.addWidget(self.mainFrame, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        # self.actionOpen_File = QtWidgets.QAction(MainWindow)
        # self.actionOpen_File.setObjectName("actionOpen_File")
        # self.actionMaximize = QtWidgets.QAction(MainWindow)
        # self.actionMaximize.setObjectName("actionMaximize")
        # self.actionMinimize = QtWidgets.QAction(MainWindow)
        # self.actionMinimize.setObjectName("actionMinimize")
        # self.actionClose = QtWidgets.QAction(MainWindow)
        # self.actionClose.setObjectName("actionClose")
        # self.actionAbout_Mini_Player = QtWidgets.QAction(MainWindow)
        # self.actionAbout_Mini_Player.setObjectName("actionAbout_Mini_Player")
        # self.menuMenu.addAction(self.actionOpen_File)
        # self.menuMenu.addAction(self.actionMaximize)
        # self.menuMenu.addAction(self.actionMinimize)
        # self.menuMenu.addSeparator()
        # self.menuMenu.addAction(self.actionClose)
        # self.menuHelp.addAction(self.actionAbout_Mini_Player)
        # self.menubar.addAction(self.menuMenu.menuAction())
        # self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lbl_song.setText(_translate("MainWindow", ""))
        self.lbl_artist.setText(_translate("MainWindow", ""))
        self.table_songs.setSortingEnabled(False)
        self.table_songs.setFont(QtGui.QFont("Tahoma", 13))
        item = self.table_songs.verticalHeaderItem(0)
        # item.setText(_translate("MainWindow", "1"))
        # item = self.table_songs.horizontalHeaderItem(0)
        # item.setText(_translate("MainWindow", "#"))
        item = self.table_songs.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Artist"))
        item = self.table_songs.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Title"))
        item = self.table_songs.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Album"))
        item = self.table_songs.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Time"))
        __sortingEnabled = self.table_songs.isSortingEnabled()
        self.table_songs.setSortingEnabled(False)
        self.table_songs.setSortingEnabled(__sortingEnabled)
        self.menuMenu.setTitle(_translate("MainWindow", "Menu"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        # self.actionOpen_File.setText(_translate("MainWindow", "Open File"))
        # self.actionMaximize.setText(_translate("MainWindow", "Maximize"))
        # self.actionMinimize.setText(_translate("MainWindow", "Minimize"))
        # self.actionClose.setText(_translate("MainWindow", "Close"))
        # self.actionAbout_Mini_Player.setText(_translate("MainWindow", "About Mini Player"))
import icons_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
