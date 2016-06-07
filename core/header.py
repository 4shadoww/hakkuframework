from core import info
from core import bcolors
from core.check_modules import check

sploit = r"""
         _____       _       _ _
        / ____|     | |     (_) |
  _   _| (___  _ __ | | ___  _| |_
 | | | |\___ \| '_ \| |/ _ \| | __|
 | |_| |____) | |_) | | (_) | | |_
 | .___|_____/| .__/|_|\___/|_|\__|
 | |          | |
 |_|          |_|
"""

def print_info():
	check()

	ston = bcolors.OKBLUE + "[" + bcolors.END
	print("\t\t--=" + ston + bcolors.OKGREEN + '\xb5' +"Sploit Framework" + bcolors.END)
	print("\t+---**---==" + ston + "Version : " + bcolors.WARNING + info.version + bcolors.END)
	print("\t+---**---==" + ston + "Codename : " + bcolors.WARNING + info.codename + bcolors.END)
	print("\t+---**---==" + ston + "Available Modules : " + bcolors.OKGREEN  + check.mod + bcolors.END)
	print("\t\t--=" + ston + "Update Date : [" + bcolors.WARNING + info.update_date + bcolors.END + "]")
	print("\n")
