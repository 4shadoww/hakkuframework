import curses
import random
import time
import traceback

def generateSky(y, x, req):
	sky = []

	xsky = []

	for iy in range(0, y):
		for ix in range(0, x):
			if random.uniform(0, 1) < req:
				xsky.append(["✱"])
			else:
				xsky.append([" "])

		sky.append(xsky)
		xsky = []

	return sky

def animateSky(sky):
	for i in sky:
		for x in i:
			if x[0] == "✱" and random.uniform(0, 1) < 0.0015:
				x[0] = "⋆"
			elif x[0] == "⋆":
				x[0] = "✱"

def renderSky(screen, sky):
	screen.clear()
	try:
		for i in sky:
			for x in i:
				screen.addstr(x[0])
			screen.addstr("\n")
	except curses.error:
		pass
	screen.refresh()

def main():
	try:
		screen = curses.initscr()
		size = screen.getmaxyx()
		sky = generateSky(size[0]-1, size[1]-1, 0.025)

		while True:
			if size[0] != screen.getmaxyx()[0] and size[1] != screen.getmaxyx()[1]:
				size = screen.getmaxyx()
				sky = generateSky(size[0]-1, size[1]-1, 0.05)

			animateSky(sky)
			renderSky(screen, sky)
			time.sleep(1)

		curses.endwin()

	except KeyboardInterrupt:
		curses.endwin()

	except:
		curses.endwin()
		traceback.print_exc()