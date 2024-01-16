from parser0 import parse
from genpy import GenPy
from genjs import GenJs
from gencpp import GenCpp
from genir import GenIR
# from genobj import GenObj

langGen = {'py':GenPy(typed=True), 'js':GenJs(), 'cpp':GenCpp(), 'irasm':GenIR('irasm'), 'irobj':GenIR('irobj'), 'ir.ll':GenIR('ir.ll') }

def convert(code, lang):
	print(f'convert:lang={lang}')
	ast = parse(code)
	# print(ast)
	g = langGen[lang]
	g.gen(ast)
	return g.toCode()
