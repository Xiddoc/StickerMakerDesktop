"""
Image utility functions.
"""
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

	@staticmethod
	def save_to_tray(image: Image) -> None:
		"""
		Crops the image to 96x96 pixels, then saves it to:
		temp/tray.png

		:param image: The image to save.
		"""

	@staticmethod
	def load_image(file_path: str) -> Image:
		"""
		Wrapper for loading an image from a file path.

		:param file_path: The file to load.
		:return: An Image object instance.
		"""


