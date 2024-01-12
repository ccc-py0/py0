from parser0 import parse
from genpy import GenPy
from genjs import GenJs
from gencpp import GenCpp
from asm import GenAsm

langGen = {'py':GenPy, 'js':GenJs, 'cpp':GenCpp, 'asm':GenAsm }

def convert(code, lang, typed=False):
	ast = parse(code)
	# print(ast)
	g = langGen[lang](typed)
	g.gen(ast)
	return g.emitCode()
