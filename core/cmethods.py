#		 Copyright (C) 2015 Noa-Emil Nissinen (4shadoww)

# Import python modules

import sys
import os
from collections import OrderedDict
import imp
import traceback
import curses

# Import core modules

from core import helptable
from core import helpin
from core import info
from core import network_scanner
from core import colors
from core.exceptions import UnknownCommand
from core import moduleop
from core.prettytable import PrettyTable
from core import module_database
from core import check_module
import core.cowsay
from core import dsag
import core.matrix

# Import modules
from modules import *

# Module manager object

global mm

# Init

def init(mmi):
	global mm
	mm = mmi

# Module custom commands

def mcu(command):
	global modadd

	try:
		if command in modadd.customcommands:
			try:
				modadd.terminal = terminal
			except NameError:
				pass
			call = getattr(modadd, command)
			try:
				call()
			except Exception as e:
				print(colors.red+"error: module is corrupted\n")
				traceback.print_exc(file=sys.stdout)
				print(colors.end)
		else:
			raise UnknownCommand("unknown command")
	except AttributeError:
		raise UnknownCommand("unknown command")

# Built in commands

def exit(args):
	if mm.moduleLoaded == 1:
		mm.moduleLoaded = 0
		mm.moduleName = ""
	else:
		sys.exit()

def clear(args):
	sys.stderr.write("\x1b[2J\x1b[H")
def use(args):
	global mm
	mm.loadModule()
	mm.setName(args[0])

def cl(args):
	os.system(' '.join(args))

def help(args):
	global modadd

	if mm.moduleLoaded == 0:
		print(helptable.generateTable(helpin.commands))
	else:
		try: 
			print(helptable.generatemTable(helpin.mcommands, modadd.mhelp))
		except AttributeError:
			print(helptable.generateTable(helpin.mcommands))
		try:
			print('\n',modadd.help_notes,'\n')
		except(AttributeError):
			pass

def version(args):
	print("µSploit Framework " + info.version)

def ifconfig(args):
	os.system("ifconfig"+" "+' '.join(args))

def scan(args):
	network_scanner.scan()

def about(args):
	print(info.about)

def changelog(args):
	global modadd
	if mm.moduleLoaded == 1:
		try:
			print(colors.yellow+modadd.changelog+colors.end)
		except Exception as error:
			print(colors.red+"error: module is corrupted\n")
			traceback.print_exc(file=sys.stdout)
			print(colors.end)
	else:
		try:
			f = open('changelog', 'r')
			file_contents = f.read()
			print (colors.yellow+file_contents+colors.end)
			f.close()
		except(IOError):
			print(colors.red + "error: changelog file not found (have you removed it?)" + colors.end)

def use(args):
	global modadd
	if mm.moduleLoaded == 0:
		try:
			modadd = globals()[args[0]]
			mm.moduleLoaded = 1
			mm.setName(modadd.name)
			try:
				if modadd.outdated == 1:
					print(colors.red+"this module is outdated and might not be working"+colors.end)
			except (AttributeError):
				pass
			try:
				if modadd.needroot == 1:
					if not os.geteuid() == 0:
						print(colors.red+"this module requires root permissions for full functionality!"+colors.end)
			except(AttributeError):
				pass
			try:
				modadd.init()
			except(AttributeError):
				pass
		except KeyError:
			print(colors.red + "module not found" + colors.end)
		except IndexError:
			print(colors.red + "please enter module name" + colors.end)
	else:
		raise UnknownCommand("module in use")

def show(args):
	try:
		if args[0] == "modules" and mm.moduleLoaded == 0:
			t = PrettyTable([colors.green+'Modules:', ''+colors.end])
			t.add_row(['',''])
			t.align = 'l'
			t.valing = 'm'
			t.border = False

			for key, val in module_database.database.items():
					t.add_row([key, val])

			print (t)
		elif args[0] == "options" and mm.moduleLoaded == 1:
			moduleop.printoptions(modadd)
		else:
			raise UnknownCommand("module not loaded or unknown command")
	except IndexError:
		raise UnknownCommand("unknown command")

