#        Copyright (C) 2015 Noa-Emil Nissinen (4shadoww)


# Import python modules
import sys
import os
import traceback

# Append
sys.path.append(os.path.dirname(os.path.realpath(__file__)))

# Import core modules
from core import command_handler
from core.module_manager import ModuleManager

# Exceptions
import core.exceptions

class Hakkuapi:
	mm = None
	ch = None
	allowPrint = False

	def disablePrint(self):
		if self.allowPrint == False:
			f = open(os.devnull, 'w')
			sys.stdout = f

	def enablePrint(self):
		if self.allowPrint == False:
			sys.stdout = sys.__stdout__

	def __init__(self, allowPrint):
		self.allowPrint = allowPrint
		self.mm = ModuleManager
		self.ch = command_handler.Commandhandler(self.mm, True)

	def loadModule(self, module):
		self.disablePrint()
		try:
			self.ch.handle(["use", module])
			modadd = sys.modules["modules.cloudflare_resolver"]
			if modadd.conf['apisupport'] == False:
				raise ApiNotSupported("this module doesn't support api")
		except core.exceptions.ModuleNotFound:
			self.enablePrint()
			raise ModuleNotFound("error: module not found")
		except:
			self.enablePrint()
			print("unexpected error:")
			traceback.print_exc()

		self.enablePrint()

	def unloadModule(self):
		self.disablePrint()
		try:
			self.ch.handle(["back"])
		except:
			self.enablePrint()
			print("unexpected error:")
			traceback.print_exc()
		self.enablePrint()

	def setVariable(self, target, value):
		self.disablePrint()
		try:
			self.ch.handle(["set", target, value])
		except core.exceptions.VariableError:
			self.enablePrint()
			raise VariableError("error: variable not found")
		except:
			self.enablePrint()
			print("unexpected error:")
			traceback.print_exc()

		self.enablePrint()

	def runModule(self):
		self.disablePrint()
		try:
			answer = self.ch.handle(["run"])
		except:
			self.enablePrint()
			print("unexpected error:")
			traceback.print_exc()
		self.enablePrint()
		return answer

	def customCommand(self, command):
		self.disablePrint()
		try:
			answer = self.ch.handle([command])
		except:
			self.enablePrint()
			print("unexpected error:")
			traceback.print_exc()

		self.enablePrint()
		return answer

class ModuleNotFound(Exception):
	pass

class VariableError(Exception):
	pass

class ApiNotSupported(Exception):
	pass