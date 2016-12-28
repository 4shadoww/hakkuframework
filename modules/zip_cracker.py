#		Copyright (C) 2015 Noa-Emil Nissinen (4shadoww)

from core.messages import *
from core import colors
from collections import OrderedDict
import zipfile
import threading, queue
from core import getpath
from os.path import relpath
import sys

conf = {
	"name": "zip_cracker", # Module's name (should be same as file name)
	"version": "1.0", # Module version
	"shortdesc": "zip file brute-force attack using dictionary", # Short description
	"github": "4shadoww", # Author's github
	"author": "4shadoww", # Author
	"email": "4shadoww", # Email
	"initdate": "22.12.2016", # Initial date
	"lastmod": "27.12.2016",
	"apisupport": True, # Api support
}

# List of the variables
variables = OrderedDict((
	("file", ["none", "target zip file"]),
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
			zipf = zipfile.ZipFile(variables["file"][0])
		
		except FileNotFoundError:
			self.pwdh.error = "[err] zip file not found"
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
				zipf.extractall(variables["exto"][0], pwd=word.encode("utf-8"))
				self.pwdh.pwd = word
				return
			except RuntimeError:
				pass
			except zipfile.BadZipFile:
				pass

def run():
	try:
		wordlist = open(variables["dict"][0], "rb")
		printInfo("reading word list...")
		words = wordlist.read().splitlines()
	except FileNotFoundError:
		printError("word list not found")
		return "[err] word list not found"
	printInfo("brute-force attack started...")

	pwdh = PwdHolder
	pwdh.reset()

	try:
		u = int(variables["tc"][0])
	except TypeError:
		printError("invalid thread count")
		return "[err] invalid thread count"
	threads = []

	for i in range(variables["tc"][0]):
		t = Worker(words[i::u], pwdh)
		threads.append(t)
		t.start()
	printInfo("now cracking...")
	try:
		for thread in threads:
			thread.join()
	except KeyboardInterrupt:
		pwdh.kill = True
		printInfo("brute-force attack terminated")

	if pwdh.pwd != None:
		printSuccess("password found: "+pwdh.pwd)
		return pwdh.pwd

	elif pwdh.error != None:
		printError(pwdh.error)
		return pwdh.error