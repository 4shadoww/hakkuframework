Modules
=======

On this page will be documentation about creating Hakku framework modules.

Basic commands
--------------

Here are few commands that can be useful when developing a module.

***

**new module**

This command creates a new module from the template.

usage:

- **new module** *name*

***

**reload**

This command reloads the currently loaded or specified module.

usage:

- **reload**
- **reload** *name*

***

**check module**

Does basic checks to the module (variables and functions).

usage:

- **check module** *name*

***

**redb**

Add new modules to the database.

usage:

- **redb**

***

Writing to stdout
--------
Don't use **print()**, use functions below to print.

List of functions:

* **print_info()**
* **print_warning()**
* **print_error()**
* **print_success()**

These functions have optional arguments **start** and **end** for defining line beginning and ending.

***

Text colors
-----------
Please use the colour pallet from "core/colors".

```python
from core import colors
```

```python
print(colors.blue+"hello world"+colors.end)
```

List of colours:
```python
purple
blue
green
cyan
yellow
red
end
bold (bold text)
uline (underline)
```

***
Module custom commands
---------------

```python
customcommands = {
    "example": "example command"
}
```
This variable holds a description for the "example" command and lets the framework know this command exists.

Custom command function should always have one argument:
```python
def example(args):
```

***

Hello message
-------------
To print some messages when the module is loaded, use the message variable.

```python
message = "hello world"
```
***
Needroot warning
----------------

If the module needs root privileges, add this variable:
```python
needroot = 1
```

***
Modifying module variables at runtime
-----------------------------------
Use prebuild function to modify module variables at runtime (the OrderedDict *variables*).

```python
from core.setvar import *
setvar('variable', 'value', variables)
```
***
Paths
--------
```python
from core import getpath
```

getpath module finds absolute paths to various locations.

List of functions:

* **main()** (main executable's directory path)
* **main_module()** (main module path)
* **modules()** (modules/)
* **core()** (core/)
* **lib()** (lib/)
* **tools()** (core/tools/)
* **conf()** (core/conf/)
* **tmp()** (core/tmp/)
* **scripts()** (core/scripts/)
* **db()** (core/db/)

Example usage:
```python
from core import getpath

print(getpath.db())
```
***

init function
-------------
init function will be executed if it exists when the module is loaded.

Example:
```python
def init():
    print('hello world')
```
***
