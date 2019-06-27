# Input widgets for pins
from Qt import QtCore
from Qt.QtWidgets import *

from PyFlow.Core.Common import *
from PyFlow.UI.Canvas.UICommon import DEFAULT_WIDGET_VARIANT
from PyFlow.UI.Widgets.InputWidgets import *
from PyFlow.UI.Widgets.QtSliders import pyf_Slider

FLOAT_SINGLE_STEP = 0.01
FLOAT_DECIMALS = 5


def _configDoubleSpinBox(sb):
    sb.setDecimals(FLOAT_DECIMALS)
    sb.setRange(FLOAT_RANGE_MIN, FLOAT_RANGE_MAX)
    sb.setSingleStep(FLOAT_SINGLE_STEP)
    sb.setDisplayMinimun(0)
    sb.setDisplayMaximum(10)


def _configIntSpinBox(sb):
    sb.setRange(INT_RANGE_MIN, INT_RANGE_MAX)
    sb.setDisplayMinimun(0)
    sb.setDisplayMaximum(10)


class ExecInputWidget(InputWidgetSingle):
    """docstring for ExecInputWidget"""

    def __init__(self, parent=None, **kwds):
        super(ExecInputWidget, self).__init__(parent=parent, **kwds)
        self.pb = QPushButton('execute', self)
        self.setWidget(self.pb)
        self.pb.clicked.connect(self.dataSetCallback)

    def blockWidgetSignals(self, bLocked):
        pass


class FloatInputWidget(InputWidgetSingle):
    """
    Floating point data input widget
    """

    def __init__(self, parent=None, **kwds):
        super(FloatInputWidget, self).__init__(parent=parent, **kwds)
        self.sb = pyf_Slider(self, "float", style=1)
        _configDoubleSpinBox(self.sb)
        self.sb.setDisplayMinimun(0)
        self.sb.setDisplayMaximum(10)
        self.setWidget(self.sb)
        # when spin box updated call setter function
        self.sb.valueChanged.connect(lambda val: self.dataSetCallback(val))

    def blockWidgetSignals(self, bLocked):
        self.sb.blockSignals(bLocked)

    def setWidgetValue(self, val):
        self.sb.setValue(float(val))

    def setMaximum(self,max):
        self.sb.setMaximum(max)

    def setMinimum(self,min):
        self.sb.setMinimum(min)

class IntInputWidget(InputWidgetSingle):
    """
    Decimal number input widget
    """

    def __init__(self, parent=None, **kwds):
        super(IntInputWidget, self).__init__(parent=parent, **kwds)
        self.sb = pyf_Slider(self, "int", style=1)
        _configIntSpinBox(self.sb)
        self.setWidget(self.sb)
        self.sb.valueChanged.connect(self.dataSetCallback)

    def blockWidgetSignals(self, bLocked):
        self.sb.blockSignals(bLocked)

    def setWidgetValue(self, val):
        self.sb.setValue(int(val))


class StringInputWidget(InputWidgetSingle):
    """
    String data input widget
    """

    def __init__(self, parent=None, **kwds):
        super(StringInputWidget, self).__init__(parent=parent, **kwds)
        self.le = QLineEdit(self)
        self.le.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.setWidget(self.le)
        self.le.editingFinished.connect(lambda : self.dataSetCallback(self.le.text()))

    def blockWidgetSignals(self, bLocked):
        self.le.blockSignals(bLocked)

    def setWidgetValue(self, val):
        self.le.setText(str(val))


class PathInputWidget(InputWidgetSingle):
    """
    Path input widget
    """

    def __init__(self, parent=None, **kwds):
        super(PathInputWidget, self).__init__(parent=parent, **kwds)
        self.content = QWidget()
        self.content.setContentsMargins(0, 0, 0, 0)
        self.pathLayout = QHBoxLayout(self.content)
        self.pathLayout.setContentsMargins(0, 0, 0, 0)
        self.le = QLineEdit()
        self.le.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.pathLayout.addWidget(self.le)
        self.pbGetPath = QPushButton("...")
        self.pbGetPath.clicked.connect(self.getPath)
        self.pathLayout.addWidget(self.pbGetPath)
        self.setWidget(self.content)
        self.le.textChanged.connect(lambda val: self.dataSetCallback(val))

    def getPath(self):
        directory = QFileDialog.getExistingDirectory(None, "Select dir", "")
        self.le.setText(directory)

    def blockWidgetSignals(self, bLocked):
        self.le.blockSignals(bLocked)

    def setWidgetValue(self, val):
        self.le.setText(str(val))


class BoolInputWidget(InputWidgetSingle):
    """Boolean data input widget"""

    def __init__(self, parent=None, **kwds):
        super(BoolInputWidget, self).__init__(parent=parent, **kwds)
        self.cb = QCheckBox(self)
        self.setWidget(self.cb)
        self.cb.stateChanged.connect(
            lambda val: self.dataSetCallback(bool(val)))

    def blockWidgetSignals(self, bLocked):
        self.cb.blockSignals(bLocked)

    def setWidgetValue(self, val):
        if bool(val):
            self.cb.setCheckState(QtCore.Qt.Checked)
        else:
            self.cb.setCheckState(QtCore.Qt.Unchecked)


class NoneInputWidget(InputWidgetSingle):
    """
    String data input widget
    """

    def __init__(self, parent=None, **kwds):
        super(NoneInputWidget, self).__init__(parent=parent, **kwds)
        self.le = QLineEdit(self)
        self.le.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.setWidget(self.le)
        self.le.textChanged.connect(lambda val: self.dataSetCallback(val))
        self.le.setEnabled(False)

    def blockWidgetSignals(self, bLocked):
        self.le.blockSignals(bLocked)

    def setWidgetValue(self, val):
        self.le.setText(str(val))


def getInputWidget(dataType, dataSetter, defaultValue, widgetVariant=DEFAULT_WIDGET_VARIANT):
    '''
    factory method
    '''
    if dataType == 'FloatPin':
        return FloatInputWidget(dataSetCallback=dataSetter, defaultValue=defaultValue)
    if dataType == 'IntPin':
        return IntInputWidget(dataSetCallback=dataSetter, defaultValue=defaultValue)
    if dataType == 'StringPin':
        if widgetVariant == DEFAULT_WIDGET_VARIANT:
            return StringInputWidget(dataSetCallback=dataSetter, defaultValue=defaultValue)
        elif widgetVariant == "PathWidget":
            return PathInputWidget(dataSetCallback=dataSetter, defaultValue=defaultValue)
    if dataType == 'BoolPin':
        return BoolInputWidget(dataSetCallback=dataSetter, defaultValue=defaultValue)
    if dataType == 'ExecPin':
        return ExecInputWidget(dataSetCallback=dataSetter, defaultValue=None)
    if dataType == 'AnyPin':
        return NoneInputWidget(dataSetCallback=dataSetter, defaultValue=None)
