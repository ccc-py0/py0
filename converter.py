from parser0 import parse
from genpy import GenPy
from genjs import GenJs
langGen = {'py':GenPy,'js':GenJs}

def convert(code, lang):
    ast = parse(code)
    # print(ast)
    g = langGen[lang]()
    g.gen(ast)
    return g.emitCode()

def convertFile(pyFile, lang):
    with open(pyFile, 'r', encoding='utf-8') as file:
        code = file.read()
    toCode = convert(code, lang)
    toFile = pyFile.replace('.py0', f'.{lang}')
    match lang:
        case 'js':
            toCode = toCode
        case 'py':
            toCode = 'import sys\nsys.path.append("sys0")\n'+toCode
    with open(toFile, 'w', encoding='utf-8') as file:
        file.write(toCode)
    return toCode
