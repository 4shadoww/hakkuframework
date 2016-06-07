from core import bcolors

def check():
	global funcname

	try:
		funcname.modulename
		print(bcolors.OKGREEN+"[OK] modulename variable exists"+bcolors.END)
	except(AttributeError):
		print(bcolors.WARNING + "[FAIL] modulename variable does't exists" + bcolors.END)
	try:
		funcname.version
		print(bcolors.OKGREEN+"[OK] version variable exists"+bcolors.END)
	except(AttributeError):
		print(bcolors.WARNING + "[FAIL] version variable does't exists" + bcolors.END)
	try:
		funcname.desc
		print(bcolors.OKGREEN+"[OK] desc variable exists"+bcolors.END)
	except(AttributeError):
		print(bcolors.WARNING + "[FAIL] desc variable does't exists" + bcolors.END)
	try:
		funcname.github
		print(bcolors.OKGREEN+"[OK] github variable exists"+bcolors.END)
	except(AttributeError):
		print(bcolors.WARNING + "[FAIL] github variable does't exists" + bcolors.END)
	try:
		funcname.createdby
		print(bcolors.OKGREEN+"[OK] createdby variable exists"+bcolors.END)
	except(AttributeError):
		print(bcolors.WARNING + "[FAIL] createdby variable does't exists" + bcolors.END)
	try:
		funcname.email
		print(bcolors.OKGREEN+"[OK] email variable exists"+bcolors.END)
	except(AttributeError):
		print(bcolors.WARNING + "[FAIL] email variable does't exists" + bcolors.END)
	try:
		funcname.variables
		print(bcolors.OKGREEN+"[OK] variables list exists"+bcolors.END)
	except(AttributeError):
		print(bcolors.WARNING + "[FAIL] variables list does't exists" + bcolors.END)
	try:
		funcname.vdesc
		print(bcolors.OKGREEN+"[OK] variables description list exists"+bcolors.END)
	except(AttributeError):
		print(bcolors.WARNING + "[FAIL] variables description list does't exists" + bcolors.END)
	try:
		funcname.changelog
		print(bcolors.OKGREEN+"[OK] changelog variable exists"+bcolors.END)
	except(AttributeError):
		print(bcolors.WARNING + "[FAIL] changelog variable does't exists" + bcolors.END)
	try:
		funcname.run
		print(bcolors.OKGREEN+"[OK] run function exists"+bcolors.END)
	except(AttributeError):
		print(bcolors.WARNING + "[FAIL] run function does't exists" + bcolors.END)
	try:
		funcname.message
		print(bcolors.OKGREEN+"[OK] message variable exists"+bcolors.END)
	except(AttributeError):
		print(bcolors.YEL + "[?] message variable does't exists" + bcolors.END)
	try:
		funcname.help_notes
		print(bcolors.OKGREEN+"[OK] help_notes variable exists"+bcolors.END)
	except(AttributeError):
		print(bcolors.YEL + "[?] help_notes variable does't exists" + bcolors.END)
	try:
		funcname.mhelp
		print(bcolors.OKGREEN+"[OK] mhelp list exists"+bcolors.END)
	except(AttributeError):
		print(bcolors.YEL + "[?] mhelp list does't exists" + bcolors.END)
	try:
		funcname.customcommands
		print(bcolors.OKGREEN+"[OK] customcommands list exists"+bcolors.END)
	except(AttributeError):
		print(bcolors.YEL + "[?] customcommands list does't exists" + bcolors.END)
	try:
		funcname.terminal
		print(bcolors.OKGREEN+"[OK] terminal variable exists"+bcolors.END)
	except(AttributeError):
		print(bcolors.YEL + "[?] terminal variable does't exists" + bcolors.END)
	try:
		funcname.needroot
		print(bcolors.OKGREEN+"[OK] needroot variable exists"+bcolors.END)
	except(AttributeError):
		print(bcolors.YEL + "[?] needroot variable does't exists" + bcolors.END)
	try:
		funcname.outdated
		print(bcolors.OKGREEN+"[OK] outdated variable exists"+bcolors.END)
	except(AttributeError):
		print(bcolors.YEL + "[?] outdated variable does't exists" + bcolors.END)