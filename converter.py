from parser0 import parse
from genpy import GenPy
from genjs import GenJs
from gencpp import GenCpp
from genasm import GenAsm
from genobj import GenObj

langGen = {'py':GenPy, 'js':GenJs, 'cpp':GenCpp, 'asm':GenAsm, 'obj':GenObj }

def convert(code, lang, typed=False):
	ast = parse(code)
	# print(ast)
	g = langGen[lang](typed)
	g.gen(ast)
	return g.emitCode()
