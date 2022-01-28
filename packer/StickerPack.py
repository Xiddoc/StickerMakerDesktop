"""
Sticker Pack class.
"""
from os import mkdir, listdir
from shutil import rmtree

from typing import List
from zipfile import ZipFile

from PIL.Image import Image

from structures.Constants import TEMP_LOCATION


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
			rmtree(TEMP_LOCATION, ignore_errors=True)
			# Make the temp directory
			mkdir(TEMP_LOCATION)
		except FileExistsError:
			# If it already exists, then ignore
			pass

	@staticmethod
	def save_pack(file_path: str) -> None:
		"""
		Compresses the 'temp' directory to a zip file,
		then saves it to the specified location.

		:param file_path: The save path.
		"""
		# Make a new zip file
		with ZipFile(file_path, "w") as f:
			# For each file in the pack
			for file in listdir(TEMP_LOCATION):
				# Add it to the zip
				f.write(f"{TEMP_LOCATION}/{file}")
