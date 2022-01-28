"""
Image utility functions.
"""
from os.path import exists
from time import time
from typing import Optional

from PIL import ImageGrab
from PIL import Image as PILImage
from PIL.Image import Image

from structures.Constants import STICKER_RES, TRAY_RES, TEMP_LOCATION


class ImageUtils:
	"""
	Static functions for image utilities.
	"""

	@classmethod
	def save_to_sticker(cls, image: Image) -> None:
		"""
		Crops the image to 512x512 pixels, then saves it to:
		temp/[RANDOM_INTEGER].webp

		:param image: The image to save.
		"""
		# Resize the image to the respective pixel size
		# Then save to the designated location
		image \
			.resize(STICKER_RES, PILImage.ANTIALIAS) \
			.save(cls.__get_random_file_name())

	@classmethod
	def create_blank_sticker(cls) -> None:
		"""
		Creates a blank sticker (transparent background), then saves it.
		"""
		# Make a new blank sticker
		# Save it using our method
		return cls.save_to_sticker(PILImage.new("RGBA", STICKER_RES, (0, 0, 0, 0)))

	@staticmethod
	def save_to_tray(image: Image) -> None:
		"""
		Crops the image to 96x96 pixels, then saves it to:
		temp/tray.png

		:param image: The image to save.
		"""
		# Resize the image to the respective pixel size
		# Then save to the designated location
		image \
			.resize(TRAY_RES, PILImage.ANTIALIAS) \
			.save(f"{TEMP_LOCATION}/tray.png")

	@staticmethod
	def load_image_from_file(file_path: str) -> Image:
		"""
		Wrapper for loading an image from a file path.

		:param file_path: The file to load.
		:return: An Image object instance.
		"""
		return PILImage.open(file_path)

	@staticmethod
	def load_image_from_clipboard() -> Optional[Image]:
		"""
		Wrapper for loading an image from the current Clipboard.

		:return: An Image object instance **IF THERE IS AN IMAGE ON THE CLIPBOARD**, otherwise None.
		"""
		return ImageGrab.grabclipboard()

	@classmethod
	def __get_random_file_name(cls) -> str:
		"""
		Creates a random image name that does not exist.
		"""
		# Generate random file name
		file_name: str = f"{TEMP_LOCATION}/{str(time()).replace('.', '')}.png"
		# If file exists, recurse to try again
		if exists(file_name):
			return cls.__get_random_file_name()
