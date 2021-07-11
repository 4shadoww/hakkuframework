#!/usr/bin/env python3

#  Copyright (C) 2015 – 2021 Noa-Emil Nissinen (4shadoww)

import shutil
import distutils
import getopt
import sys
import os

def print_help():
    print("usage:", sys.argv[0], "<option>")
    print("Options:\n -i\t\tinstall\n -u\t\tuninstall\n -h\t\tprint help")


def install():
    print("installing Hakku Framework")

    print("creating dictionary /usr/share/hakkuframework")

    if os.path.exists("/usr/share/hakkuframework/"):
        print("removing exist installion...")
        shutil.rmtree("/usr/share/hakkuframework/")

    try:

        os.mkdir("/usr/share/hakkuframework")

    except PermissionError:
        print("permission error: permission denied")
        return

    print("copying files...")
    shutil.copyfile("hakku", "/usr/share/hakkuframework/hakku")

    shutil.copyfile("license", "/usr/share/hakkuframework/license")
    shutil.copyfile("changelog", "/usr/share/hakkuframework/changelog")

    shutil.copytree("core", "/usr/share/hakkuframework/core/")
    shutil.copytree("modules", "/usr/share/hakkuframework/modules/")
    shutil.copytree("lib", "/usr/share/hakkuframework/lib/")

    print("creating symlink...")
    os.system("ln -s /usr/share/hakkuframework/hakku /usr/bin/hakku")

    print("giving executeable permissions...")
    os.system("chmod +x /usr/share/hakkuframework/hakku")

def uninstall():
    print("uninstalling Hakku Framework")

    print("removing Hakku Framework...")
    try:
        shutil.rmtree("/usr/share/hakkuframework/")
    except FileNotFoundError:
        pass

    except PermissionError:
        print("permission error: permission denied")
        return

    print("removing symlink...")
    try:
        os.system("unlink /usr/bin/hakku")
    except FileNotFoundError:
        pass

    print("Hakku Framework uninstalled successfully")

if __name__ == "__main__":
    if not os.geteuid() == 0:
        print("warning: no root access")

    if len(sys.argv[1:]) > 1:
        print("invalid argument")
        print_help()

    elif len(sys.argv[1:]) == 1:
        if sys.argv[1] == '-i':
            install()
        elif sys.argv[1] == '-u':
            uninstall()
        elif sys.argv[1] == '-h':
            print_help()
        else:
            print("invalid argument")
            print_help()
