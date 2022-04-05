# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'styleQt.ui'
##
## Created by: Qt User Interface Compiler version 6.2.4
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)
import files_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(300, 500)
        MainWindow.setMinimumSize(QSize(300, 500))
        MainWindow.setMaximumSize(QSize(300, 500))
        icon = QIcon()
        icon.addFile(u":/icon/outline_calculate_black_24dp.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"QWidget {\n"
"	color:white;\n"
"	background-color: #121212;\n"
"	font-family:Rubik;\n"
"    font-size:16pt;\n"
"    font-weight:600;\n"
"}\n"
"\n"
"QPushButton{\n"
"	background-color:transparent;\n"
"	border:none;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"	background-color:#666;\n"
"\n"
"\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color:#888;\n"
"\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_01 = QLabel(self.centralwidget)
        self.label_01.setObjectName(u"label_01")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_01.sizePolicy().hasHeightForWidth())
        self.label_01.setSizePolicy(sizePolicy)
        self.label_01.setMinimumSize(QSize(0, 0))
        self.label_01.setStyleSheet(u"color:#888;")
        self.label_01.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.label_01)

        self.line_01 = QLineEdit(self.centralwidget)
        self.line_01.setObjectName(u"line_01")
        self.line_01.setStyleSheet(u"font-size:40pt;\n"
"border:none;")
        self.line_01.setMaxLength(12)
        self.line_01.setReadOnly(True)

        self.verticalLayout.addWidget(self.line_01)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.btn_7 = QPushButton(self.centralwidget)
        self.btn_7.setObjectName(u"btn_7")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_7.sizePolicy().hasHeightForWidth())
        self.btn_7.setSizePolicy(sizePolicy1)

        self.gridLayout_2.addWidget(self.btn_7, 3, 0, 1, 1)

        self.btn_d = QPushButton(self.centralwidget)
        self.btn_d.setObjectName(u"btn_d")
        sizePolicy1.setHeightForWidth(self.btn_d.sizePolicy().hasHeightForWidth())
        self.btn_d.setSizePolicy(sizePolicy1)

        self.gridLayout_2.addWidget(self.btn_d, 0, 3, 1, 1)

        self.btn_C = QPushButton(self.centralwidget)
        self.btn_C.setObjectName(u"btn_C")
        sizePolicy1.setHeightForWidth(self.btn_C.sizePolicy().hasHeightForWidth())
        self.btn_C.setSizePolicy(sizePolicy1)

        self.gridLayout_2.addWidget(self.btn_C, 0, 0, 1, 1)

        self.btn_mu = QPushButton(self.centralwidget)
        self.btn_mu.setObjectName(u"btn_mu")
        sizePolicy1.setHeightForWidth(self.btn_mu.sizePolicy().hasHeightForWidth())
        self.btn_mu.setSizePolicy(sizePolicy1)

        self.gridLayout_2.addWidget(self.btn_mu, 4, 0, 1, 1)

        self.btn_6 = QPushButton(self.centralwidget)
        self.btn_6.setObjectName(u"btn_6")
        sizePolicy1.setHeightForWidth(self.btn_6.sizePolicy().hasHeightForWidth())
        self.btn_6.setSizePolicy(sizePolicy1)

        self.gridLayout_2.addWidget(self.btn_6, 2, 2, 1, 1)

        self.btn_uu = QPushButton(self.centralwidget)
        self.btn_uu.setObjectName(u"btn_uu")
        sizePolicy1.setHeightForWidth(self.btn_uu.sizePolicy().hasHeightForWidth())
        self.btn_uu.setSizePolicy(sizePolicy1)

        self.gridLayout_2.addWidget(self.btn_uu, 2, 3, 1, 1)

        self.btn_3 = QPushButton(self.centralwidget)
        self.btn_3.setObjectName(u"btn_3")
        sizePolicy1.setHeightForWidth(self.btn_3.sizePolicy().hasHeightForWidth())
        self.btn_3.setSizePolicy(sizePolicy1)

        self.gridLayout_2.addWidget(self.btn_3, 1, 2, 1, 1)

        self.btn_x = QPushButton(self.centralwidget)
        self.btn_x.setObjectName(u"btn_x")
        sizePolicy1.setHeightForWidth(self.btn_x.sizePolicy().hasHeightForWidth())
        self.btn_x.setSizePolicy(sizePolicy1)
        icon1 = QIcon()
        icon1.addFile(u":/icon/outline_backspace_white_24dp.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_x.setIcon(icon1)
        self.btn_x.setIconSize(QSize(24, 24))

        self.gridLayout_2.addWidget(self.btn_x, 0, 2, 1, 1)

        self.btn_4 = QPushButton(self.centralwidget)
        self.btn_4.setObjectName(u"btn_4")
        sizePolicy1.setHeightForWidth(self.btn_4.sizePolicy().hasHeightForWidth())
        self.btn_4.setSizePolicy(sizePolicy1)

        self.gridLayout_2.addWidget(self.btn_4, 2, 0, 1, 1)

        self.btn_t = QPushButton(self.centralwidget)
        self.btn_t.setObjectName(u"btn_t")
        sizePolicy1.setHeightForWidth(self.btn_t.sizePolicy().hasHeightForWidth())
        self.btn_t.setSizePolicy(sizePolicy1)

        self.gridLayout_2.addWidget(self.btn_t, 4, 2, 1, 1)

        self.btn_do = QPushButton(self.centralwidget)
        self.btn_do.setObjectName(u"btn_do")
        sizePolicy1.setHeightForWidth(self.btn_do.sizePolicy().hasHeightForWidth())
        self.btn_do.setSizePolicy(sizePolicy1)

        self.gridLayout_2.addWidget(self.btn_do, 3, 3, 1, 1)

        self.btn_9 = QPushButton(self.centralwidget)
        self.btn_9.setObjectName(u"btn_9")
        sizePolicy1.setHeightForWidth(self.btn_9.sizePolicy().hasHeightForWidth())
        self.btn_9.setSizePolicy(sizePolicy1)

        self.gridLayout_2.addWidget(self.btn_9, 3, 2, 1, 1)

        self.btn_r = QPushButton(self.centralwidget)
        self.btn_r.setObjectName(u"btn_r")
        sizePolicy1.setHeightForWidth(self.btn_r.sizePolicy().hasHeightForWidth())
        self.btn_r.setSizePolicy(sizePolicy1)

        self.gridLayout_2.addWidget(self.btn_r, 4, 3, 1, 1)

        self.btn_u = QPushButton(self.centralwidget)
        self.btn_u.setObjectName(u"btn_u")
        sizePolicy1.setHeightForWidth(self.btn_u.sizePolicy().hasHeightForWidth())
        self.btn_u.setSizePolicy(sizePolicy1)

        self.gridLayout_2.addWidget(self.btn_u, 1, 3, 1, 1)

        self.btn_1 = QPushButton(self.centralwidget)
        self.btn_1.setObjectName(u"btn_1")
        sizePolicy1.setHeightForWidth(self.btn_1.sizePolicy().hasHeightForWidth())
        self.btn_1.setSizePolicy(sizePolicy1)

        self.gridLayout_2.addWidget(self.btn_1, 1, 0, 1, 1)

        self.btn_5 = QPushButton(self.centralwidget)
        self.btn_5.setObjectName(u"btn_5")
        sizePolicy1.setHeightForWidth(self.btn_5.sizePolicy().hasHeightForWidth())
        self.btn_5.setSizePolicy(sizePolicy1)

        self.gridLayout_2.addWidget(self.btn_5, 2, 1, 1, 1)

        self.btn_2 = QPushButton(self.centralwidget)
        self.btn_2.setObjectName(u"btn_2")
        sizePolicy1.setHeightForWidth(self.btn_2.sizePolicy().hasHeightForWidth())
        self.btn_2.setSizePolicy(sizePolicy1)

        self.gridLayout_2.addWidget(self.btn_2, 1, 1, 1, 1)

        self.btn_8 = QPushButton(self.centralwidget)
        self.btn_8.setObjectName(u"btn_8")
        sizePolicy1.setHeightForWidth(self.btn_8.sizePolicy().hasHeightForWidth())
        self.btn_8.setSizePolicy(sizePolicy1)

        self.gridLayout_2.addWidget(self.btn_8, 3, 1, 1, 1)

        self.btn_0 = QPushButton(self.centralwidget)
        self.btn_0.setObjectName(u"btn_0")
        sizePolicy1.setHeightForWidth(self.btn_0.sizePolicy().hasHeightForWidth())
        self.btn_0.setSizePolicy(sizePolicy1)

        self.gridLayout_2.addWidget(self.btn_0, 4, 1, 1, 1)

        self.btn_CE = QPushButton(self.centralwidget)
        self.btn_CE.setObjectName(u"btn_CE")
        sizePolicy1.setHeightForWidth(self.btn_CE.sizePolicy().hasHeightForWidth())
        self.btn_CE.setSizePolicy(sizePolicy1)

        self.gridLayout_2.addWidget(self.btn_CE, 0, 1, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_2, 1, 0, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u" calculator -W", None))
        self.label_01.setText("")
        self.btn_7.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.btn_d.setText(QCoreApplication.translate("MainWindow", u"/", None))
        self.btn_C.setText(QCoreApplication.translate("MainWindow", u"C", None))
        self.btn_mu.setText(QCoreApplication.translate("MainWindow", u"+/-", None))
        self.btn_6.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.btn_uu.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.btn_3.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.btn_4.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.btn_t.setText(QCoreApplication.translate("MainWindow", u".", None))
        self.btn_do.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.btn_9.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.btn_r.setText(QCoreApplication.translate("MainWindow", u"=", None))
        self.btn_u.setText(QCoreApplication.translate("MainWindow", u"*", None))
        self.btn_1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.btn_5.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.btn_2.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.btn_8.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.btn_0.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.btn_CE.setText(QCoreApplication.translate("MainWindow", u"CE", None))
    # retranslateUi

