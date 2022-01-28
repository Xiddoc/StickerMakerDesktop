"""
Main script / entry script.
"""
from PIL.Image import Image
from qtpy import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton, QShortcut
from PyQt5.QtGui import QDragEnterEvent, QDropEvent, QDragMoveEvent, QKeySequence


# noinspection PyUnusedFunction
class StickerMakerApp(QMainWindow):
	"""
	Main window and app for the GUI.
	"""

	ImageDrop: QLabel
	SaveToFile: QPushButton
	CopyToClipboard: QPushButton
	PasteShortcut: QShortcut

	def __init__(self) -> None:
		# Initialize main window
		super().__init__()

		# Allow drops
		self.setAcceptDrops(True)

		# Load the UI from a designer file
		uic.loadUi('stickermaker.ui', self)

		# Initiate shortcut
		self.PasteShortcut = QShortcut(QKeySequence("Ctrl+V"), self)
		self.PasteShortcut.activated.connect(lambda: self.load_image())

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

	def load_image(self, image: Image) -> None:
		"""
		Loads an image into the packer.
		Then, it updates the UI.

		:param image: The image to add to the sticker pack.
		"""


# Execute on direct run
if __name__ == "__main__":
	# Initialize app frame (required for Qt)
	app = QApplication([])

	# Make a new window
	ui = StickerMakerApp()

	# Execute the app
	app.exec_()
