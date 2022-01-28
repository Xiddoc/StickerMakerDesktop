"""
Sticker Pack class.
"""
from typing import List

from PIL.Image import Image


class StickerPack:
	"""
	Class to help organize and set up the sticker pack.
	"""

	images: List[Image]

	def __init__(self) -> None:
		# Init the list
		self.images = []

	def init_pack(self) -> None:
		"""
		Creates a new 'temp' directory if it doesn't exist,
		or cleans out the directory if it is full of old files.
		"""

	def compress_pack(self, file_path: str) -> None:
		"""
		Compresses the 'temp' directory to a zip file,
		then saves it to the specified location.

		:param file_path: The save path.
		"""
