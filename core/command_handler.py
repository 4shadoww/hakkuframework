#         Copyright (C) 2015 Noa-Emil Nissinen (4shadoww)

from core.exceptions import UnknownCommand
from core.exceptions import ModuleNotFound
from core.exceptions import VariableError
from core import cmethods
from core.module_manager import ModuleManager
from core import colors

class Commandhandler:
    mm = None
    notcommand = ["mcu"]
    cm = None
    api = False

    def __init__(self, gmm, enableapi):
        self.mm = gmm
        self.cm = cmethods.Cmethods(self.mm)
        if enableapi == True:
            self.api = True

    def handle(self, command):
        # String to list
        command = command.split()

        # Custom command
        if self.mm.moduleLoaded == 1:
                try:
                    return self.cm.mcu(command)
                except IndexError:
                    return
                except UnknownCommand:
                    pass

        # Validate command

        if len(command) != 0 and command[0] in self.notcommand:
            print(colors.red+"unknown command"+colors.end)
            return
        try:
            method = getattr(self.cm, command[0])
        except AttributeError:
            print(colors.red+"unknown command"+colors.end)
            return
        except IndexError:
            return

        try:
            return method(command[1:])
        except UnknownCommand:
            print(colors.red+"unknown command"+colors.end)

        except ModuleNotFound:
            if self.api == True:
                raise ModuleNotFound("Module not found")

        except VariableError:
            if self.api == True:
                raise VariableError("variable error")