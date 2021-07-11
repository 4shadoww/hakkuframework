import traceback
import sys
import os
import subprocess
import glob
import py_compile
import importlib
import json

from core import getpath
from core import colors

env = dict(os.environ)
if 'PYTHONPATH' in env:
    env['PYTHONPATH'] = getpath.lib() + ':' + getpath.main() + ':' + env['PYTHONPATH']
else:
    env['PYTHONPATH'] = getpath.lib() + ':' + getpath.main()

pylint_workarounds = ['scapy.all', 'whois', 'netfilterqueue']

def pylint_ignore(message):
    for item in pylint_workarounds:
        if item in message: return True

    return False


def pylint_check(path, ignored=None):
    if ignored:
        result = subprocess.run(['pylint', path, 'ignore=['+','.join(ignored)+']', '--output-format=json'], capture_output=True, env=env)
    else:
        result = subprocess.run(['pylint', path, '--output-format=json'], capture_output=True, env=env)
    if result.returncode == 1:
        print(colors.red+"pylint returned 1"+colors.end)
        print(result.stdout.decode('utf-8'))
        print(result.stderr.decode('utf-8'))
        return False

    js = json.loads(result.stdout.decode('utf-8'))
    noerror = True
    for mes in js:
        if mes['type'] == "error" and not pylint_ignore(mes['message']): # pylint cannot load scapy correctly
            print(colors.red+"pylint found error:")
            print(mes['type'], mes['message-id'], mes['path'], 'line:', str(mes['line']) + ':' + str(mes['column']), mes['message'] +colors.end)
            noerror = False

    return noerror

def check_modules():
    modules = glob.glob(getpath.modules()+"*.py")

    for module in modules:
        module = module.replace(getpath.modules(), '').replace('.py', '')
        if module != '__init__':
            modadd = importlib.import_module("modules."+module)
            check_module(modadd)

def check_module(modadd):
    print(colors.yellow+'checking',modadd.conf["name"]+colors.green)

    if not pylint_check(modadd.__file__):
        testfailed()

    module = modadd.__name__.replace("modules.", "")
    if modadd.conf["name"] != module:
        print(colors.red+"\nmodules name doesn't match")
    modadd.conf["version"]
    if modadd.conf["shortdesc"] == 'none':
        print(colors.red+'\ndesc variable has default value'+colors.green)
        testfailed()
    if modadd.conf["github"] == 'none':
         print(colors.red+'\ngithub variable has default value'+colors.green)
         testfailed()
    if modadd.conf["author"] == 'none':
        print(colors.red+'\ncreatedby variable has default value'+colors.green)
        testfailed()
    if modadd.conf["email"] == 'none':
        print(colors.red+'\nemail variable has default value'+colors.green)
        testfailed()

    if modadd.conf["initdate"] == "none":
        print(colors.red+'\ninitdate variable has default value'+colors.green)
        testfailed()

    if modadd.conf["lastmod"] == "none":
        print(colors.red+'\nlastmod variable has default value'+colors.green)
        testfailed()

    try:
        if modadd.conf["dependencies"][0] == None:
            print(colors.red+"\ndependencies has default value")
            testfailed()
    except KeyError:
        pass

    modadd.variables.items()

    modadd.conf["apisupport"]
    modadd.changelog
    modadd.run
    try:
        modadd.customcommands
        check_customcommands(modadd)
    except AttributeError:
        pass


def check_customcommands(modadd):

    f = open(modadd.__file__, "r")
    for line in f:
        for c in modadd.customcommands:
            if c in line and "def" in line and "#" not in line and "args" not in line:
                print(colors.red+"custom command function doesn't have args argument"+colors.end)
                testfailed()
    f.close()


def check_core():
    core = glob.glob(getpath.core()+"*.py")

    print(colors.green+'\ntesting core...\n'+colors.green)

    for item in core:
        print(colors.yellow+'checking',item+colors.green)

        if not pylint_check(item):
            testfailed()

        py_compile.compile(item)

def compile_lib():
    print(colors.green+'\ntesting libraries...\n'+colors.green)
    for file in glob.iglob(getpath.lib()+'/**/*.py', recursive=True):
        print(colors.yellow+'compiling',file+colors.green)
        py_compile.compile(file)
    
def check_cmethods():

    print(colors.green+"\ntesting cmethods...\n"+colors.end)

    fcm = open(getpath.core()+"cmethods.py", "r")

    linenum = 1

    for line in fcm:
        if "self" not in line and "def " in line or "args" not in line and "def " in line:
            if "__init__" not in line and "mcu" not in line and "#" not in line:
                print(colors.red+"error in line "+str(linenum)+":\n"+colors.end)
                print(colors.red+line+colors.end)
                testfailed()
        linenum += 1

def compile_api():
    print(colors.green+"compiling api...\n"+colors.end)
    py_compile.compile("api.py")

def challenge():
    try:
        print(colors.green+"\nstarting challenge"+colors.green)
        print(colors.green+"\ntesting modules\n"+colors.green)

        check_modules()
        check_core()
        compile_lib()
        check_cmethods()
        compile_api()

        print(colors.green+"test passed!"+colors.end)

        sys.exit(0)

    except SystemExit as e:
        sys.exit(e)

    except:
        print(colors.red+"\ntest not passed!\n")
        traceback.print_exc()
        print(colors.end)
        sys.exit(1)

def testfailed():
    print(colors.red+"\ntest not passed!\n"+colors.end)
    sys.exit(1)
