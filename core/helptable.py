from core.prettytable import PrettyTable
from core import colors

def generateTable(hlist):
	t = PrettyTable([colors.bold+"Command"+colors.end, "",colors.bold+"Description"+colors.end])
	t.add_row(["-------"," ","-----------"])
	t.align = 'l'
	t.valing = 'm'
	t.border = False

	for key, val in hlist.items():
			t.add_row([key, "  =>  ", val])

	return t

def generatemTable(hlist1, hlist2):
	t = PrettyTable([colors.bold+"Command"+colors.end, "",colors.bold+"Description"+colors.end])
	t.add_row(["-------"," ","-----------"])
	t.align = 'l'
	t.valing = 'm'
	t.border = False

	for key, val in hlist1.items():
			t.add_row([key, "  =>  ", val])

	for key, val in hlist2.items():
			t.add_row([key, "  =>  ", val])

	return t