from core.exceptions import UnknownCommand
from core import cmethods
from core.module_manager import ModuleManager
from core import colors

class Commandhandler:
	mm = None
	notcommand = ["init", "mcu"]
	cm = None

	def __init__(self, gmm):
		self.mm = gmm
		self.cm = cmethods.Cmethods(self.mm)

	def handle(self, command):
		if self.mm.moduleLoaded == 1:
				try:
					self.cm.mcu(command[0])
					return
				except IndexError:
					return
				except UnknownCommand:
					pass

		# Validate command

		if command[0] in self.notcommand:
			print(colors.red+"unknown command"+colors.end)
			return
		try:
			method = getattr(self.cm, command[0])
		except AttributeError:
			print(colors.red+"unknown command"+colors.end)
			return
		except IndexError:
			return

		try:
			method(command[1:])
		except UnknownCommand:
			print(colors.red+"unknown command"+colors.end)