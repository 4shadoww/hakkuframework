from core import info
from core import colors
from core.moduleop import count

hakku = r"""
  _    _       _    _          
 | |  | |     | |  | |         
 | |__| | __ _| | _| | ___   _ 
 |  __  |/ _` | |/ / |/ / | | |
 | |  | | (_| |   <|   <| |_| |
 |_|  |_|\__,_|_|\_\_|\_\\__,_|
"""

def print_info():
	count()

	print("\t" + colors.bold + "Hakku Framework\n" + colors.end)
	print("\t" + colors.bold + "Core "+colors.end+"\t[ "+info.version+" "+info.codename+"\t]" + colors.end)
	print("\t" + colors.bold + "API"+colors.end+"\t[ "+info.apiversion+"\t\t]"+colors.end)
	print("\t" + colors.bold + "Date"+colors.end+"\t[ "+info.update_date+"\t\t]"+colors.end)
	print("\t" + colors.bold + "Modules "+colors.end+"[ "+count.mod+" modules"+"\t\t]"+colors.end)
	print("\n")
