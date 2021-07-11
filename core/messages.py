import sys
from core import colors

errorstr = "["+colors.bold+colors.red+"err"+colors.end+"] "
infostr = "["+colors.bold+colors.blue+"inf"+colors.end+"] "
warningstr = "["+colors.bold+colors.yellow+"war"+colors.end+"] "
successstr = "["+colors.bold+colors.green+"suf"+colors.end+"] "

def print_error(message, start="", end="\n"):
    sys.stdout.write(errorstr+message+end)

def print_warning(message, start="", end="\n"):
    sys.stdout.write(start+warningstr+message+end)

def print_info(message, start="", end="\n"):
    sys.stdout.write(start+infostr+message+end)

def print_success(message, start="", end="\n"):
    sys.stdout.write(start+successstr+message+end)
