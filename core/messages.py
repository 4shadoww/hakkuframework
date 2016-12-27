import sys
from core import colors

error = "["+colors.bold+colors.red+"err"+colors.end+"] "
info = "["+colors.bold+colors.blue+"inf"+colors.end+"] "
warning = "["+colors.bold+colors.yellow+"war"+colors.end+"] "
success = "["+colors.bold+colors.green+"suf"+colors.end+"] "

def printError(message, end="\n"):
	sys.stdout.write(error+message+end)

def printWarning(message, end="\n"):
	sys.stdout.write(warning+message+end)

def printInfo(message, end="\n"):
	sys.stdout.write(info+message+end)

def printSuccess(message, end="\n"):
	sys.stdout.write(success+message+end)
