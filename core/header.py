from core import info
from core import colors
from core.moduleop import count

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
	count()

	ston = colors.blue + "[" + colors.end
	print("\t\t--=" + ston + colors.green + '\xb5' +"Sploit Framework" + colors.end)
	print("\t+---**---==" + ston + "Version : " + colors.red + info.version + colors.end)
	print("\t+---**---==" + ston + "Codename : " + colors.red + info.codename + colors.end)
	print("\t+---**---==" + ston + "Available Modules : " + colors.green  + count.mod + colors.end)
	print("\t\t--=" + ston + "Update Date : [" + colors.red + info.update_date + colors.end + "]")
	print("\n")
