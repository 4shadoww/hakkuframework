import sys

def animline(text):
	print(text, end="\r")
	sys.stdout.write("\033[K")