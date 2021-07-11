Python API
==========

Hakku Framework does have a simple python API, that can be used to run commands. The module must support API if you want some data back from the module when you execute it.

Here is an example:
```python
from hakku import api # Import api

hakku = api.Hakkuapi(False) # Create hakku object (agurment: enable stdout)
hakku.loadModule("zip_cracker") # Load modulke zip_cracker
hakku.setVariable("file", "hakku/core/tmp/test.zip") # Set target zip file
print(hakku.runModule()) # Print results
```

API reference
-------------

* **loadModule(module)** (load module)
* **unloadModule(module)** (unload module)
* **setVariable(variable, value)** (change option's value)
* **runModule() (run module)**
* **customCommand(customcommand)** (run module's custom command)
* **runCommand(command)** (run any command)

Exceptions
----------

* **ModuleNotFound** (module not found)
* **VariableError** (module's variable not found)
* **ApiNotSupported** (will be raised when you load module that doesn't support API)
* **ModuleError** (will be raised when module faces an error)
