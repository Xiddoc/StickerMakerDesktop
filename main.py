"""
Main script / entry script.
"""
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

	__pack: StickerPack

	def __init__(self) -> None:
		# Initialize main window
		super().__init__()

		# Make sticker pack field
		self.__pack = StickerPack()

		# Allow drops
		self.setAcceptDrops(True)

		# Load the UI from a designer file
		uic.loadUi('stickermaker.ui', self)

		# Initiate shortcut
		self.PasteShortcut = QShortcut(QKeySequence("Ctrl+V"), self)
		self.PasteShortcut.activated.connect(lambda: self.load_image(ImageUtils.load_image_from_clipboard()))

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
			return
		# Otherwise, add the sticker to the pack
		self.__pack.add_sticker_to_pack(image)
		# Update the UI
		self.ImageDrop.setTextFormat("&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;Drag-and-drop a file "
		                             "here&lt;/p&gt;&lt;p&gt;or paste from your "
		                             "Clipboarda&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;")


# Execute on direct run
if __name__ == "__main__":
	# Initialize app frame (required for Qt)
	app = QApplication([])

	# Make a new window
	ui = StickerMakerApp()

	# Execute the app
	app.exec_()
