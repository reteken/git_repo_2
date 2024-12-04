import sys, math, io

from PyQt6 import uic

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow

template = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>800</width>
    <height>600</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QTextBrowser" name="textBrowser">
    <property name="geometry">
     <rect>
      <x>80</x>
      <y>30</y>
      <width>621</width>
      <height>161</height>
     </rect>
    </property>
   </widget>
   <widget class="QPushButton" name="btn">
    <property name="geometry">
     <rect>
      <x>460</x>
      <y>470</y>
      <width>201</width>
      <height>51</height>
     </rect>
    </property>
    <property name="text">
     <string>Данные кофе достай ежик</string>
    </property>
   </widget>
   <widget class="QLineEdit" name="lineEdit">
    <property name="geometry">
     <rect>
      <x>120</x>
      <y>470</y>
      <width>181</width>
      <height>51</height>
     </rect>
    </property>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>800</width>
     <height>26</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>
"""


class Umome(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(template)
        uic.loadUi(f, self)

    def run(self):
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Umome()
    ex.show()
    sys.exit(app.exec())
