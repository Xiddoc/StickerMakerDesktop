"""
Sticker Pack class.
"""
from os import mkdir, listdir
from os.path import exists
from pathlib import Path
from shutil import rmtree
from time import time

from typing import List, Optional
from zipfile import ZipFile
from main import log
from PIL.Image import Image

from packer.ImageUtils import ImageUtils
from structures.Constants import PACK_TEMP_PATH, PACK_TITLE_FILE, PACK_AUTHOR_FILE, DEFAULT_TITLE, DEFAULT_AUTHOR


class StickerPack:
	"""
	Class to help organize and set up the sticker pack.
	"""

	__images: List[Image]
	__tray: Optional[Image]
	__title: str
	__author: str

	def __init__(self) -> None:
		# Initiate the pack for the first time
		self.init_pack()

	def get_pack_size(self) -> int:
		"""
		Returns the size of the pack (the amount of stickers added).
		"""
		return len(self.__images)

	def init_pack(self) -> None:
		"""
		Creates a new 'temp' directory if it doesn't exist,
		or cleans out the directory if it is full of old files.
		"""
		# Clear out the image list
		self.__images = []
		# Set blank tray icon
		self.__tray = None
		# Default metadata
		log.info("Writing default metadata")
		self.__write_data(f"{PACK_TEMP_PATH}/{PACK_TITLE_FILE}", DEFAULT_TITLE)
		self.__write_data(f"{PACK_TEMP_PATH}/{PACK_AUTHOR_FILE}", DEFAULT_AUTHOR)
		# Update the file system and folders
		try:
			# Remove the temp directory
			log.info("Removing directory")
			rmtree(PACK_TEMP_PATH, ignore_errors=True)
			# Make the temp directory
			log.info("Creating new directory")
			mkdir(PACK_TEMP_PATH)
		except FileExistsError:
			# If it already exists, then ignore
			pass

	def add_sticker_to_pack(self, image: Image) -> None:
		"""
		Adds an image to the current sticker pack.
		This is done lazily (so the GUI does not lag), there
		is no file save until we save the entire sticker pack.

		:param image: The image to add.
		"""
		# Add the image to the sticke pack
		log.info("Added image to pack")
		self.__images.append(image)
		# Also, if there is no tray icon, then set this one as it
		if self.__tray is None:
			log.info("Set tray image of pack")
			self.__tray = image

	def save_pack_to_desktop(self) -> None:
		"""
		Compresses the 'temp' directory to a zip file,
		then saves it to the Desktop.
		"""
		# Start by writing each image to the directory
		for image in self.__images:
			# Save sticker
			log.info("Embedded custom sticker in pack")
			ImageUtils.save_to_sticker(image)

		# If we are in a lack of images (at least 3 stickers in a sticker pack)
		# I use the following expression to figure out how many times to loop: max(3 - STICKER_COUNT, 0)
		# This means that if we have less than 3
		# stickers, then it should loop enough
		# times to have saved a total of 3 stickers.
		# However, if there are more than 3 stickers,
		# then it will loop 0 times (add no blank stickers).
		for i in range(max(3 - self.get_pack_size(), 0)):
			# Add blank stickers
			log.info("Embedded blank sticker in pack")
			ImageUtils.create_blank_sticker()

		# Save the tray icon to the pack
		# if there is none, then make a blank one
		if self.__tray is None:
			log.info("Created blank tray for pack")
			ImageUtils.create_blank_tray()
		# Otherwise,
		else:
			# Save the current one as our tray
			log.info("Used custom tray for pack")
			ImageUtils.save_to_tray(self.__tray)

		# Make a new zip file on the desktop
		with ZipFile(self.__get_zip_path(), "w") as f:
			# For each file in the pack
			file_path: str
			for file in listdir(PACK_TEMP_PATH):
				# Add it to the zip
				file_path = f"{PACK_TEMP_PATH}/{file}"
				log.info(f"Added file '{file_path}' to pack")
				f.write(file_path)

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

	@classmethod
	def __get_zip_path(cls) -> str:
		"""
		Generates a random path to save the sticker pack to.
		Always located on the Desktop.
		"""
		# On the desktop
		# Generate a random file name
		# With the file extension .wastickers
		file_name: str = f"{Path.home() / 'Desktop'}/{str(time()).replace('.', '')}.wastickers"
		# If the file exists, recurse to try again
		if exists(file_name):
			return cls.__get_zip_path()
