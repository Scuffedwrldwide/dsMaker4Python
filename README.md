# dsMaker4Python
Docstring Maker for Python. This python program will add template docstrings to all your functions. Currently only supports functions on the global scope.

Updates coming soon.
#
### How to use dsMaker4Python

1. Download and run dsMaker4Python.py.  
2. Copy your code. Make sure that every function is well idented.
3. Write a new file name for your docstringed version of the code. Do not give the same name the file that contains your code.
4. Paste your code with the keyboard shortcut `ctrl + shift + V` or `command + shift + V`.
5. To stop docstringing code, enter a single `q`.
   
Done, your docstringed code was created in dsMaker4Python's directory as filename.py.
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
#

### Upcoming Updates
1. Add support for functions inside functions.
2. Add support for Python classes.
3. Add support for multiple different docstring templates.
4. Improve code import method.
