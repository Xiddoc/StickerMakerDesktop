"""
Main script / entry script.
"""
import logging
from typing import Optional

from packer.StickerPack import StickerPack
from packer.ImageUtils import ImageUtils
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
	QuitShortcut: QShortcut

	__pack: StickerPack

	def __init__(self) -> None:
		# Initialize main window
		super().__init__()

		# Make sticker pack field
		log.info("Initializing sticker pack")
		self.__pack = StickerPack()

		# Allow drops
		self.setAcceptDrops(True)

		# Load the UI from a designer file
		log.info("Loading UI")
		uic.loadUi('stickermaker.ui', self)

		# Initiate shortcut
		log.info("Initializing pasting shortcut")
		self.PasteShortcut = QShortcut(QKeySequence("Ctrl+V"), self)
		self.PasteShortcut.activated.connect(lambda: self.load_image(ImageUtils.load_image_from_clipboard()))

		# Initiate shortcut
		log.info("Initializing quitting shortcut")
		self.QuitShortcut = QShortcut(QKeySequence("Ctrl+W"), self)
		# noinspection PyTypeChecker
		self.QuitShortcut.activated.connect(self.close)

		# Show the window
		log.info("Displaying window")
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
		log.info("File dropped on window")
		if event.mimeData().hasUrls():
			# Get the file path to the image
			file_path: str = event.mimeData().urls()[0].toLocalFile()

			print(file_path)

			# Valid
			event.accept()
		else:
			# Invalid
			event.ignore()

	def load_image(self, image: Optional[Image]) -> None:
		"""
		Loads an image into the packer.
		Then, it updates the UI.

		This method accounts for the possibility that the image is None, and simply ignores.
		(For simplicity with the ImageUtils.load_image_from_clipboard() method)

		:param image: The image to add to the sticker pack.
		"""
		# Simply ignore if there is no picture to load
		if image is None:
			log.info("User pasted text to the window")
			return

		# Otherwise, add the sticker to the pack
		log.info("User pasted an image to the window")
		self.__pack.add_sticker_to_pack(image)
		# Update the UI
		self.ImageDrop.setText('<html><head/><body>'
		                       f'<p>{self.__pack.get_pack_size()} stickers added.</p>'
		                       '<p>Want to add more?</p>'
		                       '</body></html>')


# Execute on direct run
if __name__ == "__main__":
	# Set logger settings
	logging.basicConfig(level=logging.INFO, format="[%(levelname)s] %(message)s")
	# Make logger
	log = logging.getLogger("Logger")

	# Initialize app frame (required for Qt)
	log.info("Creating application frame")
	app = QApplication([])

	# Make a new window
	log.info("Initializing application")
	ui = StickerMakerApp()

	# Execute the app
	log.info("Executing application using frame")
	app.exec_()
