from parser0 import parse
from genpy import GenPy
from genjs import GenJs
from gencpp import GenCpp
from genir import GenIR
# from genobj import GenObj

langGen = {'py':GenPy, 'js':GenJs, 'cpp':GenCpp, 'ir':GenIR }

def convert(code, lang, typed=False):
	ast = parse(code)
	# print(ast)
	g = langGen[lang](typed)
	g.gen(ast)
	return g.toCode()
