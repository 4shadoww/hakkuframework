from core import bcolors
import sys
from glob import glob
from core.messages import *

def check():
	global funcname

	print(bcolors.YEL+'\nchecking',funcname.modulename+bcolors.END)

	funcname.version
	if funcname.desc == 'modules_description':
		print(bcolors.WARNING+'\ndesc variable has default value'+bcolors.END)
		testfailed()
	if funcname.github == 'mygithub':
			print(bcolors.WARNING+'\ngithub variable has default value'+bcolors.END)
			testfailed()
	if funcname.createdby == 'creators_name':
		print(bcolors.WARNING+'\ncreatedby variable has default value'+bcolors.END)
		testfailed()
	if funcname.email == 'creators@email.com':
		print(bcolors.WARNING+'\nemail variable has default value'+bcolors.END)
		testfailed()

	for item in funcname.variables.items():
		if item[0] == 'option1' or item[0] == 'option2' or item[1] == 'none1' or item[1] == 'none2':
			print(bcolors.WARNING+'\nvariables has default value')
			testfailed()

	for desc in funcname.vdesc:
		if desc == 'description1' or desc == 'description2':
			print(bcolors.WARNING+'\ndesc list has default value'+bcolors.END)
			testfailed()
	if len(funcname.variables) != len(funcname.vdesc):
		print(bcolors.WARNING+'\nvdesc has not same amount of items than variables')
		testfailed()

	funcname.changelog
	funcname.run

	print(bcolors.OKGREEN+'\n[*] test passed'+bcolors.END)

	try:
		funcname.customcommands
		check_customcommands()
	except AttributeError:
		pass