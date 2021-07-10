from prettytable import PrettyTable
from core import colors

def generateTable(hlist):
    t = PrettyTable([colors.bold+"Command"+colors.end, "",colors.bold+"Description"+colors.end])
    t.add_row(["-------"," ","-----------"])
    t.align = 'l'
    t.valing = 'm'
    t.border = False

    for val in hlist:
            t.add_row([val[0], "  =>  ", val[1]])

    return t

def generatemTable(hlist1, hlist2):
    t = PrettyTable([colors.bold+"Command"+colors.end, "",colors.bold+"Description"+colors.end])
    t.add_row(["-------"," ","-----------"])
    t.align = 'l'
    t.valing = 'm'
    t.border = False

    for val in hlist1:
            t.add_row([val[0], "  =>  ", val[1]])

    for key, val in hlist2.items():
            t.add_row([key, "  =>  ", val])

    return t