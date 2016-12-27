#        Copyright (C) 2015 Noa-Emil Nissinen (4shadoww)
from core import colors
from collections import OrderedDict
import rarfile
import threading, queue
from core import getpath
from os.path import relpath
import sys
from core.animline import animline

conf = {
	"name": "rar_cracker", # Module's name (should be same as file name)
	"version": "1.0", # Module version
	"shortdesc": "rar file brute-force attack using word list", # Short description
	"github": "4shadoww", # Author's github
	"author": "4shadoww", # Author
	"email": "4shadoww0@gmail.com", # Email
	"initdate": "25.12.2016", # Initial date
	"lastmod": "27.12.2016",
	"apisupport": True, # Api support
}

# List of the variables
variables = OrderedDict((
	("file", ["none", "target rar file"]),
	("dict", ["none", "dictionary of words"]),
	("tc", [8, "thread count (int)"]),
	("exto", ["none", "extract directory"])
))

# Simple changelog
changelog = "Version 1.0:\nrelease"

def init():
	variables["exto"][0] = relpath(getpath.tmp(), getpath.main_module())
	variables["dict"][0] = relpath(getpath.db() + "dazzlepod.txt", getpath.main_module())

class PwdHolder:
	pwd = None
	error = None
	kill = False

	def __init__(self):
		self.pwd = None
		self.error = None
		self.kill = False

	def reset():
		PwdHolder.pwd = None
		PwdHolder.error = None
		PwdHolder.kill = False

class Worker(threading.Thread):
	pwdh = None
	words = None
	def __init__(self, words, pwdh):
		self.pwdh = pwdh
		self.words = words
		threading.Thread.__init__(self)

	def run(self):
		try:

			rf = rarfile.RarFile(variables["file"][0])
		
		except FileNotFoundError:
			self.pwdh.error = "error: rar file not found"
			return
		for word in self.words:
			if self.pwdh.pwd != None:
				return
			elif self.pwdh.error != None:
				return
			elif self.pwdh.kill == True:
				return
			try:
				word = word.decode("utf-8").replace("\n", "")
				if word[0] == "#":
					continue
				#animline("trying password: "+word)
				rf.extractall(path=variables["exto"][0], pwd=word)
				self.pwdh.pwd = word
				return
			except rarfile.RarCRCError:
				pass
			except rarfile.RarUserBreak:
				self.pwdh.kill = True
			except rarfile.RarSignalExit:
				pass


def run():
	try:
		wordlist = open(variables["dict"][0], "rb")
		print("reading word list...")
		words = wordlist.read().splitlines()
	except FileNotFoundError:
		print(colors.red+"error: word list not found"+colors.end)
		return "error: word list not found"
	print("brute-force attack started...")

	pwdh = PwdHolder
	pwdh.reset()

	try:
		u = int(variables["tc"][0])
	except TypeError:
		print(colors.red+"error: invalid thread count"+colors.end)
		return "error: invalid thread count"
	threads = []

	for i in range(variables["tc"][0]):
		t = Worker(words[i::u], pwdh)
		threads.append(t)
		t.start()
		
	print(colors.bold+"now cracking..."+colors.end)
	try:
		for thread in threads:
			thread.join()
	except KeyboardInterrupt:
		pwdh.kill = True
		print(colors.bold+"brute-force attack terminated"+colors.end)

	if pwdh.pwd != None:
		print(colors.green+"password found: "+pwdh.pwd+colors.end)
		return pwdh.pwd

	elif pwdh.error != None:
		print(colors.red+pwdh.error+colors.end)
		return pwdh.error