#        Copyright (C) 2015 Noa-Emil Nissinen (4shadoww)
from core import colors
from collections import OrderedDict

commands = OrderedDict((
("use (module name)", "load module"),
("show modules", "show modules"),
("clear", "clear terminal"),
("exit", "exit from Hakku Framework"),
("version", "show Hakku Framework version"),
("cl (command)","run terminal command"),
("ifconfig", "run terminal command ifconfig"),
("scan", "scan devices from lan"),
("about", "information about Hakku Framework"),
("changelog", "show changelog"),
("new module (module name)", "create new module"),
("check module (module name)", "check module"),
("reload (module name)", "reload module (useful for developers)"),
))

mcommands = OrderedDict((
("show options", "show options"),
("set (option name) (value)", "set value to option"),
("run", "run module"),
("exit", "exit from module"),
("back", "exit from module"),
("clear", "clear terminal"),
("ifconfig", "run terminal command ifconfig"),
("scan", "scan devices from lan"),
("about", "information about this module"),
("cl (command)", "run terminal command"),
("changelog", "show changelog"),
("reload", "reload this module (useful for developers)"),
))