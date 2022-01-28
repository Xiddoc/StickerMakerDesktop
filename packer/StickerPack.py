"""
Sticker Pack class.
"""
from os import mkdir, listdir
from shutil import rmtree

from typing import List, Optional
from zipfile import ZipFile

from PIL.Image import Image

from packer.ImageUtils import ImageUtils
from structures.Constants import PACK_TEMP_PATH, PACK_TITLE_FILE, PACK_AUTHOR_FILE


class StickerPack:
	"""
	Class to help organize and set up the sticker pack.
	"""

	__images: List[Image]
	__title: str
	__author: str

	def __init__(self) -> None:
		# Initiate the pack for the first time
		self.init_pack()

	def init_pack(self) -> None:
		"""
		Creates a new 'temp' directory if it doesn't exist,
		or cleans out the directory if it is full of old files.
		"""
		# Clear out the image list
		self.__images = []
		# Default metadata
		self.update_metadata("_", "_")
		# Update the file system and folders
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

	def add_sticker_to_pack(self, image: Image) -> None:
		"""
		Adds an image to the current sticker pack.
		This is done lazily (so the GUI does not lag), there
		is no file save until we save the entire sticker pack.

		:param image: The image to add.
		"""
		self.__images.append(image)

	def save_pack(self, file_path: str) -> None:
		"""
		Compresses the 'temp' directory to a zip file,
		then saves it to the specified location.

		:param file_path: The save path.
		"""
		# Start by writing each image to the directory
		for image in self.__images:
			# Save sticker
			ImageUtils.save_to_sticker(image)

		# If we are in a lack of images (at least 3 stickers in a sticker pack)
		# I use the following expression to figure out how many times to loop: max(3 - STICKER_COUNT, 0)
		# This means that if we have less than 3
		# stickers, then it should loop enough
		# times to have saved a total of 3 stickers.
		# However, if there are more than 3 stickers,
		# then it will loop 0 times (add no blank stickers).
		for i in range(max(3 - len(self.__images), 0)):
			# Add blank stickers
			ImageUtils.create_blank_sticker()

		# Make a new zip file
		with ZipFile(file_path, "w") as f:
			# For each file in the pack
			for file in listdir(PACK_TEMP_PATH):
				# Add it to the zip
				f.write(f"{PACK_TEMP_PATH}/{file}")

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
