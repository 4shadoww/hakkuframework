import subprocess
import time
import os
from core import getpath
from core import bcolors
import sys
import time
import itertools

running = False
message = None

def init():
	if not os.geteuid() == 0:
		print(bcolors.WARNING+'[!] playing alert requires root permissions'+bcolors.END)
	else:
		subprocess.call('modprobe pcspkr', shell=True)

def alert(im):
	global running
	global message
	message = im
	running = True
	init()
	if os.geteuid() == 0:
		run_alert()


def run_alert():
	global message
	syms = [bcolors.WARNING+bcolors.BOLD+'[ALERT] '+message+' [ctrl + c]'+bcolors.END, '[ALERT] '+ message+' [ctrl + c]']
	global running
	for i in itertools.count():
		beep = getpath.tools()+'beep -f 500 -l 500'
		subprocess.call(beep, shell=True)
		for sym in syms:
			sys.stdout.write("\r%s" % sym)
			sys.stdout.flush()
			time.sleep(0.5)