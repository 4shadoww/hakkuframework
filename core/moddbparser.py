from core import getpath
import xml.etree.ElementTree as ET


def parsemoddb():
	tree = ET.parse(getpath.core()+"module_database.xml")
	root = tree.getroot()
	return root, tree