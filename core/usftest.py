from core import colors
import traceback, sys, os
from modules import *
import glob
import py_compile


def check_customcommands():
	global modadd
	try:
		modadd.mhelp
	except AttributeError:
		testfailed()

def challenge():
	try:
		global modadd
		modules = glob.glob("modules/*.py")
		core = glob.glob("core/*.py")
		libs1 = glob.glob("core/libs/*.p")
		libs2 = glob.glob("core/libs/*/*.py")

		print(colors.green+"\nstarting challenge"+colors.green)
		print(colors.green+"\ntesting modules\n"+colors.green)

		# Testing modules
		for module in modules:
			module = module.replace('modules/', '').replace('.py', '')
			if module != '__init__':
				modadd = globals()[module]
				print(colors.yellow+'checking',modadd.name+colors.green)
				if modadd.name != module:
					print(colors.red+"\nmodules name doesn't match")
				modadd.version
				if modadd.desc == 'modules_description':
					print(colors.red+'\ndesc variable has default value'+colors.green)
					testfailed()
				if modadd.github == 'mygithub':
					 print(colors.red+'\ngithub variable has default value'+colors.green)
					 testfailed()
				if modadd.createdby == 'creators_name':
					print(colors.red+'\ncreatedby variable has default value'+colors.green)
					testfailed()
				if modadd.email == 'creators@email.com':
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
					check_customcommands()
				except AttributeError:
					pass
		# Testing core
		print(colors.green+'\ntesting core...\n'+colors.green)

		for item in core:
			print(colors.yellow+'compiling',item+colors.green)
			py_compile.compile(item)
		
		# Testing libs
		print(colors.green+'\ntesting libs...\n'+colors.green)

		for lib in libs1:
			print(colors.yellow+'compiling',lib+colors.green)
			py_compile.compile(lib)
		
		for lib in libs2:
			print(colors.yellow+'compiling',lib+colors.green)
			py_compile.compile(lib)

		print(colors.green+"test passed!"+colors.end)

		sys.exit(0)

	except SystemExit as e:
		sys.exit(e)

	except:
		testfailed()

def testfailed():
	print(colors.red+"\ntest not passed!\n")
	traceback.print_exc()
	print(colors.green)
	sys.exit(1)
