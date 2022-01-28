"""
Sticker Pack class.
"""
from os import mkdir, listdir
from shutil import rmtree

from typing import List, Optional
from zipfile import ZipFile

from PIL.Image import Image

from structures.Constants import PACK_TEMP_PATH, PACK_TITLE_FILE, PACK_AUTHOR_FILE


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
			rmtree(PACK_TEMP_PATH, ignore_errors=True)
			# Make the temp directory
			mkdir(PACK_TEMP_PATH)
		except FileExistsError:
			# If it already exists, then ignore
			pass

	def update_metadata(self, pack_title: Optional[str] = None, pack_author: Optional[str] = None) -> None:
		"""
		Updates the metadata files within the sticker pack.

		:param pack_title: The sticker pack title.
		:param pack_author: The sticker pack author.
		"""
		# If param was passed
		if pack_title is not None:
			# Write to pack title
			self.__write_data(f"{PACK_TEMP_PATH}/{PACK_TITLE_FILE}", pack_title)

		# If param was passed
		if pack_author is not None:
			# Write to pack title
			self.__write_data(f"{PACK_TEMP_PATH}/{PACK_AUTHOR_FILE}", pack_author)

	@staticmethod
	def __write_data(file_name: str, data: str) -> None:
		"""
		Wrapper function for writing data to a file.
		Overwrites the file and closes the stream before returning.

		:param file_name: The file to write to.
		:param data: The data to write to the file.
		"""
		# Simple write operation
		with open(file_name, "w") as f:
			f.write(data)


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
			for file in listdir(PACK_TEMP_PATH):
				# Add it to the zip
				f.write(f"{PACK_TEMP_PATH}/{file}")
