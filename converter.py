from parser0 import parse
from genpy import GenPy
from genjs import GenJs
from gencpp import GenCpp

langGen = {'py':GenPy,'js':GenJs,'cpp':GenCpp}

def convert(code, lang, typed=False):
	ast = parse(code)
	# print(ast)
	g = langGen[lang](typed)
	g.gen(ast)
	return g.emitCode()
