from parser0 import parse
from genpy import GenPy
from genjs import GenJs
from genc import GenC

langGen = {'py':GenPy,'js':GenJs,'c':GenC}

def convert(code, lang, typed=False):
    ast = parse(code)
    # print(ast)
    g = langGen[lang](typed)
    g.gen(ast)
    return g.emitCode()

def convertFile(pyFile, lang, typed=False):
    match lang:
        case 'js':
            toCode = convert(code, lang, typed=False)
        case 'py':
            toCode = convert(code, lang, typed=True)
            toCode = 'import sys\nsys.path.append("sys0")\n'+toCode
        case 'c':
            toCode = convert(code, lang, typed=True)

    toFile = pyFile.replace('.py0', f'.{lang}')
    with open(toFile, 'w', encoding='utf-8') as file:
        file.write(toCode)
    return toCode
