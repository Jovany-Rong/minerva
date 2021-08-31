# coding: utf-8

import sys
import ctypes
import os
if hasattr(sys, 'frozen'):
    os.environ['PATH'] = sys._MEIPASS + ";" + os.environ['PATH']
    
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from views.main import Minerva

if __name__ == '__main__':
    try:
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("MinervaOCRTool")
    except:
        pass

    app = QApplication(sys.argv)
    
    mainWindow = Minerva()
    mainWindow.showNormal()
    
    sys.exit(app.exec_())