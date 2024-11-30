import sys, io

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton

template = """
<?xml version="1.0" encoding="UTF-8"?>
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
   <widget class="QPushButton" name="pushButton">
    <property name="geometry">
     <rect>
      <x>-50</x>
      <y>240</y>
      <width>891</width>
      <height>391</height>
     </rect>
    </property>
    <property name="text">
     <string>Это кнопка которая делает очень много контента просто не жать ее лучше чем нажать и получить минус вайб не жми</string>
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


class tester(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(template)
        uic.loadUi(f, self)
        self.btn = QPushButton(self)
        self.btn.clicked.connect(self.run())

    def run(self):
        print("кружочек рандомного размера")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = tester()
    ex.show()
    sys.exit(app.exec())
