# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/epi/.qgis/python/plugins/Qplanet/preference_ui.ui'
#
# Created: Tue Nov 10 19:01:42 2009
#      by: PyQt4 UI code generator 4.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(394, 327)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/epi.gif"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.toolBox = QtGui.QToolBox(Form)
        self.toolBox.setObjectName("toolBox")
        self.page_5 = QtGui.QWidget()
        self.page_5.setGeometry(QtCore.QRect(0, 0, 376, 213))
        self.page_5.setObjectName("page_5")
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.page_5)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.groupBox_2 = QtGui.QGroupBox(self.page_5)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_6 = QtGui.QLabel(self.groupBox_2)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_7.addWidget(self.label_6)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem)
        self.selectpref = QtGui.QToolButton(self.groupBox_2)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/page22_1.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.selectpref.setIcon(icon1)
        self.selectpref.setObjectName("selectpref")
        self.horizontalLayout_7.addWidget(self.selectpref)
        self.ossimpreference = QtGui.QLineEdit(self.groupBox_2)
        self.ossimpreference.setObjectName("ossimpreference")
        self.horizontalLayout_7.addWidget(self.ossimpreference)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_5 = QtGui.QLabel(self.groupBox_2)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_6.addWidget(self.label_5)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem1)
        self.selectkmlDir = QtGui.QToolButton(self.groupBox_2)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/directory.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.selectkmlDir.setIcon(icon2)
        self.selectkmlDir.setObjectName("selectkmlDir")
        self.horizontalLayout_6.addWidget(self.selectkmlDir)
        self.kmldir = QtGui.QLineEdit(self.groupBox_2)
        self.kmldir.setObjectName("kmldir")
        self.horizontalLayout_6.addWidget(self.kmldir)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        spacerItem2 = QtGui.QSpacerItem(20, 104, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.verticalLayout_5.addWidget(self.groupBox_2)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/epi.gif"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolBox.addItem(self.page_5, icon3, "")
        self.page_4 = QtGui.QWidget()
        self.page_4.setGeometry(QtCore.QRect(0, 0, 376, 213))
        self.page_4.setObjectName("page_4")
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.page_4)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.groupBox_4 = QtGui.QGroupBox(self.page_4)
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout_8 = QtGui.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_4 = QtGui.QLabel(self.groupBox_4)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_5.addWidget(self.label_4)
        self.selectgeonamesdb = QtGui.QToolButton(self.groupBox_4)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/icons/db.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.selectgeonamesdb.setIcon(icon4)
        self.selectgeonamesdb.setObjectName("selectgeonamesdb")
        self.horizontalLayout_5.addWidget(self.selectgeonamesdb)
        self.geonames = QtGui.QLineEdit(self.groupBox_4)
        self.geonames.setObjectName("geonames")
        self.horizontalLayout_5.addWidget(self.geonames)
        self.verticalLayout_8.addLayout(self.horizontalLayout_5)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem3)
        self.verticalLayout_7.addWidget(self.groupBox_4)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/db.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolBox.addItem(self.page_4, icon5, "")
        self.page_2 = QtGui.QWidget()
        self.page_2.setGeometry(QtCore.QRect(0, 0, 376, 213))
        self.page_2.setObjectName("page_2")
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.page_2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.groupBox = QtGui.QGroupBox(self.page_2)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.hostname = QtGui.QLineEdit(self.groupBox)
        self.hostname.setObjectName("hostname")
        self.horizontalLayout.addWidget(self.hostname)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.navport = QtGui.QLineEdit(self.groupBox)
        self.navport.setObjectName("navport")
        self.horizontalLayout_2.addWidget(self.navport)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem6)
        self.dataport = QtGui.QLineEdit(self.groupBox)
        self.dataport.setObjectName("dataport")
        self.horizontalLayout_3.addWidget(self.dataport)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem7 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem7)
        self.SaveTCPSettings = QtGui.QPushButton(self.groupBox)
        self.SaveTCPSettings.setObjectName("SaveTCPSettings")
        self.horizontalLayout_4.addWidget(self.SaveTCPSettings)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        spacerItem8 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem8)
        self.verticalLayout_4.addWidget(self.groupBox)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icons/keyser-tux-wifi-logo-2300.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolBox.addItem(self.page_2, icon6, "")
        self.verticalLayout.addWidget(self.toolBox)

        self.retranslateUi(Form)
        self.toolBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Preference", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("Form", "ossim_preference", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Form", "KML Directory", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_5), QtGui.QApplication.translate("Form", "Preference", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Form", "Geonames", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_4), QtGui.QApplication.translate("Form", "SqLite", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "Host", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Form", "Nav-Port", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Form", "Data-Port", None, QtGui.QApplication.UnicodeUTF8))
        self.SaveTCPSettings.setText(QtGui.QApplication.translate("Form", "OK", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), QtGui.QApplication.translate("Form", "TCP", None, QtGui.QApplication.UnicodeUTF8))

import resources_rc
