#		 Copyright (C) 2015 Noa-Emil Nissinen (4shadoww)

# Import python modules
import readline
import sys

# Import core modules
from core import cmethods
from core.module_manager import ModuleManager
from core import colors
from core.exceptions import UnknownCommand

shellface = "usf"
mm = ModuleManager


def run(scripting, scf):
	global shellface
	global mm

	scriptline = 0
	notcommand = ["init", "mcu"]

	cmethods.init(mm)

	while True:
		try:
			if scripting == 1:
				if scriptline == len(scf):
					sys.exit(0)

				
				command = scf[scriptline][0].split()
				scriptline += 1
			else:
				setFace()
				command = input(colors.purple+shellface+colors.end+" > ")
				command = command.split()

			if mm.moduleLoaded == 1:
				try:
					cmethods.mcu(command[0])
					continue
				except IndexError:
					continue
				except UnknownCommand:
					pass

			# Validate command

			if command[0] in notcommand:
				print(colors.red+"unknown command"+colors.end)
				continue
			try:
				method = getattr(cmethods, command[0])
			except AttributeError:
				print(colors.red+"unknown command"+colors.end)
				continue
			except IndexError:
				continue

			try:
				method(command[1:])
			except UnknownCommand:
				print(colors.red+"unknown command"+colors.end)
		except KeyboardInterrupt:
			if mm.moduleLoaded == 0:
				print()
				sys.exit(0)
			else:
				print()
				mm.moduleLoaded = 0
				mm.moduleName = ""
				print(colors.green + "ctrl + c detected going back..." + colors.end)

def setFace():
	global shellface
	global mm
	if mm.moduleLoaded == 0:
		shellface = "usf"
	else:
		shellface = "usf:"+mm.moduleName