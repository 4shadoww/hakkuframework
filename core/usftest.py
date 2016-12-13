from core import colors
import traceback, sys, os
from modules import *
import glob
import py_compile
from core import getpath

def check_modules():
	modules = glob.glob(getpath.modules()+"*.py")

	for module in modules:
		module = module.replace(getpath.modules(), '').replace('.py', '')
		if module != '__init__':
			modadd = globals()[module]
			print(colors.yellow+'checking',modadd.conf["name"]+colors.green)
			if modadd.conf["name"] != module:
				print(colors.red+"\nmodules name doesn't match")
			modadd.conf["version"]
			if modadd.conf["shortdesc"] == 'modules_description':
				print(colors.red+'\ndesc variable has default value'+colors.green)
				testfailed()
			if modadd.conf["github"] == 'mygithub':
				 print(colors.red+'\ngithub variable has default value'+colors.green)
				 testfailed()
			if modadd.conf["author"] == 'creators_name':
				print(colors.red+'\ncreatedby variable has default value'+colors.green)
				testfailed()
			if modadd.conf["email"] == 'creators@email.com':
				print(colors.red+'\nemail variable has default value'+colors.green)
				testfailed()

			for item in modadd.variables.items():
				if item[0] == 'option1' or item[0] == 'option2' or item[1] == 'none1' or item[1] == 'none2':
					print(colors.red+'\nvariables has default value')
					testfailed()

			for desc in modadd.vdesc:
				if desc == 'description1' or desc == 'description2':
					print(colors.red+'\ndesc list has default value'+colors.green)
					testfailed()
			if len(modadd.variables) != len(modadd.vdesc):
				print(colors.red+'\nvdesc has not same amount of items than variables')
				testfailed()

			modadd.changelog
			modadd.run
			try:
				modadd.customcommands
				check_customcommands(modadd)
			except AttributeError:
				pass

def check_customcommands(modadd):
	try:
		modadd.mhelp
	except AttributeError:
		testfailed()

	if len(modadd.mhelp) != len(modadd.customcommands):
		print(len(modadd.mhelp), len(modadd.customcommands))
		print(colors.red+"customcommands doesn't have same amount items as mhelp"+colors.end)
		testfailed()

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

def compile_libs():
	libs1 = glob.glob(getpath.libs()+"*.p")
	libs2 = glob.glob(getpath.libs()+"*/*.py")

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
		compile_libs()
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
