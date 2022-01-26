"""
Main script / entry script.
"""

from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton
from qtpy import uic


class StickerMakerApp(QMainWindow):
	"""
	Main window and app for the GUI.
	"""

	ImageDrop: QLabel
	SaveToFile: QPushButton
	CopyToClipboard: QPushButton

	def __init__(self) -> None:
		# Initialize main window
		super().__init__()

		# Load the UI from a designer file
		uic.loadUi('stickermaker.ui', self)

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
