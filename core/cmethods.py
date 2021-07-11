#         Copyright (C) 2015 Noa-Emil Nissinen (4shadoww)

# Import python modules

import sys
import os
import imp
import traceback
import curses
import time
import importlib
import glob

# Import getpath for lib path
from core import getpath

# Append lib path
sys.path.append(getpath.lib())

# Import core modules

from core import helptable
from core import helpin
from core import info
from core import colors
from core import moduleop
from prettytable import PrettyTable
import core.cowsay
from core import dsag
import core.matrix
import core.touchingsky
from core.hftest import check_module
from core import mscop
from core import value_holder
from core import moddbparser
from core.messages import *
from core.apistatus import *

# Import exceptions
from core.exceptions import UnknownCommand
from core.exceptions import ModuleNotFound
from core.exceptions import VariableError

class Cmethods:

    # Module manager object

    mm = None
    modadd = None

    # Init

    def __init__(self, mmi):
        self.mm = mmi

    # Module custom commands

    def mcu(self, command):
        try:
            if command[0] in self.modadd.customcommands.keys():
                call = getattr(self.modadd, command[0])
                try:
                    return call(command[1:])
                except Exception as e:
                    print(colors.red+"unexpected error in module:\n")
                    traceback.print_exc(file=sys.stdout)
                    print(colors.end)
                    if api.enabled == True:
                        raise
            else:
                raise UnknownCommand("unknown command")
        except AttributeError:
            raise UnknownCommand("unknown command")

    # Built in commands

    def exit(self, args):
        if self.mm.module_loaded == 1:
            self.mm.module_loaded = 0
            self.mm.module_name = ""
        else:
            sys.exit()

    def clear(self, args):
        if len(args) != 0 and args[0] == "tmp":
            mscop.clear_tmp()
        else:
            sys.stderr.write("\x1b[2J\x1b[H")

    def cl(self, args):
        os.system(' '.join(args))

    def help(self, args):

        if self.mm.module_loaded == 0:
            print(helptable.generate_table(helpin.commands))
        else:
            try: 
                print(helptable.generate_mtable(helpin.mcommands, self.modadd.customcommands))
            except AttributeError:
                print(helptable.generate_table(helpin.mcommands))
            try:
                print('\n',self.modadd.help_notes,'\n')
            except AttributeError:
                pass

    def version(self, args):
        if self.mm.module_loaded == 1:
            try:
                print(self.modadd.conf["name"]+" "+self.modadd.conf["version"])
            except:
                print(colors.red+"unexpected error in module:\n")
                traceback.print_exc(file=sys.stdout)
                print(colors.end)
                if api.enabled == True:
                    raise
        else:
            print("Hakku Framework " + info.version + " " + info.codename)

    def ifconfig(self, args):
        os.system("ifconfig"+" "+' '.join(args))

    def scan(self, args):
        network_scanner = importlib.import_module("core.network_scanner")
        network_scanner.scan()
        del network_scanner

    def about(self, args):
        if self.mm.module_loaded == 1:
            try:
                t = PrettyTable([self.modadd.conf["name"]+" "+self.modadd.conf["version"], ""])
                t.add_row(["",""])
                t.align = 'l'
                t.valing = 'm'
                t.border = False
                t.add_row(["author:", self.modadd.conf["author"]])
                t.add_row(["github:", self.modadd.conf["github"]])
                t.add_row(["email:", self.modadd.conf["email"]])
                t.add_row(["description:", self.modadd.conf["shortdesc"]])
                t.add_row(["initial date:", self.modadd.conf["initdate"]])
                t.add_row(["last modification:", self.modadd.conf["lastmod"]])
            
                if self.modadd.conf["apisupport"] == True:
                    support = "supported"
                else:
                    support = "not supported"
                t.add_row(["api support:", support])
                try:
                    self.modadd.conf["dependencies"]
                    deps = ""
                    i = 0
                    for dep in self.modadd.conf["dependencies"]:
                        i += 1
                        if i == len(self.modadd.conf["dependencies"]):
                            deps += dep
                        else:
                            deps += dep+", "
                    t.add_row(["dependencies:", deps])
                except KeyError:
                    pass
                print(t)
            except:
                print(colors.red+"unexpected error in module:\n")
                traceback.print_exc(file=sys.stdout)
                print(colors.end)
                if api.enabled == True:
                    raise
        else:
            print(info.about)

    def changelog(self, args):
        if self.mm.module_loaded == 1:
            try:
                print(self.modadd.changelog)
            except:
                print(colors.red+"unexpected error in module:\n")
                traceback.print_exc(file=sys.stdout)
                print(colors.end)
                if api.enabled == True:
                    raise
        else:
            try:
                f = open('changelog', 'r')
                file_contents = f.read()
                print (file_contents)
                f.close()
            except IOError:
                print_error("changelog file not found (have you removed it?)")

    def use(self, args):
        init = False
        if "modules."+args[0] not in sys.modules:
            init = True

        if self.mm.module_loaded == 0:
            try:
                self.modadd = importlib.import_module("modules."+args[0])
                self.mm.module_loaded = 1
                self.mm.set_name(self.modadd.conf["name"])
                try:
                    print(self.modadd.conf["message"])
                except KeyError:
                    pass
                try:
                    if self.modadd.conf["outdated"] == 1:
                        print_warning("this module is outdated and might not be working")
                except KeyError:
                    pass
                try:
                    if self.modadd.conf["needroot"] == 1:
                        if not os.geteuid() == 0:
                            print_warning("this module requires root permissions for full functionality!")
                except KeyError:
                    pass
                if init == True:
                    try:
                        self.modadd.init()
                    except AttributeError:
                        pass
            except ImportError:
                print(colors.red + "module not found" + colors.end)
                raise ModuleNotFound("module not found")
            except IndexError:
                print(colors.red + "please enter module name" + colors.end)
                raise ModuleNotFound("module not found")
            except:
                print(colors.red+"unexpected error in module:\n")
                traceback.print_exc(file=sys.stdout)
                print(colors.end)
                if api.enabled == True:
                    raise
        else:
            raise UnknownCommand("module in use")

    def show(self, args):
        try:
            if args[0] == "modules":
                t = PrettyTable([colors.bold+'Modules:', ''+colors.end])
                t.align = 'l'
                t.valing = 'm'
                t.border = False
                xml = moddbparser.parsemoddb()
                root = xml[0]
                for category in root:
                    if category.tag == "category":
                        t.add_row(["", ""])
                        t.add_row([colors.red+colors.uline+category.attrib["name"]+colors.end, colors.red+colors.uline+"Description"+colors.end])

                    for item in category:
                        if item.tag == "module":
                            for child in item:
                                if child.tag == "shortdesc":
                                    t.add_row([item.attrib["name"], child.text])
                                    break

                print(t)                

            elif args[0] == "options" and self.mm.module_loaded == 1:
                try:
                    moduleop.printoptions(self.modadd)
                except:
                    print(colors.red+"unexpected error in module:\n")
                    traceback.print_exc(file=sys.stdout)
                    print(colors.end)
                    if api.enabled == True:
                        raise
            else:
                raise UnknownCommand("module not loaded or unknown command")
        except IndexError:
            raise UnknownCommand("unknown command")

    def back(self, args):
        if self.mm.module_loaded == 1:
            self.mm.module_loaded = 0
            self.mm.module_name = ""
        else:
            raise UnknownCommand("unknown command")

    def reload(self, args):
        try:
            if self.mm.module_loaded == 0:
                try:
                    mod = "modules."+args[0]
                    if mod in sys.modules:
                        value_holder.save_values(sys.modules[mod].variables)
                        importlib.reload(sys.modules[mod])
                        value_holder.set_values(sys.modules[mod].variables)
                        try:
                            self.modadd.init()
                        except AttributeError:
                            pass
                        print (colors.bold+"module "+ args[0] +" reloaded"+colors.end)
                    else:
                        importlib.import_module(mod)
                        try:
                            self.modadd.init()
                        except AttributeError:
                            pass
                        print(colors.bold+"module "+ args[0] +" imported"+colors.end)

                except IndexError:
                    print (colors.red+"please enter module's name"+colors.end)
            else:
                try:
                    mod = "modules."+args[0]
                    if mod in sys.modules:
                        value_holder.save_values(sys.modules[mod].variables)
                        importlib.reload(sys.modules[mod])
                        value_holder.set_values(sys.modules[mod].variables)
                        try:
                            self.modadd.init()
                        except AttributeError:
                            pass                
                        print (colors.bold+"module "+ args[0] +" reloaded"+colors.end)
                    else:
                        importlib.import_module(mod)
                        try:
                            self.modadd.init()
                        except AttributeError:
                            pass
                        print(colors.bold+"module "+ self.mm.module_name +" reloaded"+colors.end)
                except IndexError:
                    mod = "modules."+self.mm.module_name
                    if mod in sys.modules:
                        value_holder.save_values(sys.modules[mod].variables)
                        importlib.reload(sys.modules[mod])
                        value_holder.set_values(sys.modules[mod].variables)
                        try:
                            self.modadd.init()
                        except AttributeError:
                            pass
                        print (colors.bold+"module "+ self.mm.module_name +" reloaded"+colors.end)

                    else:
                        modadd = importlib.import_module(mod)
                        try:
                            self.modadd.init()
                        except AttributeError:
                            pass
                        print(colors.bold+"module "+ self.mm.module_name +" reloaded"+colors.end)
        except:
            print(colors.red+"faced unexpected error during reimporting:\n")
            traceback.print_exc()
            print(colors.end)
            if api.enabled == True:
                raise

    def run(self, args):

        if self.mm.module_loaded == 1:
            try:
                return self.modadd.run()

            except KeyboardInterrupt:
                print(colors.red+"module terminated"+colors.end)
            except PermissionError:
                print_error("permission denied")
                return "[err] permission denied"
            except:
                print(colors.red+"unexpected error in module:\n")
                traceback.print_exc(file=sys.stdout)
                print(colors.end)
                if api.enabled == True:
                    raise
        else:
            raise UnknownCommand("module not loaded")

    def set(self, args):
        try:
            self.modadd.variables[args[0]][0] = args[1]
            print(colors.bold+args[0] +" => "+ str(args[1]) + colors.end)

        except (NameError, KeyError):
            print(colors.red + "option not found" + colors.end)
            raise VariableError("option not found")
        except IndexError:
            print(colors.red + "please enter variable's value" + colors.end)
            raise VariableError("no value")
        except:
            print(colors.red+"unexpected error in module:\n")
            traceback.print_exc(file=sys.stdout)
            print(colors.end)
            if api.enabled == True:
                raise

    def new(self, args):
        try:
            if args[0] == "module":
                try:
                    completeName = os.path.join(getpath.modules(), args[1]+".py")
                    if os.path.exists(completeName):
                        print(colors.red+"module already exists"+colors.end)

                    else:
                        mfile = open(completeName, 'w')
                        template = os.path.join('core', 'module_template')
                        f = open(template, 'r')
                        template_contents = f.readlines()
                        template_contents[5] = "    \"name\": \""+args[1]+"\", # Module's name (should be same as file name)\n"
                        template_contents[11] = "    \"initdate\": \""+(time.strftime("%d.%m.%Y"))+"\", # Initial date\n"
                        template_contents[12] = "    \"lastmod\": \""+(time.strftime("%d.%m.%Y"))+"\", # Last modification\n"
                        mfile.writelines(template_contents)
                        mfile.close()
                        print(colors.bold+"module "+ args[1] +".py" +" created to modules folder"+colors.end)
                        print(colors.bold+"done"+colors.end)

                except IndexError:
                    print(colors.red + "please enter module's name" + colors.end)

                except PermissionError:
                    print(colors.red + "error: permission denied" + colors.end)

                except IOError:
                    print(colors.red + "something went wrong" + colors.end)

            else:
                raise UnknownCommand("unknown command")
        except IndexError:
            raise UnknownCommand("unkown command")

    def check(self, args):
        try:
            if args[0] == "module":
                try:
                    self.modadd = importlib.import_module("modules."+args[1])
                    print(colors.green+"module found"+colors.end)
                    check_module(self.modadd)
                    print(colors.green+"\ntest passed"+colors.end)

                except IndexError:
                    print(colors.red + "please enter module name"+ colors.end)

                except ImportError:
                    print(colors.red+"error: module not found"+colors.end)

                except:
                    print(colors.red + "error:\n")
                    traceback.print_exc(file=sys.stdout)
                    print(colors.end)
            else:
                raise UnknownCommand("unknown command")
        except IndexError:
            raise UnknownCommand("unkown command")

    def matrix(self, args):
        try:
            core.matrix.main()
        except KeyboardInterrupt:
            curses.endwin()
            curses.curs_set(1)
            curses.reset_shell_mode()
            curses.echo()

    def cowsay(self, args):
        try:
            message = ' '.join(args)
            print(core.cowsay.cowsay(message))
            return
        except ValueError:
            print(core.cowsay.cowsay("Hakku Framework"))

    def ds(self, args):
        print(dsag.darkside)

    def make(self, args):
        try:
            if args[0] == "exit":
                sys.exit(0)
            else:
                raise UnknownCommand("unkown command")
        except IndexError:
            raise UnknownCommand("unkown command")

    def touchingsky(self, args):
        core.touchingsky.main()

    def loaded(self, args):
        print(sys.modules.keys())

    def list(self, args):
        if len(args) != 0 and args[0] == "dependencies":
            if self.mm.module_loaded == 0:
                modules = glob.glob(getpath.modules()+"*.py")
                dependencies = []
                for module in modules:
                    try:
                        modadd = importlib.import_module("modules."+os.path.basename(module).replace(".py", ""))
                        for dep in modadd.conf["dependencies"]:
                            if dep not in dependencies:
                                dependencies.append(dep)
                    except ImportError:
                        print(colors.red+"import error: "+os.path.basename(module).replace(".py", "")+colors.end)
                        break
                    except KeyError:
                        pass
                for dep in dependencies:
                    print(dep)
            else:
                try:
                    for dep in self.modadd.conf["dependencies"]:
                        print(dep)
                except KeyError:
                    print_info("this module doesn't require any dependencies")
        else:
            raise UnknownCommand("unknown command")

    def init(self, args):
        if self.mm.module_loaded == 1:
            try:
                self.modadd.init()
                print("module initialized")
            except AttributeError:
                print("this module doesn't have init function")
        else:
            raise UnknownCommand("unknown command")

    def redb(self, args):
        if self.mm.module_loaded == 1:
            try:
                moduleop.addtodb(self.modadd)
            except PermissionError:
                print(colors.red+"error: permission denied"+colors.end)
            except KeyboardInterrupt:
                print()
            except:
                print(colors.red+"faced unexpected:\n")
                traceback.print_exc(file=sys.stdout)
                print(colors.end)
                if api.enabled == True:
                    raise

        else:
            answer = input("do you want to update whole database? ")
            if answer == "yes" or answer == "y":
                try:
                    modules = glob.glob(getpath.modules()+"*.py")
                    for module in modules:
                        module = module.replace(getpath.modules(), '').replace('.py', '')
                        if module != '__init__' and module != "test":
                            modadd = importlib.import_module("modules."+module)
                            moduleop.addtodb(modadd)
                except PermissionError:
                    print(colors.red+"error: permission denied"+colors.end)
                except KeyboardInterrupt:
                    print()
                except:
                    print(colors.red+"faced unexpected:\n")
                    traceback.print_exc(file=sys.stdout)
                    print(colors.end)
                    if api.enabled == True:
                        raise
