class Parser():
	"""docstring for Parser"""
	def __init__(self, prompt):
		self.prompt = prompt

	def getInput(self):
		input = raw_input(self.prompt + "> ")
		return input

	def getTokens(self):
		return self.getInput()		