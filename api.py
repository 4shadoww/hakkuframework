import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)))
from core import command_handler
from core.module_manager import ModuleManager

class Hakkuapi:
	mm = None
	ch = None

	def disablePrint(self):
		f = open(os.devnull, 'w')
		sys.stdout = f

	def enablePrint(self):
		sys.stdout = sys.__stdout__

	def __init__(self):
		self.mm = ModuleManager
		self.ch = command_handler.Commandhandler(self.mm, True)

	def loadModule(self, module):
		self.disablePrint()
		self.ch.handle(["use", module])
		self.enablePrint()

	def unloadModule(self):
		self.disablePrint()
		self.ch.handle(["back"])
		self.enablePrint()

	def setVariable(self, target, value):
		self.disablePrint()
		self.ch.handle(["set", target, value])
		self.enablePrint()

	def runModule(self):
		self.disablePrint()
		answer = self.ch.handle(["run"])
		self.enablePrint()
		return answer

	def customCommand(self, command):
		self.disablePrint()
		answer = self.ch.handle([command])
		self.enablePrint()
		return answer
		