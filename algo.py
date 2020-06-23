from __future__ import print_function    

import pymysql

import sys
from PyQt5 import QtCore, QtGui, uic, QtWidgets






qtCreatorFile = "algopro.ui" # Enter file here.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):

	def __init__(self):
		QtWidgets.QMainWindow.__init__(self)
		Ui_MainWindow.__init__(self)
		self.setupUi(self)
		self.workpage.setGeometry(QtCore.QRect(0,0,741,521))
		filename,garbage_value_returning_ignore_it=QtWidgets.QFileDialog.getOpenFileName(self,'open a text file')


if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)
	window = MyApp()
	window.show()
	sys.exit(app.exec_())

