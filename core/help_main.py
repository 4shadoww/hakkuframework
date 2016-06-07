#        Copyright (C) 2015 Noa-Emil Nissinen (4shadoww)
from core import bcolors
from collections import OrderedDict

commands = OrderedDict((
('use '+bcolors.END+'(module name)', 'load module'),
('show modules', 'show modules'),
('clear', 'clear terminal'),
('exit', 'exit from '+ '\xb5' +'Sploit'),
('version', 'show '+ '\xb5' +'Sploit version'),
('t '+bcolors.END+'(command)','run terminal command'),
('ifconfig', 'run terminal command ifconfig'),
('install requirements', 'install required softwares'),
('about', 'information about '+ '\xb5' +'Sploit'),
('changelog', 'show changelog'),
('new module '+bcolors.END+'(module name)', 'create new module'),
('check module '+bcolors.END+'(module name)', 'check module'),
('reload '+bcolors.END+'(module name)', 'reload module (useful for developers)'),

))