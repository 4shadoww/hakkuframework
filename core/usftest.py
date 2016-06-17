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
        testfailed()

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
                if funcname.modulename != module:
                    print(bcolors.WARNING+"\nmodules name doesn't match")
                    testfailed()
                funcname.version
                if funcname.desc == 'modules_description':
                    print(bcolors.WARNING+'\ndesc variable has default value'+bcolors.END)
                    testfailed()
                if funcname.github == 'mygithub':
                     print(bcolors.WARNING+'\ngithub variable has default value'+bcolors.END)
                     testfailed()
                if funcname.createdby == 'creators_name':
                    print(bcolors.WARNING+'\ncreatedby variable has default value'+bcolors.END)
                    testfailed()
                if funcname.email == 'creators@email.com':
                    print(bcolors.WARNING+'\nemail variable has default value'+bcolors.END)
                    testfailed()
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

        print(bcolors.OKGREEN+'\n[*] testing '+'\xb5'+'Sploit'+bcolors.END)

        from __main__ import module
        from __main__ import terminal
        from __main__ import modulename
        from __main__ import funcname
        from __main__ import scoml
        from __main__ import scripting
        from __main__ import scriptline



        print(bcolors.OKGREEN+"\n[*] test passed"+bcolors.END)

        sys.exit(0)

    except SystemExit as e:
        sys.exit(e)

    except:
       testfailed()

def testfailed():
    print(bcolors.WARNING+"\n[!] test failed\n")
    traceback.print_exc()
    print(bcolors.END)
    sys.exit(1)