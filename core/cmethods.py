#		 Copyright (C) 2015 Noa-Emil Nissinen (4shadoww)

# Import python modules

import sys
import os
from collections import OrderedDict
import imp
import traceback
import curses
import time

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
import core.cowsay
from core import dsag
import core.matrix
import core.touchingsky
from core import getpath
from core import usftest

# Import modules
from modules import *

class Cmethods:

	# Module manager object

	mm = None
	modadd = None

	# Init

	def __init__(self, mmi):
		self.mm = mmi

	# Module custom commands

	def mcu(self, command):

		try:
			if command[0] in self.modadd.customcommands:
				call = getattr(self.modadd, command[0])
				try:
					call(command[1:])
				except Exception as e:
					print(colors.red+"error: module is corrupted\n")
					traceback.print_exc(file=sys.stdout)
					print(colors.end)
			else:
				raise UnknownCommand("unknown command")
		except AttributeError:
			raise UnknownCommand("unknown command")

	# Built in commands

	def exit(self, args):
		if self.mm.moduleLoaded == 1:
			self.mm.moduleLoaded = 0
			self.mm.moduleName = ""
		else:
			sys.exit()

	def clear(self, args):
		sys.stderr.write("\x1b[2J\x1b[H")

	def cl(self, args):
		os.system(' '.join(args))

	def help(self, args):

		if self.mm.moduleLoaded == 0:
			print(helptable.generateTable(helpin.commands))
		else:
			try: 
				print(helptable.generatemTable(helpin.mcommands, self.modadd.mhelp))
			except AttributeError:
				print(helptable.generateTable(helpin.mcommands))
			try:
				print('\n',self.modadd.help_notes,'\n')
			except AttributeError:
				pass

	def version(self, args):

		if self.mm.moduleLoaded == 1:
			print(self.modadd.conf["name"]+" "+self.modadd.conf["version"])
		else:
			print("µSploit Framework " + info.version)

	def ifconfig(self, args):
		os.system("ifconfig"+" "+' '.join(args))

	def scan(self, args):
		network_scanner.scan()

	def about(self, args):
		if self.mm.moduleLoaded == 1:
			try:
				print(self.modadd.conf["name"]+" "+self.modadd.conf["version"])
				print("created by: "+self.modadd.conf["author"])
				print("github: "+self.modadd.conf["github"])
				print("email: "+self.modadd.conf["email"])
				print("description: "+self.modadd.conf["shortdesc"])
			except:
				print(colors.red+"error: module is corrupted\n")
				traceback.print_exc(file=sys.stdout)
				print(colors.end)
		else:
			print(info.about)

	def changelog(self, args):
		if self.mm.moduleLoaded == 1:
			try:
				print(colors.yellow+self.modadd.changelog+colors.end)
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
			except IOError:
				print(colors.red + "error: changelog file not found (have you removed it?)" + colors.end)

	def use(self, args):
		if self.mm.moduleLoaded == 0:
			try:
				self.modadd = globals()[args[0]]
				self.mm.moduleLoaded = 1
				self.mm.setName(self.modadd.conf["name"])
				try:
					if self.modadd.conf["outdated"] == 1:
						print(colors.red + "this module is outdated and might not be working" + colors.end)
				except KeyError:
					pass
				try:
					if self.modadd.conf["needroot"] == 1:
						if not os.geteuid() == 0:
							print(colors.red+"this module requires root permissions for full functionality!"+colors.end)
				except KeyError:
					pass
				try:
					self.modadd.init()
				except AttributeError:
					pass
			except KeyError:
				print(colors.red + "module not found" + colors.end)
			except IndexError:
				print(colors.red + "please enter module name" + colors.end)
		else:
			raise UnknownCommand("module in use")

	def show(self, args):
		try:
			if args[0] == "modules" and self.mm.moduleLoaded == 0:
				t = PrettyTable([colors.green+'Modules:', ''+colors.end])
				t.add_row(['',''])
				t.align = 'l'
				t.valing = 'm'
				t.border = False

				for key, val in module_database.database.items():
						t.add_row([key, val])

				print (t)
			elif args[0] == "options" and self.mm.moduleLoaded == 1:
				moduleop.printoptions(self.modadd)
			else:
				raise UnknownCommand("module not loaded or unknown command")
		except IndexError:
			raise UnknownCommand("unknown command")

	def back(self, args):
		if self.mm.moduleLoaded == 1:
			self.mm.moduleLoaded = 0
			self.mm.moduleName = ""
		else:
			raise UnknownCommand("unknown command")

	def reload(self, args):
		if self.mm.moduleLoaded == 0:
			try:
				mod = "modules."+args[0]
				imp.reload(sys.modules[mod])
				sys.modules[mod]
				print (colors.green+"module "+ args[0] +" reloaded"+colors.end)
			except IndexError:
				print (colors.red+"please enter module's name"+colors.end)
			except KeyError:
				print (colors.red+"module not found"+colors.end)
		else:
			try:
				mod = "modules."+args[0]
				imp.reload(sys.modules[mod])
				sys.modules[mod]
				print (colors.green+"module "+ args[0] +" reloaded"+colors.end)
			except IndexError:
				mod = "modules."+self.mm.moduleName
				imp.reload(sys.modules[mod])
				sys.modules[mod]
				print (colors.green+"module "+ self.mm.moduleName +" reloaded"+colors.end)
			except KeyError:
				print (colors.red+"module not found"+colors.end)

	def run(self, args):

		if self.mm.moduleLoaded == 1:
			try:
				self.modadd.run()
			except Exception as error:
				print(colors.red+"error: module is corrupted\n")
				traceback.print_exc(file=sys.stdout)
				print(colors.end)
		else:
			raise UnknownCommand("module not loaded")

	def set(self, args):
		try:
			targetvariable = self.modadd.variables[args[0]]
			self.modadd.variables[args[0]] = args[1]
			print(colors.green+args[0] +" => "+ args[1] + colors.end)

		except (NameError, KeyError):
			print(colors.red + "option not found" + colors.end)
		except IndexError:
			print(colors.red + "please enter variable's value" + colors.end)

	def new(self, args):
		try:
			if args[0] == "module":
				try:
					completeName = os.path.join(getpath.modules(), args[1]+".py")
					if os.path.exists(completeName):
						print(colors.red+"module already exists"+colors.end)

					else:
						mfile = open(completeName, 'w')
						template = os.path.join('core', 'module_template')
						f = open(template, 'r')
						template_contents = f.readlines()
						template_contents[5] = "	\"name\": \""+args[1]+"\", # Module's name (should be same as file name)\n"
						template_contents[11] = "	\"initdate\": \""+(time.strftime("%d.%m.%Y"))+"\", # Initial date\n"
						mfile.writelines(template_contents)
						mfile.close()
						print(colors.green+"module "+ args[1] +".py" +" created to modules folder"+colors.end)
						print(colors.green+"done"+colors.end)

				except IndexError:
					print(colors.red + "please enter module's name" + colors.end)

				except PermissionError:
					print(colors.red + "error: permission denied" + colors.end)

				except IOError:
					print(colors.red + "something went wrong" + colors.end)

			else:
				raise UnknownCommand("unknown command")
		except IndexError:
			raise UnknownCommand("unkown command")

	def check(self, args):
		try:
			if args[0] == "module":
				try:
					self.modadd = globals()[args[1]]
					print(colors.green+"module found"+colors.end)
					usftest.check_module(self.modadd)
					print(colors.green+"\ntest passed"+colors.end)

				except IndexError:
					print(colors.red + "please enter module name"+ colors.end)

				except KeyError:
					print(colors.red+"error: module not found"+colors.end)

				except:
					print(colors.red + "error:\n")
					traceback.print_exc(file=sys.stdout)
					print(colors.end)
			else:
				raise UnknownCommand("unknown command")
		except IndexError:
			raise UnknownCommand("unkown command")

	def matrix(self, args):
		try:
			core.matrix.main()
		except KeyboardInterrupt:
			curses.endwin()
			curses.curs_set(1)
			curses.reset_shell_mode()
			curses.echo()

	def cowsay(self, args):
		try:
			message = ' '.join(args)
			print(core.cowsay.cowsay(message))
			return
		except ValueError:
			print(core.cowsay.cowsay("µSploit Framework"))

	def ds(self, args):
		print(dsag.darkside)

	def make(self, args):
		try:
			if args[0] == "exit":
				sys.exit(0)
			else:
				raise UnknownCommand("unkown command")
		except IndexError:
			raise UnknownCommand("unkown command")

	def touchingsky(self, args):
		core.touchingsky.main()