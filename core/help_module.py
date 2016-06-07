from core import bcolors
from collections import OrderedDict

commands = OrderedDict((
('show options', 'show options'),
('set '+bcolors.END+'(option name) (value)', 'set value to option'),
('run', 'run module'),
('exit', 'exit from module'),
('back', 'exit from module'),
('clear', 'clear terminal'),
('ifconfig', 'run terminal command ifconfig'),
('t '+bcolors.END+'(command)', 'run terminal command'),
('changelog', 'show changelog'),
('reload', 'reload this module (useful for developers)'),
('debug '+bcolors.END+'(function)', 'debug custom command function (useful for developers)'),

))