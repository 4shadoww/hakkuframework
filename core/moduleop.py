#		Copyright (C) 2015 Noa-Emil Nissinen (4shadoww)
import os
from core import colors
import traceback
import sys
from prettytable import PrettyTable
from core import getpath
from core import moddbparser
from xml.etree import ElementTree
from xml.dom import minidom

def count():
	isfile = os.path.isfile
	join = os.path.join

	directory = getpath.modules()
	global module_count
	module_count = sum(1 for item in os.listdir(directory) if isfile(join(directory, item)))
	module_count = module_count - 1
	count.mod = str(module_count)

def printoptions(modadd):
	try:
		print(" ")
		t = PrettyTable([colors.red +'Option', 'Value', 'Description'+colors.end])
		t.add_row(["------","------","-----------"])
		t.align = 'l'
		t.valing = 'm'
		t.border = False

		for key, val in modadd.variables.items():
				t.add_row([key, val[0], val[1]])

		print (t,'\n')
		try:
			print(modadd.option_notes,'\n')
		except(AttributeError):
			pass

	except Exception as error:
		print(colors.red+"error: module is corrupted\n")
		traceback.print_exc(file=sys.stdout)
		print(colors.end)

def writedb(root):
	rough_string = ElementTree.tostring(root, 'utf-8').decode("utf-8").replace("\n", "").replace("\t", "").replace("  ", "").replace("    ", "").encode("utf-8")
	reparsed = minidom.parseString(rough_string)
	clean = reparsed.toprettyxml(indent="\t")
	f = open(getpath.core()+"module_database.xml", "w")
	f.write(clean)
	f.close()

def addtodb(modadd):
	xml = moddbparser.parsemoddb()
	root = xml[0]
	tree = xml[1]

	new = True
	newcat = True

	for category in root:
		if category.tag == "category":
			for item in category:
				if item.tag == "module" and item.attrib["name"] == modadd.conf["name"]:
					for info in item:
						if info.tag == "shortdesc":
							info.text = modadd.conf["shortdesc"]
							new = False
							tree.write(getpath.core()+"module_database.xml")
							print("database updated")
							return
	if new == True:
		print("\n"+modadd.conf["name"]+" doesn't exist in database")
		print("available categorie keys:"+colors.yellow)
		for category in root:
			if category.tag == "category":
				print(category.attrib["key"])
		print(colors.end, end="")
		catkey = input("\n\ngive new or exist key? ")

		for category in root:
			if category.tag == "category" and category.attrib["key"] == catkey:
				module = ElementTree.Element("module")
				shortdesc = ElementTree.Element("shortdesc")
				shortdesc.text = modadd.conf["shortdesc"]
				module.set("name", modadd.conf["name"])
				module.append(shortdesc)
				category.append(module)
				writedb(root)
				newcat = False
				print("module added to "+category.attrib["name"])
				break

		if newcat == True:
			print("category not found\ngoing to add new category")
			catname = input("give new category's name: ")
			newcat = ElementTree.Element("category")
			newcat.set("name", catname)
			newcat.set("key", catkey)
			module = ElementTree.Element("module")
			shortdesc = ElementTree.Element("shortdesc")
			shortdesc.text = modadd.conf["shortdesc"]
			module.set("name", modadd.conf["name"])
			module.append(shortdesc)
			newcat.append(module)
			root.append(newcat)
			writedb(root)
			print("new category created")
			print("module added to "+newcat.attrib["name"])