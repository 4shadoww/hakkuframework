#        Copyright (C) 2015 Noa-Emil Nissinen (4shadoww)
import os
import sys

def rchop(thestring, ending):
	if thestring.endswith(ending):
		return thestring[:-len(ending)]
	return thestring

def main():
	path = rchop(os.path.dirname(os.path.abspath(__file__)), "core")
	return path

def modules():
	path = rchop(os.path.dirname(os.path.abspath(__file__)), "core") + "modules/"
	return path

def core():
	path = os.path.dirname(os.path.abspath(__file__)) + "/"
	return path

def lib():
	path = os.path.dirname(os.path.abspath(__file__)) + "/lib/"
	return path

def tools():
	path = os.path.dirname(os.path.abspath(__file__)) + "/tools/"
	return path

def conf():
	path = os.path.dirname(os.path.abspath(__file__)) + "/conf/"
	return path

def tmp():
	path = os.path.dirname(os.path.abspath(__file__)) + "/tmp/"
	return path

def scripts():
	path = os.path.dirname(os.path.abspath(__file__)) + "/scripts/"
	return path