import os
import sys
from converter import convert
import lib0
from lexer0 import *
from parser0 import *

def excepthook(type, value, traceback):
    print(value)
    traceback()

sys.excepthook = excepthook

def run(code, lang):
	match lang:
		case 'js':
			toCode = convert(code, lang)
			cmd = f'deno run -A {toFile}'
		case 'py':
			toCode = convert(code, lang)
			toCode = 'import sys\nsys.path.append("sys0")\n'+toCode
			cmd = f'python {toFile}'
		case 'cpp':
			toCode = convert(code, lang)
			cmd = f'g++ -c {toFile} -I ./sys0/'
		case 'irasm':
			toCode = convert(code, lang)
			cmd = f'echo ir {toFile}'
		case 'irobj':
			toCode = convert(code, lang)
			cmd = f'echo ir {toFile}'
	print(f'-------------- {toFile} -----------')
	print(toCode)
	# if lang != 'obj':
	lib0.writeTextFile(toFile, toCode)
	if op == 'run':
		print('---------- run ---------------')
		os.system(cmd)


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
		run(code, lang)

