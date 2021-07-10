import sys
from core import colors

errorstr = "["+colors.bold+colors.red+"err"+colors.end+"] "
infostr = "["+colors.bold+colors.blue+"inf"+colors.end+"] "
warningstr = "["+colors.bold+colors.yellow+"war"+colors.end+"] "
successstr = "["+colors.bold+colors.green+"suf"+colors.end+"] "

def printError(message, start="", end="\n"):
    sys.stdout.write(errorstr+message+end)

def printWarning(message, start="", end="\n"):
    sys.stdout.write(start+warningstr+message+end)

def printInfo(message, start="", end="\n"):
    sys.stdout.write(start+infostr+message+end)

def printSuccess(message, start="", end="\n"):
    sys.stdout.write(start+successstr+message+end)
