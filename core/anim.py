import sys
from core import colors

error = "["+colors.bold+colors.red+"err"+colors.end+"] "
info = "["+colors.bold+colors.blue+"inf"+colors.end+"] "
warning = "["+colors.bold+colors.yellow+"war"+colors.end+"] "
success = "["+colors.bold+colors.green+"suf"+colors.end+"] "

def animline(message, last=False):
	sys.stdout.write("\033[K")
	if last == False:
		sys.stdout.write(message+"\r")
	else:
		sys.stdout.write(message+"\n")

def animError(message, last=False):
	sys.stdout.write("\033[K")
	if last == False:
		sys.stdout.write(error+message+"\r")
	else:
		sys.stdout.write(error+message+"\n")

def animWarning(message, last=False):
	sys.stdout.write("\033[K")
	if last == False:
		sys.stdout.write(warning+message+"\r")
	else:
		sys.stdout.write(warning+message+"\n")

def animInfo(message, last=False):
	sys.stdout.write("\033[K")
	if last == False:
		sys.stdout.write(info+message+"\r")
	else:
		sys.stdout.write(info+message+"\n")

def animSuccess(message, last=False):
	sys.stdout.write("\033[K")
	if last == False:
		sys.stdout.write(success+text+"\r")
	else:
		sys.stdout.write(success+text+"\n")