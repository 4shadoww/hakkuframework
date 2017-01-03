class UnknownCommand(Exception):
	pass

class ModuleNotFound(Exception):
	pass

class VariableError(Exception):
	pass

class ModuleError:
	error = ""

	def __init__(self, error):
		self.error = error