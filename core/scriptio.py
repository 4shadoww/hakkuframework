#         Copyright (C) 2015 Noa-Emil Nissinen (4shadoww)

# Import python modules
import readline
import sys

# Import core modules
from core.module_manager import ModuleManager
from core import colors
from core import command_handler

mm = ModuleManager

def run(scf):
    global mm

    scriptline = 0
    ch = command_handler.Commandhandler(mm, False)

    while True:
        try:
            if scriptline == len(scf):
                sys.exit(0)

            command = scf[scriptline][0]
            scriptline += 1

            ch.handle(command)
        except KeyboardInterrupt:
            print()
            sys.exit(0)