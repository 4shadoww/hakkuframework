import sys

def animline(text, last=False):
	sys.stdout.write("\033[K")
	if last == False:
		sys.stdout.write(text+"\r")
	else:
		sys.stdout.write(text+"\n")