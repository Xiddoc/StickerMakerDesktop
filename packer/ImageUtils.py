"""
Image utility functions.
"""
from PIL import ImageGrab
from PIL import Image as PILImage
from PIL.Image import Image


class ImageUtils:
	"""
	Static functions for image utilities.
	"""

	@staticmethod
	def save_to_sticker(image: Image) -> None:
		"""
		Crops the image to 512x512 pixels, then saves it to:
		temp/[RANDOM_INTEGER].webp

		:param image: The image to save.
		"""

	@classmethod
	def create_blank_sticker(cls) -> None:
		"""
		Creates a blank sticker (transparent background), then saves it.
		"""
		# Make a new blank sticker
		# Save it using our method
		return cls.save_to_sticker(PILImage.new("RGBA", (512, 512), (0, 0, 0, 0)))

	@staticmethod
	def save_to_tray(image: Image) -> None:
		"""
		Crops the image to 96x96 pixels, then saves it to:
		temp/tray.png

		:param image: The image to save.
		"""

	@staticmethod
	def load_image_from_file(file_path: str) -> Image:
		"""
		Wrapper for loading an image from a file path.

		:param file_path: The file to load.
		:return: An Image object instance.
		"""
		return PILImage.open(file_path)

	@staticmethod
	def load_image_from_clipboard() -> Image:
		"""
		Wrapper for loading an image from the current Clipboard.

		:return: An Image object instance.
		"""
		return ImageGrab.grabclipboard()


