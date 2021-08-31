# coding: utf-8

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from forms.Ui_mainWindow import Ui_MainWindow
from views.core import *
from views.maps import *

import cv2
import os

class Minerva(QMainWindow, Ui_MainWindow):
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.setWindowIcon(QIcon("lib/src/icon.png"))
        
        self.actionAbout_Minerva.triggered.connect(self.about_minerva)
        self.btnCopy.clicked.connect(self.copy_text)
        self.btnSave.clicked.connect(self.save_text_to_file)
        
        self.btnFromCb.clicked.connect(self.convert_from_clipboard)
        self.btnFromFile.clicked.connect(self.convert_from_file)
        
    def convert_from_clipboard(self):
        img = load_img_from_clipboard()
        if not img:
            QMessageBox.information(self, "Info", "No picture in the clipboard.")
            return
        
        self.convert_to_text(img)
        self.show_image()
        
    def convert_from_file(self):
        fileName, fileType = QFileDialog.getOpenFileName(self, "Select a picture", os.getcwd(), 
        "Picture Files (*.png *.jpeg *.jpg *.webp *.bmp)")
        
        if fileName == "":
            return
        
        img = load_img_from_file(fileName)
        if not img:
            QMessageBox.information(self, "Info", "It's not a picture.")
            return
        
        self.convert_to_text(img)
        self.show_image()
        
    
    def convert_to_text(self, img):
        lang = LANGUAGES[self.comboBoxLang.currentIndex()]
        text = img_to_txt(img, lang)
        self.textBrowser.clear()
        self.textBrowser.append(text)
        
    def show_image(self):
        img = cv2.imread("temp.png")
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        x = img.shape[1]
        y = img.shape[0]
        frame = QImage(img, x, y, x*3, QImage.Format_RGB888)
        pix = QPixmap.fromImage(frame)
        self.graphicsView.item = QGraphicsPixmapItem(pix)
        self.graphicsView.scene = QGraphicsScene()
        self.graphicsView.scene.addItem(self.graphicsView.item)
        self.graphicsView.setScene(self.graphicsView.scene)
        
    def copy_text(self):
        text = self.textBrowser.toPlainText()
        clipboard = QApplication.clipboard()
        clipboard.setText(text)
        
    def about_minerva(self):
        text = """Minerva %s

Minerva is a OCR tool which can get text from pictures. It has complete functions even if there is no network.

Author: Jovany Rong
        """ % (VERSION)
        
        QMessageBox.about(self, "About", text)
        
    def save_text_to_file(self):
        text = self.textBrowser.toPlainText()
        fileName, fileType = QFileDialog.getSaveFileName(self, "Save", os.getcwd(), 
        "All Files (*);;Text Files (*.txt)")
        
        if fileName != "":
            with open(fileName, "w+", encoding="utf-8") as f:
                f.write(text)
                QMessageBox.information(self, "Info", "Text saved to file: %s." % fileName)