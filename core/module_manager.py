class ModuleManager():
    moduleLoaded = 0
    moduleName = None
    modadd = None

    def unload_module(self):
        ModuleManager.moduleLoaded = 0

    def load_module(self):
        ModuleManager.moduleLoaded = 1

    def set_name(self, name):
        ModuleManager.moduleName = name
