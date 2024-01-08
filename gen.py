from lib0 import *
from parser0 import parse

def gen(n, g):
	t = n['type']
	match t:
		case 'stmts':
			g.STMTS(n)
		case 'stmt':
			g.STMT(n)
		case 'while':
			g.WHILE(n)
		case 'for':
			g.FOR(n)
		case 'if':
			g.IF(n)
		case 'return':
			g.RETURN(n)
		case 'assign':
			g.ASSIGN(n)
		case 'func':
			g.FUNC(n)
		case 'params':
			g.PARAMS(n)
		case 'param':
			g.PARAM(n)
		case 'block':
			g.BLOCK(n)
		case 'expr':
			g.EXPR(n)
		case 'mexpr':
			g.MEXPR(n)
		case 'cexpr':
			g.CEXPR(n)
		case 'bexpr':
			g.BEXPR(n)
		case 'lrexpr': 
			g.LREXPR(n)
		case 'array':
			g.ARRAY(n)
		case 'map':
			g.MAP(n)
		case 'obj':
			g.OBJ(n)
		case 'term':
			g.TERM(n)
		case 'args': 
			g.ARGS(n)
		case 'float':
			g.FLOAT(n)
		case 'integer':
			g.INTEGER(n)
		case 'string':
			g.STRING(n)
		case 'id':
			g.ID(n)

# 測試詞彙掃描器
if __name__ == "__main__":
	from test0 import code
	ast = parse(code)
	print(ast)
	gen(ast)
