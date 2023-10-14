def getCode():
    code = input("Paste your code (CTRL+SHIFT+V). Enter 'q' when you're done.\n") + "\n"
    while 1:
        line = input()
        if line == 'q':
            return code
        code += line + "\n"

def getArguments(line):
    args = []
    size = len(line)
    word = ""
    for i in range(size):
    # Ignore up until the first parentheses
        if line[i] == '(':
            j = i + 1
            while j < size and line[j] != ')':
                # Words are any characters besides spaces and commas
                if line[j] != "," and line[j] != " ":
                    word += line[j]
                else:
                # If it finds a space or a comma, finishes the word and adds to the list
                    if word != "":
                        args.append(word)
                    word = ""
                j += 1
            break
    # Add last argument
    if word != "":
        args.append(word)
    return args

def setDocstring(lines, i):
    args = getArguments(lines[i])
    docstring = f'    """\n    Add Description Here\n\n'
    for arg in args:
        docstring += f'    :param {arg}: Add Type\n'
    docstring += f'    :return: Add Type\n    """\n'
    lines[i] += f'\n{docstring}'

def getDefsPositions(lines):
    positions = []
    for i in range(len(lines)):
        if lines[i].startswith('def '):
            positions.append(i)
    return positions

def addDocstrings(code):
    lines = code.split('\n')
    positions = getDefsPositions(lines)
    for i in positions:
        setDocstring(lines, i)
    code = '\n'.join(lines)
    return code

def create_file(filename, code):
    with open(filename, 'w') as file:
        file.write(code)

def main():
    running = True
    while running:
        filename = input("Name your NEW file: ") + ".py"
        code = getCode()
        code = addDocstrings(code)
        create_file(filename, code)
        while running:
            choice = input("Do you wish to docstring more programs? Y|N\n").upper()
            if choice == "N":
                return
            if choice == "Y":
                break
    return

main()
