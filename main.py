"""
Main script / entry script.
"""
from qtpy import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton
from PyQt5.QtGui import QDragEnterEvent, QDropEvent, QDragMoveEvent


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

		# Allow drops
		self.setAcceptDrops(True)

		# Load the UI from a designer file
		uic.loadUi('stickermaker.ui', self)

		# Show the window
		self.show()

	def dragEnterEvent(self, event: QDragEnterEvent) -> None:
		"""
		Fired when a file is dragged over the UI.
		"""
		# Accept it to pass to next event
		event.accept()

	def dragMoveEvent(self, event: QDragMoveEvent) -> None:
		"""
		Fired when a file is moved over the UI.
		"""
		# Accept it to pass to next event
		event.accept()

	def dropEvent(self, event: QDropEvent) -> None:
		"""
		Fired when a file is dropped on the UI.
		"""
		# If the dropped object is a file
		if event.mimeData().hasUrls():
			# Get the file path to the image
			file_path: str = event.mimeData().urls()[0].toLocalFile()

			print(file_path)

			# Valid
			event.accept()
		else:
			# Invalid
			event.ignore()


# Execute on direct run
if __name__ == "__main__":
	# Initialize app frame (required for Qt)
	app = QApplication([])

	# Make a new window
	ui = StickerMakerApp()

	# Execute the app
	app.exec_()
