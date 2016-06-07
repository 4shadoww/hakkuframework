#        Copyright (C) 2015 Noa-Emil Nissinen (4shadoww)
import os


def tools():
	path = os.path.dirname(os.path.abspath(__file__)) + "/tools/"
	return path

def conf():
	path = os.path.dirname(os.path.abspath(__file__)) + "/conf/"
	return path