# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from os import truncate
from PyQt6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PyQt6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PyQt6.QtWidgets import (QAbstractScrollArea, QApplication, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QSlider, QSpacerItem, QTableWidget, QTableWidgetItem, QListWidget, QListView, QListWidgetItem, QWidget)
import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 1112)
        self.actionOpen_File = QAction(MainWindow)
        self.actionOpen_File.setObjectName(u"actionOpen_File")
        self.actionMaximize = QAction(MainWindow)
        self.actionMaximize.setObjectName(u"actionMaximize")
        self.actionMinimize = QAction(MainWindow)
        self.actionMinimize.setObjectName(u"actionMinimize")
        self.actionClose = QAction(MainWindow)
        self.actionClose.setObjectName(u"actionClose")
        self.actionAbout_Mini_Player = QAction(MainWindow)
        self.actionAbout_Mini_Player.setObjectName(u"actionAbout_Mini_Player")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.mainFrame = QFrame(self.centralwidget)
        self.mainFrame.setObjectName(u"mainFrame")
        self.mainFrame.setFrameShape(QFrame.NoFrame)
        self.mainFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.mainFrame)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.topFrame = QFrame(self.mainFrame)
        self.topFrame.setObjectName(u"topFrame")
        self.topFrame.setEnabled(True)
        self.topFrame.setFrameShape(QFrame.NoFrame)
        self.topFrame.setFrameShadow(QFrame.Plain)
        self.gridLayout_2 = QGridLayout(self.topFrame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalSpacer = QSpacerItem(50, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 0, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(50, 0, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 0, 2, 1, 1)

        self.lbl_artwork = QLabel(self.topFrame)
        self.lbl_artwork.setObjectName(u"lbl_artwork")
        self.lbl_artwork.setMaximumSize(QSize(500, 500))
        self.lbl_artwork.setPixmap(QPixmap(u":/icons/images/list-music.png"))
        self.lbl_artwork.setScaledContents(truncate)

        self.gridLayout_2.addWidget(self.lbl_artwork, 1, 1, 1, 1)


        self.gridLayout_6.addWidget(self.topFrame, 0, 0, 1, 1)

        self.frameMiddle = QFrame(self.mainFrame)
        self.frameMiddle.setObjectName(u"frameMiddle")
        self.frameMiddle.setFrameShape(QFrame.NoFrame)
        self.frameMiddle.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frameMiddle)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.frameSlider = QFrame(self.frameMiddle)
        self.frameSlider.setObjectName(u"frameSlider")
        self.frameSlider.setFrameShape(QFrame.NoFrame)
        self.frameSlider.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frameSlider)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.horizontalSlider = QSlider(self.frameSlider)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setOrientation(Qt.Horizontal)

        self.gridLayout_3.addWidget(self.horizontalSlider, 0, 0, 1, 1)

        self.lbl_song = QLabel(self.frameSlider)
        self.lbl_song.setObjectName(u"lbl_song")
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setKerning(True)
        font.setStyleStrategy(QFont.PreferAntialias)
        self.lbl_song.setFont(font)
        self.lbl_song.setLayoutDirection(Qt.LeftToRight)
        self.lbl_song.setScaledContents(True)
        self.lbl_song.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.lbl_song, 1, 0, 1, 1)

        self.lbl_artist = QLabel(self.frameSlider)
        self.lbl_artist.setObjectName(u"lbl_artist")
        font1 = QFont()
        font1.setPointSize(20)
        font1.setBold(False)
        font1.setKerning(True)
        font1.setStyleStrategy(QFont.PreferAntialias)
        self.lbl_artist.setFont(font1)
        self.lbl_artist.setLayoutDirection(Qt.LeftToRight)
        self.lbl_artist.setScaledContents(True)
        self.lbl_artist.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.lbl_artist, 2, 0, 1, 1)


        self.gridLayout_4.addWidget(self.frameSlider, 0, 0, 1, 1)

        self.frameButtons = QFrame(self.frameMiddle)
        self.frameButtons.setObjectName(u"frameButtons")
        self.frameButtons.setFrameShape(QFrame.NoFrame)
        self.frameButtons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frameButtons)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_back = QPushButton(self.frameButtons)
        self.btn_back.setObjectName(u"btn_back")
        icon = QIcon()
        icon.addFile(u":/icons/images/rewind.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_back.setIcon(icon)
        self.btn_back.setIconSize(QSize(30, 30))
        self.btn_back.setCheckable(False)

        self.horizontalLayout.addWidget(self.btn_back)

        self.btn_stop = QPushButton(self.frameButtons)
        self.btn_stop.setObjectName(u"btn_stop")
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/stop.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_stop.setIcon(icon1)
        self.btn_stop.setIconSize(QSize(30, 30))

        self.horizontalLayout.addWidget(self.btn_stop)

        self.btn_playpause = QPushButton(self.frameButtons)
        self.btn_playpause.setObjectName(u"btn_playpause")
        icon2 = QIcon()
        icon2.addFile(u":/icons/images/play-pause.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_playpause.setIcon(icon2)
        self.btn_playpause.setIconSize(QSize(30, 30))

        self.horizontalLayout.addWidget(self.btn_playpause)

        self.btn_forward = QPushButton(self.frameButtons)
        self.btn_forward.setObjectName(u"btn_forward")
        icon3 = QIcon()
        icon3.addFile(u":/icons/images/forward.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_forward.setIcon(icon3)
        self.btn_forward.setIconSize(QSize(30, 30))

        self.horizontalLayout.addWidget(self.btn_forward)

        self.slider_volume = QSlider(self.frameButtons)
        self.slider_volume.setObjectName(u"slider_volume")
        self.slider_volume.setMaximumSize(QSize(150, 16777215))
        self.slider_volume.setMaximum(100)
        self.slider_volume.setOrientation(Qt.Horizontal)

        self.horizontalLayout.addWidget(self.slider_volume)


        self.gridLayout_4.addWidget(self.frameButtons, 1, 0, 1, 1)


        self.gridLayout_6.addWidget(self.frameMiddle, 1, 0, 1, 1)

        self.frameDown = QFrame(self.mainFrame)
        self.frameDown.setObjectName(u"frameDown")
        self.frameDown.setFrameShape(QFrame.NoFrame)
        self.frameDown.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frameDown)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.table_songs = QListWidget(self.frameDown)
        if (self.table_songs.columnCount() < 4):
            self.table_songs.setColumnCount(4)
        __qlistwidgetitem = QListWidgetItem()
        self.table_songs.setHorizontalHeaderItem(0, __qlistwidgetitem)
        __qlistwidgetitem1 = QListWidgetItem()
        self.table_songs.setHorizontalHeaderItem(1, __qlistwidgetitem1)
        __qlistwidgetitem2 = QListWidgetItem()
        self.table_songs.setHorizontalHeaderItem(2, __qlistwidgetitem2)
        __qlistwidgetitem3 = QListWidgetItem()
        self.table_songs.setHorizontalHeaderItem(3, __qlistwidgetitem3)
        if (self.table_songs.rowCount() < 1):
            self.table_songs.setRowCount(1)
        __qlistwidgetitem4 = QListWidgetItem()
        self.table_songs.setVerticalHeaderItem(0, __qlistwidgetitem4)
        __qlistwidgetitem5 = QListWidgetItem()
        self.table_songs.setItem(0, 0, __qlistwidgetitem5)
        __qlistwidgetitem6 = QListWidgetItem()
        self.table_songs.setItem(0, 1, __qlistwidgetitem6)
        __qlistwidgetitem7 = QListWidgetItem()
        self.table_songs.setItem(0, 2, __qlistwidgetitem7)
        __qlistwidgetitem8 = QListWidgetItem()
        self.table_songs.setItem(0, 3, __qlistwidgetitem8)
        self.table_songs.setObjectName(u"table_songs")
        self.table_songs.setTabletTracking(False)
        self.table_songs.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.table_songs.setTextElideMode(Qt.ElideLeft)
        self.table_songs.setShowGrid(True)
        self.table_songs.setGridStyle(Qt.DashDotDotLine)
        self.table_songs.setSortingEnabled(False)
        self.table_songs.setWordWrap(True)
        self.table_songs.setCornerButtonEnabled(False)
        self.table_songs.horizontalHeader().setVisible(True)
        self.table_songs.horizontalHeader().setCascadingSectionResizes(False)
        self.table_songs.horizontalHeader().setDefaultSectionSize(100)
        self.table_songs.horizontalHeader().setHighlightSections(True)
        self.table_songs.horizontalHeader().setProperty("showSortIndicator", False)
        self.table_songs.horizontalHeader().setStretchLastSection(True)
        self.table_songs.verticalHeader().setStretchLastSection(False)

        self.gridLayout_5.addWidget(self.table_songs, 0, 0, 1, 1)


        self.gridLayout_6.addWidget(self.frameDown, 2, 0, 1, 1)


        self.gridLayout.addWidget(self.mainFrame, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        # self.menubar.setNativeMenuBar(False)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 21))
        self.menuMenu = QMenu(self.menubar)
        self.menuMenu.setObjectName(u"menuMenu")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuMenu.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuMenu.addAction(self.actionOpen_File)
        self.menuMenu.addAction(self.actionMaximize)
        self.menuMenu.addAction(self.actionMinimize)
        self.menuMenu.addSeparator()
        self.menuMenu.addAction(self.actionClose)
        self.menuHelp.addAction(self.actionAbout_Mini_Player)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionOpen_File.setText(QCoreApplication.translate("MainWindow", u"Open File", None))
        self.actionMaximize.setText(QCoreApplication.translate("MainWindow", u"Maximize", None))
        self.actionMinimize.setText(QCoreApplication.translate("MainWindow", u"Minimize", None))
        self.actionClose.setText(QCoreApplication.translate("MainWindow", u"Close", None))
        self.actionAbout_Mini_Player.setText(QCoreApplication.translate("MainWindow", u"About Mini Player", None))
        self.lbl_artwork.setText("")
        self.lbl_song.setText(QCoreApplication.translate("MainWindow", u"Song", None))
        self.lbl_artist.setText(QCoreApplication.translate("MainWindow", u"Artist", None))
        self.btn_back.setText("")
        self.btn_stop.setText("")
        self.btn_playpause.setText("")
        self.btn_forward.setText("")
        ___qlistwidgetitem = self.table_songs.horizontalHeaderItem(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", u"#", None));
        ___qlistwidgetitem1 = self.table_songs.horizontalHeaderItem(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Artist", None));
        ___qlistwidgetitem2 = self.table_songs.horizontalHeaderItem(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Songs", None));
        ___qlistwidgetitem3 = self.table_songs.horizontalHeaderItem(3)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Time", None));
        ___qlistwidgetitem4 = self.table_songs.verticalHeaderItem(0)
        ___qlistwidgetitem4.setText(QCoreApplication.translate("MainWindow", u"1", None));

        # __sortingEnabled = self.table_songs.isSortingEnabled()
        # self.table_songs.setSortingEnabled(False)
        # # ___qlistwidgetitem5 = self.table_songs.item(0, 0)
        # # ___qlistwidgetitem5.setText(QCoreApplication.translate("MainWindow", u"1", None));
        # # ___qlistwidgetitem6 = self.table_songs.item(0, 1)
        # # ___qlistwidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Googoosh", None));
        # # ___qlistwidgetitem7 = self.table_songs.item(0, 2)
        # # ___qlistwidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Nafas", None));
        # # ___qlistwidgetitem8 = self.table_songs.item(0, 3)
        # # ___qlistwidgetitem8.setText(QCoreApplication.translate("MainWindow", u"05:27", None));
        # self.table_songs.setSortingEnabled(__sortingEnabled)

        self.menuMenu.setTitle(QCoreApplication.translate("MainWindow", u"Menu", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

