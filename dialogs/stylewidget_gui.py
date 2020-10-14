# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialogs\stylewidget_gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(419, 334)
        self.gridLayout_2 = QtWidgets.QGridLayout(Form)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.combSymbol = QtWidgets.QComboBox(Form)
        self.combSymbol.setObjectName("combSymbol")
        self.gridLayout.addWidget(self.combSymbol, 6, 2, 1, 2)
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 8, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 7, 0, 1, 1)
        self.btnSymBrushColor = QtWidgets.QPushButton(Form)
        self.btnSymBrushColor.setAutoFillBackground(False)
        self.btnSymBrushColor.setObjectName("btnSymBrushColor")
        self.gridLayout.addWidget(self.btnSymBrushColor, 7, 2, 1, 1)
        self.btnSymFillColor = QtWidgets.QPushButton(Form)
        self.btnSymFillColor.setAutoFillBackground(False)
        self.btnSymFillColor.setObjectName("btnSymFillColor")
        self.gridLayout.addWidget(self.btnSymFillColor, 8, 2, 1, 1)
        self.sbSymBrushAlpha = QtWidgets.QSpinBox(Form)
        self.sbSymBrushAlpha.setMaximum(255)
        self.sbSymBrushAlpha.setObjectName("sbSymBrushAlpha")
        self.gridLayout.addWidget(self.sbSymBrushAlpha, 7, 3, 1, 1)
        self.cbSymBrushDefault = QtWidgets.QCheckBox(Form)
        self.cbSymBrushDefault.setObjectName("cbSymBrushDefault")
        self.gridLayout.addWidget(self.cbSymBrushDefault, 7, 4, 1, 1)
        self.cbSymFillDefault = QtWidgets.QCheckBox(Form)
        self.cbSymFillDefault.setObjectName("cbSymFillDefault")
        self.gridLayout.addWidget(self.cbSymFillDefault, 8, 4, 1, 1)
        self.sbSymFillAlpha = QtWidgets.QSpinBox(Form)
        self.sbSymFillAlpha.setMaximum(255)
        self.sbSymFillAlpha.setObjectName("sbSymFillAlpha")
        self.gridLayout.addWidget(self.sbSymFillAlpha, 8, 3, 1, 1)
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 6, 0, 1, 1)
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 3, 0, 1, 1)
        self.btnColor = QtWidgets.QPushButton(Form)
        self.btnColor.setAutoFillBackground(False)
        self.btnColor.setObjectName("btnColor")
        self.gridLayout.addWidget(self.btnColor, 3, 2, 1, 1)
        self.sbAlpha = QtWidgets.QSpinBox(Form)
        self.sbAlpha.setMaximum(255)
        self.sbAlpha.setObjectName("sbAlpha")
        self.gridLayout.addWidget(self.sbAlpha, 3, 3, 1, 1)
        self.cbColor = QtWidgets.QCheckBox(Form)
        self.cbColor.setObjectName("cbColor")
        self.gridLayout.addWidget(self.cbColor, 3, 4, 1, 1)
        self.cbPlotLegend = QtWidgets.QCheckBox(Form)
        self.cbPlotLegend.setObjectName("cbPlotLegend")
        self.gridLayout.addWidget(self.cbPlotLegend, 10, 0, 1, 1)
        self.cbLineWidth = QtWidgets.QCheckBox(Form)
        self.cbLineWidth.setObjectName("cbLineWidth")
        self.gridLayout.addWidget(self.cbLineWidth, 4, 4, 1, 1)
        self.dsbLineWidth = QtWidgets.QDoubleSpinBox(Form)
        self.dsbLineWidth.setDecimals(1)
        self.dsbLineWidth.setSingleStep(0.1)
        self.dsbLineWidth.setObjectName("dsbLineWidth")
        self.gridLayout.addWidget(self.dsbLineWidth, 4, 2, 1, 2)
        self.cbLineType = QtWidgets.QCheckBox(Form)
        self.cbLineType.setObjectName("cbLineType")
        self.gridLayout.addWidget(self.cbLineType, 5, 4, 1, 1)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 5, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 3, 1, 1)
        self.combLineType = QtWidgets.QComboBox(Form)
        self.combLineType.setObjectName("combLineType")
        self.gridLayout.addWidget(self.combLineType, 5, 2, 1, 2)
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 9, 0, 1, 1)
        self.dsbSymSize = QtWidgets.QDoubleSpinBox(Form)
        self.dsbSymSize.setDecimals(1)
        self.dsbSymSize.setSingleStep(0.1)
        self.dsbSymSize.setObjectName("dsbSymSize")
        self.gridLayout.addWidget(self.dsbSymSize, 9, 2, 1, 2)
        self.verticalLayout.addLayout(self.gridLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnSetDefauls = QtWidgets.QPushButton(Form)
        self.btnSetDefauls.setAutoFillBackground(False)
        self.btnSetDefauls.setObjectName("btnSetDefauls")
        self.horizontalLayout.addWidget(self.btnSetDefauls)
        self.btnCancel = QtWidgets.QPushButton(Form)
        self.btnCancel.setAutoFillBackground(False)
        self.btnCancel.setObjectName("btnCancel")
        self.horizontalLayout.addWidget(self.btnCancel)
        self.btnApply = QtWidgets.QPushButton(Form)
        self.btnApply.setAutoFillBackground(False)
        self.btnApply.setObjectName("btnApply")
        self.horizontalLayout.addWidget(self.btnApply)
        self.btnOK = QtWidgets.QPushButton(Form)
        self.btnOK.setAutoFillBackground(False)
        self.btnOK.setObjectName("btnOK")
        self.horizontalLayout.addWidget(self.btnOK)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_7.setText(_translate("Form", "Symbol fill color"))
        self.label_6.setText(_translate("Form", "Symbol brush color"))
        self.btnSymBrushColor.setText(_translate("Form", "Pick color"))
        self.btnSymFillColor.setText(_translate("Form", "Pick color"))
        self.cbSymBrushDefault.setText(_translate("Form", "Set same as line"))
        self.cbSymFillDefault.setText(_translate("Form", "Set same as line"))
        self.label_5.setText(_translate("Form", "Symbol type"))
        self.label.setText(_translate("Form", "Color"))
        self.btnColor.setText(_translate("Form", "Pick color"))
        self.cbColor.setText(_translate("Form", "Default"))
        self.cbPlotLegend.setText(_translate("Form", "Plot legend"))
        self.cbLineWidth.setText(_translate("Form", "Default"))
        self.cbLineType.setText(_translate("Form", "Default"))
        self.label_3.setText(_translate("Form", "Line type"))
        self.label_4.setText(_translate("Form", "Line width"))
        self.label_2.setText(_translate("Form", "Alpha"))
        self.label_8.setText(_translate("Form", "Symbol size"))
        self.btnSetDefauls.setText(_translate("Form", "Set defaults"))
        self.btnCancel.setText(_translate("Form", "Cancel"))
        self.btnApply.setText(_translate("Form", "Apply"))
        self.btnOK.setText(_translate("Form", "OK"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
