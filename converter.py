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
