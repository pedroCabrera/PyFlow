# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:/GIT/nodes/PyFlow/Matrix33InputWidget_ui.ui'
#
# Created: Sun Mar 11 18:19:07 2018
#      by: pyside2-uic 2.0.0 running on PySide2 5.6.0~a1
#
# WARNING! All changes made in this file will be lost!

from Qt import QtCompat, QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(221, 72)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setSpacing(7)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSpacing(2)
        self.gridLayout.setObjectName("gridLayout")
        self.dsbm22 = QtWidgets.QDoubleSpinBox(Form)
        self.dsbm22.setMaximumSize(QtCore.QSize(80, 16777215))
        self.dsbm22.setSingleStep(0.1)
        self.dsbm22.setObjectName("dsbm22")
        self.gridLayout.addWidget(self.dsbm22, 1, 1, 1, 1)
        self.dsbm21 = QtWidgets.QDoubleSpinBox(Form)
        self.dsbm21.setMaximumSize(QtCore.QSize(80, 16777215))
        self.dsbm21.setSingleStep(0.1)
        self.dsbm21.setObjectName("dsbm21")
        self.gridLayout.addWidget(self.dsbm21, 1, 0, 1, 1)
        self.dsbm31 = QtWidgets.QDoubleSpinBox(Form)
        self.dsbm31.setMaximumSize(QtCore.QSize(80, 16777215))
        self.dsbm31.setSingleStep(0.1)
        self.dsbm31.setObjectName("dsbm31")
        self.gridLayout.addWidget(self.dsbm31, 2, 0, 1, 1)
        self.dsbm23 = QtWidgets.QDoubleSpinBox(Form)
        self.dsbm23.setMaximumSize(QtCore.QSize(80, 16777215))
        self.dsbm23.setSingleStep(0.1)
        self.dsbm23.setObjectName("dsbm23")
        self.gridLayout.addWidget(self.dsbm23, 1, 2, 1, 1)
        self.dsbm32 = QtWidgets.QDoubleSpinBox(Form)
        self.dsbm32.setMaximumSize(QtCore.QSize(80, 16777215))
        self.dsbm32.setSingleStep(0.1)
        self.dsbm32.setObjectName("dsbm32")
        self.gridLayout.addWidget(self.dsbm32, 2, 1, 1, 1)
        self.dsbm33 = QtWidgets.QDoubleSpinBox(Form)
        self.dsbm33.setMaximumSize(QtCore.QSize(80, 16777215))
        self.dsbm33.setSingleStep(0.1)
        self.dsbm33.setObjectName("dsbm33")
        self.gridLayout.addWidget(self.dsbm33, 2, 2, 1, 1)
        self.dsbm12 = QtWidgets.QDoubleSpinBox(Form)
        self.dsbm12.setMaximumSize(QtCore.QSize(80, 16777215))
        self.dsbm12.setSingleStep(0.1)
        self.dsbm12.setObjectName("dsbm12")
        self.gridLayout.addWidget(self.dsbm12, 0, 1, 1, 1)
        self.dsbm11 = QtWidgets.QDoubleSpinBox(Form)
        self.dsbm11.setMaximumSize(QtCore.QSize(80, 16777215))
        self.dsbm11.setSingleStep(0.1)
        self.dsbm11.setObjectName("dsbm11")
        self.gridLayout.addWidget(self.dsbm11, 0, 0, 1, 1)
        self.dsbm13 = QtWidgets.QDoubleSpinBox(Form)
        self.dsbm13.setMaximumSize(QtCore.QSize(80, 16777215))
        self.dsbm13.setSingleStep(0.1)
        self.dsbm13.setObjectName("dsbm13")
        self.gridLayout.addWidget(self.dsbm13, 0, 2, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.pbReset = QtWidgets.QPushButton(Form)
        self.pbReset.setMaximumSize(QtCore.QSize(25, 25))
        self.pbReset.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/resources/reset.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pbReset.setIcon(icon)
        self.pbReset.setObjectName("pbReset")
        self.verticalLayout.addWidget(self.pbReset)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtCompat.translate("Form", "Form", None, -1))

from .. import nodes_res_rc

