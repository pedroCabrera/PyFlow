from Qt.QtWidgets import QApplication,QStyleFactory,QMainWindow
import sys
from os import path
from PyFlow.App import PyFlow

FILE_DIR = path.dirname(__file__)

SETTINGS_PATH = path.join(FILE_DIR, "PyFlow", "appConfig.ini")

STYLE_PATH = path.join(FILE_DIR, "PyFlow", "style.css")

app = QApplication(sys.argv)

app.setStyle(QStyleFactory.create("plastique"))

instance = PyFlow.instance()
app.setActiveWindow(instance)
instance.show()	

try:
    sys.exit(app.exec_())
except Exception as e:
    print(e)
