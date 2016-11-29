class ModuleManager():
	moduleLoaded = 0
	moduleName = ""
	modadd = ""

	def unloadModule():
		ModuleManager.moduleLoaded = 0

	def loadModule():
		ModuleManager.moduleLoaded = 1

	def setName(name):
		ModuleManager.moduleName = name