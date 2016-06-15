from core import bcolors
import traceback, sys, os
from modules import *
import glob
import py_compile


def check_customcommands():
    global funcname
    try:
        funcname.mhelp
    except AttributeError:
        print(bcolors.WARNING+"\n[!] test failed\n")
        traceback.print_exc()
        print(bcolors.END)
        sys.exit(1)

def challenge():
    try:
        global funcname
        modules = glob.glob("modules/*.py")
        core = glob.glob("core/*.py")
        libs1 = glob.glob("core/libs/*.p")
        libs2 = glob.glob("core/libs/*/*.py")

        print(bcolors.OKGREEN+"\n[*] starting test"+bcolors.END)
        print(bcolors.OKGREEN+"\n[*] testing modules\n"+bcolors.END)
        #testing modules
        for module in modules:
            module = module.replace('modules/', '').replace('.py', '')
            if module != '__init__':
                funcname = globals()[module]
                print(bcolors.YEL+'checking',funcname.modulename+bcolors.END)
                funcname.version
                funcname.desc
                funcname.github
                funcname.createdby
                funcname.email
                funcname.variables
                funcname.vdesc
                funcname.changelog
                funcname.run
                try:
                    funcname.customcommands
                    check_customcommands()
                except AttributeError:
                    pass
        print(bcolors.OKGREEN+'\n[*] testing core\n'+bcolors.END)

        for item in core:
            print(bcolors.YEL+'compiling',item+bcolors.END)
            py_compile.compile(item)

        print(bcolors.OKGREEN+'\n[*] testing libs\n'+bcolors.END)

        for lib in libs1:
            print(bcolors.YEL+'compiling',lib+bcolors.END)
            py_compile.compile(lib)
        
        for lib in libs2:
            print(bcolors.YEL+'compiling',lib+bcolors.END)
            py_compile.compile(lib)



        print(bcolors.OKGREEN+"\n[*] test passed"+bcolors.END)

        sys.exit(0)

    except SystemExit as e:
        sys.exit(e)

    except:
        print(bcolors.WARNING+"\n[!] test failed\n")
        traceback.print_exc()
        print(bcolors.END)
        sys.exit(1)