# dsMaker4Python
Docstring Maker for Python. This python program will add template docstrings to all your functions.
Updates coming soon.
#
### How to use dsMaker4Python

1. Download and run dsMaker4Python.py on the same directory as the file you want to docstring.
2. Insert your filename (example.py -> Insert "example").
   
Done, your docstringed code was created in that same directory as doc_filename.py.
#
### Utilization Example
Before:
```Python
def sum(a,b):
  return a+b
```
After:
```Python
def sum(a,b):
  """
  Add Descrpition Here
  
  :param a: Add type
  :param b: Add type
  :return: Add Type
  """
  return a+b
```
### Added Changes
1. Support for every function, global scope or not.
2. Improved user input method.
3. Improved file searching and argument validation.

### Upcoming Updates
1. Add support for Python classes.
2. Add support for multiple different docstring templates.
