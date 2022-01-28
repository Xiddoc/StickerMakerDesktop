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

# Set logger settings
logging.basicConfig(level=logging.INFO, format="[%(levelname)s] %(message)s")
# Make logger
log = logging.getLogger("Logger")


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

		# Declare shortcut callback
		log.info("Initializing pasting shortcut")
		self.PasteShortcut = QShortcut(QKeySequence("Ctrl+V"), self)
		self.PasteShortcut.activated.connect(lambda: self.load_image(ImageUtils.load_image_from_clipboard()))

		# Declare shortcut callback
		log.info("Initializing quitting shortcut")
		self.QuitShortcut = QShortcut(QKeySequence("Ctrl+W"), self)
		# noinspection PyTypeChecker
		self.QuitShortcut.activated.connect(self.close)

		# Declare button click callback
		self.SaveToFile.clicked.connect(self.__pack.save_pack_to_desktop)

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

			# Load the image
			image_file: Optional[Image] = ImageUtils.load_image_from_file(file_path)

			# If the image was loaded
			if image_file is not None:
				log.info("Dropped file was an image")

				# Add image to pack
				self.__pack.add_sticker_to_pack(image_file)

				# Update UI
				self.update_UI()

				# Valid
				event.accept()
			else:
				log.info("Dropped file was not an image")

				# Update UI
				self.update_UI(error=True)

				# Invalid
				event.ignore()
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
		# Update UI
		self.update_UI()

	def update_UI(self, error: bool = False) -> None:
		"""
		Simple method to update the text with the new sticker pack size.
		"""
		log.info("Updated UI with new pack size")

		# Create informational message
		info_msg = \
			'<span style="font-size: 18pt; color:#AA0000"><b>Not an image.</b></span>' \
				if error else \
				'<span style="font-size: 18pt; color:#00AA00"><b>Image added successfully!</b></span>'

		# Update the UI text
		self.ImageDrop.setText(
			'<html><head/><body>'
			f'<p>{self.__pack.get_pack_size()} stickers added.</p>'
			'<p>Want to add more?</p>'
			f'{info_msg}'
			'</body></html>'
		)


# Execute on direct run
if __name__ == "__main__":
	# Initialize app frame (required for Qt)
	log.info("Creating application frame")
	app = QApplication([])

	# Make a new window
	log.info("Initializing application")
	ui = StickerMakerApp()

	# Execute the app
	log.info("Executing application using frame")
	app.exec_()
