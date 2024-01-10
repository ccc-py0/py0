import os
import sys
from converter import convert
import lib0
from lexer0 import *
from parser0 import *

sys.path.append('sys')

op, file, lang = sys.argv[1:4]
code = lib0.readTextFile(file)
toFile = file.replace('.py0', f'.{lang}')

match op:
    case 'lex':
        tokens = lex(code)
        lexDump(tokens)
    case 'parse':
        ast = parse(code)
        astDump(ast)
    case 'convert' | 'run':
        match lang:
            case 'js':
                toCode = convert(code, lang, typed=False)
                cmd = f'deno run -A {toFile}'
            case 'py':
                toCode = convert(code, lang, typed=True)
                toCode = 'import sys\nsys.path.append("sys0")\n'+toCode
                cmd = f'python {toFile}'
            case 'c':
                toCode = convert(code, lang, typed=True)
        print(f'-------------- {toFile} -----------')
        print(toCode)
        lib0.writeTextFile(toFile, toCode)
        if op == 'run':
            print('---------- run ---------------')
            os.system(cmd)