def back(args):
	if mm.moduleLoaded == 1:
		mm.moduleLoaded = 0
		mm.moduleName = ""
	else:
		raise UnknownCommand("unknown command")

def reload(args):
	if mm.moduleLoaded == 0:
		try:
			mod = "modules."+args[0]
			imp.reload(sys.modules[mod])
			sys.modules[mod]
			print (colors.green+"module "+ args[0] +" reloaded"+colors.end)
		except(IndexError):
			print (colors.red+"please enter module's name"+colors.end)
		except(KeyError):
			print (colors.red+"module not found"+colors.end)
	else:
		try:
			mod = "modules."+args[0]
			imp.reload(sys.modules[mod])
			sys.modules[mod]
			print (colors.green+"module "+ args[0] +" reloaded"+colors.end)
		except(IndexError):
			mod = "modules."+mm.moduleName
			imp.reload(sys.modules[mod])
			sys.modules[mod]
			print (colors.green+"module "+ mm.moduleName +" reloaded"+colors.end)
		except(KeyError):
			print (colors.red+"module not found"+colors.end)

def run(args):
	global modadd

	if mm.moduleLoaded == 1:
		try:
			modadd.run()
		except Exception as error:
			print(colors.red+"error: module is corrupted\n")
			traceback.print_exc(file=sys.stdout)
			print(colors.end)
	else:
		raise UnknownCommand("module not loaded")

def set(args):
	global modadd
	try:
		targetvariable = modadd.variables[args[0]]
		modadd.variables[args[0]] = args[1]
		print(colors.green+args[0] +" => "+ args[1] + colors.end)

	except(NameError, KeyError):
		print(colors.red+"option not found"+colors.end)
	except(IndexError):
		print(colors.red+"please enter variable's value"+colors.end)

def new(args):
	try:
		if args[0] == "module":
			try:
				completeName = os.path.join('modules', args[1]+".py")
				if os.path.exists(completeName):
					print(colors.red+"module already exists"+colors.end)

				else:
					mfile = open(completeName, 'w')
					template = os.path.join('core', 'module_template')
					f = open(template, 'r')
					template_contents = f.readlines()
					template_contents[7] = 'name = "'+args[1]+'"\n'
					mfile.writelines(template_contents)
					mfile.close()
					print(colors.green+"module "+ args[1] +".py" +" created to modules folder"+colors.end)
					print(colors.green+"done"+colors.end)
			except(IOError):
				print(colors.red+"something went wrong"+colors.end)

			except(IndexError):
				print(colors.red + "please enter module name"+ colors.end)
		else:
			raise UnknownCommand("unknown command")
	except IndexError:
		raise UnknownCommand("unkown command")

def check(args):
	try:
		if args[0] == "module":
			try:
				modadd = globals()[args[1]]
				print(colors.green+"module found"+colors.end)
				check_module.modadd = modadd
				check_module.check()

			except(IndexError):
				print(colors.red + "please enter module name"+ colors.end)

			except Exception as error:
				print(colors.red + "error: module not found ("+str(error)+")"+ colors.end)
		else:
			raise UnknownCommand("unknown command")
	except IndexError:
		raise UnknownCommand("unkown command")

def matrix(args):
	try:
		core.matrix.main()
	except KeyboardInterrupt:
		curses.endwin()
		curses.curs_set(1)
		curses.reset_shell_mode()
		curses.echo()

def cowsay(args):
	try:
		message = ' '.join(args)
		print(core.cowsay.cowsay(message))
		return
	except(ValueError):
		print(core.cowsay.cowsay("µSploit Framework"))

def ds(args):
	print(dsag.darkside)

def make(args):
	try:
		if args[0] == "exit":
			sys.exit(0)
		else:
			raise UnknownCommand("unkown command")
	except IndexError:
		raise UnknownCommand("unkown command")