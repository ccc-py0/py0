# from lib0 import *
from env import Env
from parser0 import *

def error(n, msg):
	print(f'Error: node {n}\n{msg}')
	raise Exception('interpereter:error')

env = None

def run(n):
	global env
	env = Env('global', None)
	t = n['type']
	match t:
		case 'stmts':
			STMTS(n)
		case 'stmt':
			STMT(n)
		case 'import':
			IMPORT(n)
		case 'while':
			WHILE(n)
		case 'for':
			FOR(n)
		case 'if':
			IF(n)
		case 'return':
			RETURN(n)
		case 'assign':
			ASSIGN(n)
		case 'func': # def id(PARAMS): BLOCK
			env = Env(n['id'], env) # 創建新的 Env
			params = n['params']['params']
			for param in params:
				env.add(param['id'], {'class':'?'})
			FUNC(n)
			env = env.parent # 退出 Env
		case 'params':
			PARAMS(n)
		case 'param':
			PARAM(n)
		case 'block':
			BLOCK(n)
		case 'expr':
			return EXPR(n)
		case 'mexpr':
			return MEXPR(n)
		case 'cexpr':
			return CEXPR(n)
		case 'bexpr':
			return BEXPR(n)
		case 'lrexpr': 
			return LREXPR(n)
		case 'list':
			return LIST(n)
		case 'dict':
			return DICT(n)
		case 'obj':
			return OBJ(n)
		case 'term':
			return TERM(n)
		case 'args': 
			return ARGS(n)
		case 'float':
			return FLOAT(n)
		case 'int':
			return INT(n)
		case 'str':
			return STR(n)
		case 'id':
			return ID(n)
		case 'var':
			id = n["id"]
			isNew = not env.findEnv(id)
			if isNew:
				env.add(id, {'class':'?'})
			VAR(n, isNew)

def STMTS(n):
	for stmt in n['stmts']:
		run(stmt)

def STMT(n):
	run(n['stmt'])

def IMPORT(n):
	error('尚未實作')
	# emit(f'import {n["id"]}')

def WHILE(n):
	while run(n['expr']):
		run(n['stmt'])

def FOR(n): # FOR = for VAR in EXPR: STMT
	error('尚未實作')
	"""
	# emit('for (')
	id = run(n['var']['id'])
	# emit(' in ')
	run(n['expr'])
	# emit(')')
	run(n['stmt'])
	"""

def IF(n):
	if run(n['expr']):
		run(n['stmt'])
	else:
		for el in n['elifList']:
			if run(el['expr']):
				run(el['stmt'])
		if n['elseStmt']:
			run(n['elseStmt'])

def RETURN(n):
	# emit('return ')
	return run(n['expr'])

def ASSIGN(n): # VAR = EXPR
	global env
	id = run(n['var'])
	value = run(n['expr'])
	var = env.find(id)
	if var:
		var['value'] = value

def VAR(n, isNew):
	return n['id']

def FUNC(n):
	env = Env(n['id'], env)
	run(n['params'])
	run(n['block'])
	env = env.parent

def PARAMS(n):
	params = n['params']
	for param in params:
		run(param['id'])

def PARAM(n):
	global env
	env.add({'id': n['id']})

def BLOCK(n): # BLOCK  = begin STMTS end
	level += 1
	run(n['stmts'])
	level -= 1

def EXPR(n): # EXPR = BEXPR (if EXPR else EXPR)?
	run(n['bexpr'])
	# (if EXPR else EXPR)? 尚未處理
def op2run(a, op, b):
	match op:
		case '+': return a+b
		case '-': return a-b
		case '*': return a*b
		case '/': return a/b
		case '%': return a%b
		case 'and':	return a and b
		case 'or': return a or b
		case '==': return a==b
		case '!=': return a!=b
		case '<=': return a<=b
		case '>=': return a>=b
		case '<': return a<b
		case '>': return a>b
		case _: error(f'op2run: op={op} not found!')

def opListRun(n):
	list1 = n['list']
	len1 = len(list1)
	t1 = run(list1[0])
	li = 1
	while li + 1 < len1:
		op = list1[li]
		e2 = run(list1[li+1])
		t3 = op2run(t1, op, e2)
		# t3 = ir.newTemp()
		# ir.op2(op, t1, e2, t3)
		t1 = t3
		li += 2
	return t1

def MEXPR(n):
	return opListRun(n)

def CEXPR(n):
	return opListRun(n)

def BEXPR(n):
	return opListRun(n)

def LREXPR(n): # LREXPR = ( EXPR )
	return run(n['expr'])

def LIST(n): # LIST = [ (EXPR ,)* EXPR? ]
	elist = n['list']
	rlist = []
	if len(elist)>0:
		for expr in elist:
			rlist.append(run(expr))
	return rlist

def DICT(n):
	pairs = n['pairs']
	rdict = {}
	for pair in pairs:
		value = run(pair['value'])
		rdict[pair['key']] = value
	return rdict

def OBJ(n): # OBJ = id | str | int | float | LREXPR
	ty = n['type']
	value = n['value']
	match ty:
		case 'lrexpr': return run(n['expr'])
		case 'id': return VAR(n)
		case 'int': return INT(n)
		case 'float': return FLOAT(n)
		case 'str': return STR(n)
		case _: error(f'OBJ:type error, type={ty} unknown')

def TERM(n): # TERM   = OBJ ( [EXPR] | . id | (ARGS) )*
	tlist = n['list']
	obj = tlist[0]
	o = run(obj['obj'])
	for t in tlist[1:]:
		op = t['type']
		if op == 'index':
			i = run(t['expr'])
			return o[i]
		elif op == 'member':
			# emit('.'+t['id'])
			error('TERM:member not support yet!')
		elif op == 'call':
			args = run(t['args'])
			return o(args)
		else:
			error(f'term: op = {op} 不合法！')

def ARGS(n): # ARGS = (EXPR ',')* EXPR? # args
	args = n['args']
	rlist = []
	if len(args)>0:
		for arg in args:
			rlist.append(run(arg))
	return rlist

def FLOAT(n):
	return float(n['value'])

def INT(n):
	return int(n['value'])

def STR(n):
	return n['value'].substr(1, -1)

def ID(n):
	return env.find(n['id'])['value']

# 測試詞彙掃描器
if __name__ == "__main__":
	from test0 import code
	code = 'print("Hello 你好！")'
	ast = parse(code)
	astDump(ast)
	run(ast)
	# print(ast)
