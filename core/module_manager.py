class ModuleManager():
	moduleLoaded = 0
	moduleName = None
	modadd = None

	def unloadModule():
		ModuleManager.moduleLoaded = 0

	def loadModule():
		ModuleManager.moduleLoaded = 1

	def setName(name):
		ModuleManager.moduleName = name