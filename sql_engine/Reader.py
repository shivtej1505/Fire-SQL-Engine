class Reader:
	def __init__(self, metadataFilename):
		self.metadataFilename = metadataFilename

	def printMetadata(self):
		metadataFile = open(self.metadataFilename, 'r')
		print(metadataFile.read())