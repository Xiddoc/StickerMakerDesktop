"""
Packer utility functions.
"""


class PackerUtils:
	"""
	Utility functions to help organize the sticker pack.
	"""

	@staticmethod
	def init_pack() -> None:
		"""
		Creates a new 'temp' directory if it doesn't exist,
		or cleans out the directory if it is full of old files.
		"""

	@staticmethod
	def compress_pack(file_path: str) -> None:
		"""
		Compresses the 'temp' directory to a zip file,
		then saves it to the specified location.

		:param file_path: The save path.
		"""
