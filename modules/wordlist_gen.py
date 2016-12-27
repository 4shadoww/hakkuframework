#        Copyright (C) 2015 Noa-Emil Nissinen (4shadoww)
from core import colors
from collections import OrderedDict
import threading, queue
import itertools
from os.path import relpath
from core import getpath
from core.animline import animline

conf = {
	"name": "wordlist_gen", # Module's name (should be same as file name)
	"version": "1.0", # Module version
	"shortdesc": "word list generator", # Short description
	"github": "4shadoww", # Author's github
	"author": "4shadoww", # Author
	"email": "4shadoww0@gmail.com", # Email
	"initdate": "26.12.2016", # Initial date
	"lastmod": "27.12.2016",
	"apisupport": True, # Api support
}

# List of the variables
variables = OrderedDict((
	("output", ["none", "output file"]),
	("chars", ["num_", "chars"]),
	("maxlen", [4, "max length of word (int)"]),
	("minlen", [3, "min length or word (int)"]),
))

# Additional notes to options
option_notes = " values  chars\n ------  ----- \n sc_  ->  a-z\n bc_  ->  A-Z\n num_ ->  0-9\n spc_ ->  !@#$%^&*?,()-=+[]/;"

# Simple changelog
changelog = "Version 1.0:\nrelease"

customcommands = {
	"addchar": "add more chars",
}

addchr = ""

def init():
	variables["output"][0] = relpath(getpath.db() + "wordlist", getpath.main_module())

class StatHolder:
	kill = False

	def __init__(self):
		self.kill = False

	def reset(self):
		self.kill = False

class Worker(threading.Thread):
	sh = None
	chars = None
	lenmax = None
	lenmin = None

	def __init__(self, sh, lenmax, lenmin, chars):
		self.sh = sh
		self.lenmax = lenmax
		self.lenmin = lenmin
		self.chars = chars
		threading.Thread.__init__(self)

	def run(self):
		try:
			f = open(variables["output"][0], "a")
		except Exception as error:
			print(colors.red+error+colors.end)
			return error

		for L in range(self.lenmin, self.lenmax):
			for word in itertools.combinations_with_replacement(self.chars, L):
				if self.sh.kill == True:
					f.close()
					return
				word = ''.join(word)
				#animline("generated word: "+word)
				f.write(word+"\n")

		f.close()

def run():
	global addchr
	smchars = "abcdefghijklmnopqrstuvwxyz"
	bgchars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	nums = "01223456789"
	scmarks = "!@#$%^&*?,()-=+[]/;"
	chars = ""

	chars += addchr
	if "sc_" in variables["chars"][0]:
		chars += smchars
	if "bc_" in variables["chars"][0]:
		chars += bgchars
	if "num_" in variables["chars"][0]:
		chars += nums
	if "spc_" in variables["chars"][0]:
		chars += scmarks

	try:
		variables["maxlen"][0] = int(variables["maxlen"][0])
	except ValueError:
		print(colors.red+"error: invalid maxlen"+colors.end)
		return "error: invalid maxlen"

	try:
		variables["minlen"][0] = int(variables["minlen"][0])
	except ValueError:
		print(colors.red+"error: invalid minlen"+colors.end)
		return "error: invalid minlen"

	sh = StatHolder()
	sh.reset()
	threads = []

	d = variables["maxlen"][0] - variables["minlen"][0]

	if d < 0:
		print(colors.red+"error: minlen can't be greater than minlen")
		return "error: minlen can't be greater than minlen"
	for i in range(variables["minlen"][0], variables["maxlen"][0]+1):
		t = Worker(sh, i+1, i, chars)
		threads.append(t)
		t.start()

	print(colors.bold+"generating..."+colors.end)
	try:
		for thread in threads:
			thread.join()
	except KeyboardInterrupt:
		sh.kill = True
		print(colors.bold+"word generator terminated"+colors.end)

	print(colors.green+"word list genereted\ndone"+colors.end)

def addchar(args):
	global addchr
	try:
		addchr += args[0]
		return "[suf] chars added"
	except IndexError:
		print("error: args not given")
		return "error: args not given"