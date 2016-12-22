#		 Copyright (C) 2015 Noa-Emil Nissinen (4shadoww)

# Import python modules

import sys
import os
from collections import OrderedDict
import imp
import traceback
import curses
import time
import importlib

# Import getpath for lib path
from core import getpath

# Append lib path
sys.path.append(getpath.lib())

# Import core modules

from core import helptable
from core import helpin
from core import info
from core import colors
from core import moduleop
from core.prettytable import PrettyTable
from core import module_database
import core.cowsay
from core import dsag
import core.matrix
import core.touchingsky
from core.hftest import check_module
from core import update
from core import mscop

# Import exceptions
from core.exceptions import UnknownCommand
from core.exceptions import ModuleNotFound
from core.exceptions import VariableError

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
			if command[0] in self.modadd.customcommands.keys():
				call = getattr(self.modadd, command[0])
				try:
					return call(command[1:])
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
		if len(args) != 0 and args[0] == "tmp":
			mscop.clear_tmp()
		else:
			sys.stderr.write("\x1b[2J\x1b[H")

	def cl(self, args):
		os.system(' '.join(args))

	def help(self, args):

		if self.mm.moduleLoaded == 0:
			print(helptable.generateTable(helpin.commands))
		else:
			try: 
				print(helptable.generatemTable(helpin.mcommands, self.modadd.customcommands))
			except AttributeError:
				print(helptable.generateTable(helpin.mcommands))
			try:
				print('\n',self.modadd.help_notes,'\n')
			except AttributeError:
				pass

	def version(self, args):
		if self.mm.moduleLoaded == 1:
			try:
				print(self.modadd.conf["name"]+" "+self.modadd.conf["version"])
			except:
				print(colors.red+"error: module is corrupted\n")
				traceback.print_exc(file=sys.stdout)
				print(colors.end)
		else:
			print("Hakku Framework " + info.version)

	def ifconfig(self, args):
		os.system("ifconfig"+" "+' '.join(args))

	def scan(self, args):
		network_scanner = importlib.import_module("core.network_scanner")
		network_scanner.scan()
		del network_scanner

	def about(self, args):
		if self.mm.moduleLoaded == 1:
			try:
				print(self.modadd.conf["name"]+" "+self.modadd.conf["version"])
				print("author: "+self.modadd.conf["author"])
				print("github: "+self.modadd.conf["github"])
				print("email: "+self.modadd.conf["email"])
				print("description: "+self.modadd.conf["shortdesc"])
				print("initial date: "+self.modadd.conf["initdate"])
				if self.modadd.conf["apisupport"] == True:
					support = "supported"
				else:
					support = "not supported"
				print("api support: "+support)
			except:
				print(colors.red+"error: module is corrupted\n")
				traceback.print_exc(file=sys.stdout)
				print(colors.end)
		else:
			print(info.about)

	def changelog(self, args):
		if self.mm.moduleLoaded == 1:
			try:
				print(self.modadd.changelog)
			except:
				print(colors.red+"error: module is corrupted\n")
				traceback.print_exc(file=sys.stdout)
				print(colors.end)
		else:
			try:
				f = open('changelog', 'r')
				file_contents = f.read()
				print (file_contents)
				f.close()
			except IOError:
				print(colors.red + "error: changelog file not found (have you removed it?)" + colors.end)

	def use(self, args):
		if self.mm.moduleLoaded == 0:
			try:
				self.modadd = importlib.import_module("modules."+args[0])
				self.mm.moduleLoaded = 1
				self.mm.setName(self.modadd.conf["name"])
				try:
					print(self.modadd.conf["message"])
				except KeyError:
					pass
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
			except ImportError:
				print(colors.red + "module not found" + colors.end)
				raise ModuleNotFound("module not found")
			except IndexError:
				print(colors.red + "please enter module name" + colors.end)
				raise ModuleNotFound("module not found")
			except:
				print(colors.red+"error: module is corrupted\n")
				traceback.print_exc(file=sys.stdout)
				print(colors.end)
		else:
			raise UnknownCommand("module in use")

	def show(self, args):
		try:
			if args[0] == "modules" and self.mm.moduleLoaded == 0:
				t = PrettyTable([colors.bold+'Modules:', ''+colors.end])
				t.add_row(['',''])
				t.align = 'l'
				t.valing = 'm'
				t.border = False

				for key, val in module_database.database.items():
						t.add_row([key, val])

				print (t)
			elif args[0] == "options" and self.mm.moduleLoaded == 1:
				try:
					moduleop.printoptions(self.modadd)
				except:
					print(colors.red+"error: module is corrupted\n")
					traceback.print_exc(file=sys.stdout)
					print(colors.end)
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
				print (colors.bold+"module "+ args[0] +" reloaded"+colors.end)
			except IndexError:
				print (colors.red+"please enter module's name"+colors.end)
			except KeyError:
				print (colors.red+"module not found or not loaded"+colors.end)
		else:
			try:
				mod = "modules."+args[0]
				imp.reload(sys.modules[mod])
				sys.modules[mod]
				print (colors.bold+"module "+ args[0] +" reloaded"+colors.end)
			except IndexError:
				mod = "modules."+self.mm.moduleName
				imp.reload(sys.modules[mod])
				sys.modules[mod]
				print (colors.bold+"module "+ self.mm.moduleName +" reloaded"+colors.end)
			except KeyError:
				print (colors.red+"module not found or loaded"+colors.end)

	def run(self, args):

		if self.mm.moduleLoaded == 1:
			try:
				return self.modadd.run()

			except KeyboardInterrupt:
				print(colors.red+"module terminated"+colors.end)
			except:
				print(colors.red+"error: module is corrupted\n")
				traceback.print_exc(file=sys.stdout)
				print(colors.end)
		else:
			raise UnknownCommand("module not loaded")

	def set(self, args):
		try:
			self.modadd.variables[args[0]][0] = args[1]
			print(colors.bold+args[0] +" => "+ str(args[1]) + colors.end)

		except (NameError, KeyError):
			print(colors.red + "option not found" + colors.end)
			raise VariableError("option not found")
		except IndexError:
			print(colors.red + "please enter variable's value" + colors.end)
			raise VariableError("no value")
		except:
			print(colors.red+"error: module is corrupted\n")
			traceback.print_exc(file=sys.stdout)
			print(colors.end)

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
						print(colors.bold+"module "+ args[1] +".py" +" created to modules folder"+colors.end)
						print(colors.bold+"done"+colors.end)

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
					self.modadd = importlib.import_module("modules."+args[1])
					print(colors.green+"module found"+colors.end)
					check_module(self.modadd)
					print(colors.green+"\ntest passed"+colors.end)

				except IndexError:
					print(colors.red + "please enter module name"+ colors.end)

				except ImportError:
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
			print(core.cowsay.cowsay("Hakku Framework"))

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

	def update(self, args):
		if update.check_for_updates() == True:
			try:
				update.update()
			except PermissionError:
				print(colors.red+"error: permission denied"+colors.end)

			except Exception as error:
				print(colors.red+"error: "+str(error)+colors.end)

	def loaded(self, args):
		print(sys.modules.keys())