import os
TAB = "    " # Change docstring indentation here

def getCode(filename):
    with open(filename, 'r') as file:
        code = file.read()
    return code
    
    

def getArguments(line):
    args = []
    size = len(line)
    word = ''
    for i in range(size):
        if line[i] == '(':
            j = i + 1
            while j < size and line[j] != ')':
                if line[j] != ',' and line[j] != ' ':
                    word += line[j]
                else:
                    if word != '':
                        args.append(word)
                    word = ''
                j += 1
            break
    if word != '':
        args.append(word)
    return args
    
def countSpace(line):
    count = 0
    for i in range(len(line)):
        if line[i] == ' ':
            count += 1
        else:
            break
    return count

def setDocstring(line):
    args = getArguments(line)
    space = TAB + " " * countSpace(line)
    docstring = f'{space}"""\n{space}Add Description Here\n\n'
    for arg in args:
        docstring += f'{space}:param {arg}: Add Type\n'
    docstring += f'{space}:return: Add Type\n{space}"""\n'
    line += f'\n{docstring}'
    return line


def getDefsPositions(lines):
    positions = []
    for i in range(len(lines)):
        temp = lines[i].strip()
        if temp.startswith('def '):
            positions.append(i)
    return positions
    

def addDocstrings(code):
    lines = code.split('\n')
    positions = getDefsPositions(lines)
    for i in positions:
        lines[i] = setDocstring(lines[i])
    code = '\n'.join(lines)
    return code
    

def create_file(filename, code):
    filename += '.py'
    try:
        file = open(filename, 'r')
        print('This file already exists\n Docstrings not added.\n')
        return False
    except:
        with open(filename, 'w') as file:
            file.write(code)
            return True
    
def searchFile(filename):
    directory = '.'
    filepath = None
    for root, dirs, files in os.walk(directory):
        if filename in files:
            filepath = os.path.join(root, filename)
            break
    if filepath is not None:
        return filepath
    else:
        return None

def main():
    while 1:
        try:
            filename = input('Insert filename: ')
            code = getCode(searchFile(filename + ".py"))
            break
        except:
            print('File not found\n')
            return 1

    code = addDocstrings(code)
    filename = "doc_" + filename
    create_file(filename, code)
    return 0

main()
