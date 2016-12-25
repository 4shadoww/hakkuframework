from core import colors
import traceback, sys, os
from modules import *
import glob
import py_compile
from core import getpath
import importlib

def check_modules():
	modules = glob.glob(getpath.modules()+"*.py")

	for module in modules:
		module = module.replace(getpath.modules(), '').replace('.py', '')
		if module != '__init__':
			modadd = importlib.import_module("modules."+module)
			check_module(modadd)

def check_module(modadd):
	print(colors.yellow+'checking',modadd.conf["name"]+colors.green)
	module = modadd.__name__.replace("modules.", "")
	if modadd.conf["name"] != module:
		print(colors.red+"\nmodules name doesn't match")
	modadd.conf["version"]
	if modadd.conf["shortdesc"] == 'none':
		print(colors.red+'\ndesc variable has default value'+colors.green)
		testfailed()
	if modadd.conf["github"] == 'none':
		 print(colors.red+'\ngithub variable has default value'+colors.green)
		 testfailed()
	if modadd.conf["author"] == 'none':
		print(colors.red+'\ncreatedby variable has default value'+colors.green)
		testfailed()
	if modadd.conf["email"] == 'none':
		print(colors.red+'\nemail variable has default value'+colors.green)
		testfailed()

	if modadd.conf["initdate"] == "none":
		print(colors.red+'\ninitdate variable has default value'+colors.green)
		testfailed()

	try:
		if modadd.conf["dependencies"][0] == None:
			print(colors.red+"\ndependencies has default value")
			testfailed()
	except KeyError:
		pass

	modadd.variables.items()

	modadd.conf["apisupport"]
	modadd.changelog
	modadd.run
	try:
		modadd.customcommands
		check_customcommands(modadd)
	except AttributeError:
		pass


def check_customcommands(modadd):

	f = open(modadd.__file__, "r")
	for line in f:
		for c in modadd.customcommands:
			if c in line and "def" in line and "#" not in line and "args" not in line:
				print(colors.red+"custom command function doesn't have args argument"+colors.end)
				testfailed()
	f.close()


def compile_core():
	core = glob.glob(getpath.core()+"*.py")

	print(colors.green+'\ntesting core...\n'+colors.green)

	for item in core:
		print(colors.yellow+'compiling',item+colors.green)
		py_compile.compile(item)

def compile_lib():
	libs1 = glob.glob(getpath.lib()+"*.p")
	libs2 = glob.glob(getpath.lib()+"*/*.py")

	print(colors.green+'\ntesting libs...\n'+colors.green)

	for lib in libs1:
		print(colors.yellow+'compiling',lib+colors.green)
		py_compile.compile(lib)
	
	for lib in libs2:
		print(colors.yellow+'compiling',lib+colors.green)
		py_compile.compile(lib)

def check_cmethods():

	print(colors.green+"\ntesting cmethods...\n"+colors.end)

	fcm = open(getpath.core()+"cmethods.py", "r")

	linenum = 1

	for line in fcm:
		if "self" not in line and "def " in line or "args" not in line and "def " in line:
			if "__init__" not in line and "mcu" not in line and "#" not in line:
				print(colors.red+"error in line "+str(linenum)+":\n"+colors.end)
				print(colors.red+line+colors.end)
				testfailed()
		linenum += 1


def challenge():
	try:
		print(colors.green+"\nstarting challenge"+colors.green)
		print(colors.green+"\ntesting modules\n"+colors.green)

		check_modules()
		compile_core()		
		compile_lib()
		check_cmethods()

		print(colors.green+"test passed!"+colors.end)

		sys.exit(0)

	except SystemExit as e:
		sys.exit(e)

	except:
		print(colors.red+"\ntest not passed!\n")
		traceback.print_exc()
		print(colors.end)
		sys.exit(1)

def testfailed():
	print(colors.red+"\ntest not passed!\n"+colors.end)
	sys.exit(1)
