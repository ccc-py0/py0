import os
import sys
from converter import convert
import lib0
from lexer0 import *
from parser0 import *
from interpreter import interpret

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
			cmd = f'echo irasm {toFile}'
		case 'irobj':
			toCode = convert(code, lang)
			cmd = f'echo irobj {toFile}'
		case 'ir.ll':
			toCode = convert(code, lang)
			cmd = f'echo ir.ll {toFile}'
		case 'py0':
			toCode = code
		case _:
			error(f'run():lang = {lang} not support')
	print(f'-------------- {toFile} -----------')
	print(toCode)
	print('---------- run ---------------')
	if lang == 'py0':
		interpret(toCode)
	else:
		lib0.writeTextFile(toFile, toCode)
		if op == 'run':
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

