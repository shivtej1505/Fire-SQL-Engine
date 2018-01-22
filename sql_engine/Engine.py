from Reader import Reader
from Parser import Parser

class Engine:
	"""SQL Engine"""
	def __init__(self, prompt, metadataFilename):
		self.parser = Parser(prompt)

		self.dbReader = Reader(metadataFilename)
		self.dbReader.printMetadata()

	def run(self):
		while True:
		 	query = self.parser.getTokens()
		 	if query == "exit":
		 		print("Bye")
		 		break
		 	else:
		 		print(query)

if __name__ == "__main__":
	engine = Engine("jaggu", "metadata.txt")
	engine.run()