"""
Main script / entry script.
"""

from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication, QSizePolicy, QWidget, QVBoxLayout, QLayout, QLabel, QPushButton, \
	QHBoxLayout


class StickerMakerApp(QMainWindow):
	"""
	Main window and app for the GUI.
	"""

	def __init__(self) -> None:
		# Initialize main window
		super().__init__()

		self.Main = QWidget(self)
		size_policy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
		
		size_policy.setHeightForWidth(self.Main.sizePolicy().hasHeightForWidth())
		self.Main.setSizePolicy(size_policy)

		self.verticalLayoutWidget = QWidget(self.Main)
		self.verticalLayoutWidget.setGeometry(QtCore.QRect(-1, -1, 641, 481))
		self.Vertical = QVBoxLayout(self.verticalLayoutWidget)
		self.Vertical.setSizeConstraint(QLayout.SetMaximumSize)
		self.Vertical.setContentsMargins(0, 0, 0, 0)

		self.ImageDrop = QLabel(self.verticalLayoutWidget)
		size_policy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
		size_policy.setHeightForWidth(self.ImageDrop.sizePolicy().hasHeightForWidth())
		self.ImageDrop.setSizePolicy(size_policy)
		self.ImageDrop.setMinimumSize(QtCore.QSize(0, 400))
		font = QtGui.QFont()
		font.setFamily("Segoe UI")
		font.setPointSize(28)
		self.ImageDrop.setFont(font)
		self.ImageDrop.setAcceptDrops(True)
		self.ImageDrop.setText("<html><head/><body>"
		                       "<p>Drag-and-drop a file here</p>"
		                       "<p>or paste from your Clipboard</p>"
		                       "</body></html>")
		self.ImageDrop.setAlignment(QtCore.Qt.AlignCenter)

		self.Vertical.addWidget(self.ImageDrop)
		self.Buttons = QHBoxLayout()
		self.Buttons.setSizeConstraint(QLayout.SetMaximumSize)
		self.Buttons.setSpacing(0)

		self.SaveToFile = QPushButton(self.verticalLayoutWidget)
		size_policy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
		size_policy.setHeightForWidth(self.SaveToFile.sizePolicy().hasHeightForWidth())
		self.SaveToFile.setSizePolicy(size_policy)
		font = QtGui.QFont()
		font.setFamily("Segoe UI")
		font.setPointSize(24)
		self.SaveToFile.setFont(font)
		self.SaveToFile.setText("Save to file")

		self.Buttons.addWidget(self.SaveToFile)
		self.CopyToClipboard = QPushButton(self.verticalLayoutWidget)
		size_policy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
		size_policy.setHeightForWidth(self.CopyToClipboard.sizePolicy().hasHeightForWidth())
		self.CopyToClipboard.setSizePolicy(size_policy)
		font = QtGui.QFont()
		font.setFamily("Segoe UI")
		font.setPointSize(24)
		self.CopyToClipboard.setFont(font)
		self.CopyToClipboard.setText("Copy to Clipboard")

		self.Buttons.addWidget(self.CopyToClipboard)
		self.Vertical.addLayout(self.Buttons)
		self.setCentralWidget(self.Main)

		# Create a size policy for the window
		size_policy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
		size_policy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
		self.setSizePolicy(size_policy)
		# Resize the window (fixed)
		self.resize(640, 480)
		# Name the window
		self.setWindowTitle("Sticker Maker [Desktop]")
		# Show the window
		self.show()


# Execute on direct run
if __name__ == "__main__":
	# Initialize app frame (required for Qt)
	app = QApplication([])

	# Make a new window
	ui = StickerMakerApp()

	# Execute the app
	app.exec_()
