"""
Sticker Pack class.
"""
from os import mkdir
from shutil import rmtree

from typing import List

from PIL.Image import Image


class StickerPack:
	"""
	Class to help organize and set up the sticker pack.
	"""

	images: List[Image]

	def __init__(self) -> None:
		# Initiate the pack for the first time
		self.init_pack()

	def init_pack(self) -> None:
		"""
		Creates a new 'temp' directory if it doesn't exist,
		or cleans out the directory if it is full of old files.
		"""
		# Clear out the image list
		self.images = []
		try:
			# Remove the temp directory
			rmtree("temp", ignore_errors=True)
			# Make the temp directory
			mkdir("temp")
		except FileExistsError:
			# If it already exists, then ignore
			pass

	def compress_pack(self, file_path: str) -> None:
		"""
		Compresses the 'temp' directory to a zip file,
		then saves it to the specified location.

		:param file_path: The save path.
		"""
