class ModuleManager():
    module_loaded = 0
    module_name = None
    modadd = None

    def unload_module(self):
        self.module_loaded = 0

    def load_module(self):
        self.module_loaded = 1

    def set_name(self, name):
        self.module_name = name
