#        Copyright (C) 2015 Noa-Emil Nissinen (4shadoww)
from core import colors
from collections import OrderedDict

commands = OrderedDict((
("use "+colors.end+"(module name)", "load module"),
("show modules", "show modules"),
("clear", "clear terminal"),
("exit", "exit from "+ "\xb5" +"Sploit"),
("version", "show "+ "\xb5" +"Sploit version"),
("cl "+colors.end+"(command)","run terminal command"),
("ifconfig", "run terminal command ifconfig"),
("scan", "scan devices from lan"),
("about", "information about "+ "\xb5" +"Sploit"),
("changelog", "show changelog"),
("new module "+colors.end+"(module name)", "create new module"),
("check module "+colors.end+"(module name)", "check module"),
("reload "+colors.end+"(module name)", "reload module (useful for developers)"),
))

mcommands = OrderedDict((
("show options", "show options"),
("set "+colors.end+"(option name) (value)", "set value to option"),
("run", "run module"),
("exit", "exit from module"),
("back", "exit from module"),
("clear", "clear terminal"),
("ifconfig", "run terminal command ifconfig"),
("scan", "scan devices from lan"),
("about", "information about this module"),
("cl "+colors.end+"(command)", "run terminal command"),
("changelog", "show changelog"),
("reload", "reload this module (useful for developers)"),
))