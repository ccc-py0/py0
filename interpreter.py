# from lib0 import *
from env import Env
from parser0 import *

class Function:
	def __init__(self, fname, node, env):
		self.fname = fname
		self.node = node
		self.env = env

def globalEnv():
	env = Env('global', None)
	env.vars = {
		'print':{'class':'func', 'value':print }
	}
	return env

env = gEnv = globalEnv()
level = 0

def error(n, msg):
	print(f'Error: \n{msg}')
	raise Exception('interpereter:error')

def interpret(code):
	ast = parse(code)
	run(ast)

def run(n):
	match n['type']:
		case 'stmts': STMTS(n)
		case 'expr':  return EXPR(n)
		case 'mexpr': return MEXPR(n)
		case 'cexpr': return CEXPR(n)
		case 'bexpr': return BEXPR(n)
		case 'stmt':  STMT(n)
		case 'import':IMPORT(n)
		case 'while': WHILE(n)
		case 'for': FOR(n)
		case 'if': IF(n)
		case 'return': RETURN(n)
		case 'assign': ASSIGN(n)
		case 'func': FUNC(n)
		case 'params': PARAMS(n)
		case 'param': PARAM(n)
		case 'block': BLOCK(n)
		case 'lrexpr': return LREXPR(n)
		case 'list': return LIST(n)
		case 'dict': return DICT(n)
		case 'obj': return OBJ(n)
		case 'term': return TERM(n)
		case 'args': return ARGS(n)
		case 'float': return FLOAT(n)
		case 'int': return INT(n)
		case 'str': return STR(n)
		case 'id': return ID(n)
		case 'var': return VAR(n)
		case _: error(n, f'run: type {n["type"]} not found')

# STMTS  = STMT* 
def STMTS(n):
	# print('STMTS:env=', env)
	for stmt in n['stmts']:
		if env.returned: break
		STMT(stmt)

 # STMT = BLOCK | FUNC | IF | WHILE | RETURN | ASSIGN | CALL | IMPORT
def STMT(n):
	run(n['stmt'])

# FUNC = def id(PARAMS): BLOCK
def FUNC(n):
	fname = n['id']
	f = Function(fname, n, env)
	env.add(fname, {'class':'func', 'value':f})

# PARAMS = PARAM*
def PARAMS(n, args):
	params = n['params']
	for i, param in enumerate(params):
		env.add(param['id'], {'class':'?', 'value':args[i]})

# BLOCK  = begin STMTS end
def BLOCK(n):
	global level
	level += 1
	STMTS(n['stmts'])
	level -= 1

# IMPORT = import id
def IMPORT(n):
	error('尚未實作')
	# emit(f'import {n["id"]}')

# WHILE  = while EXPR: STMT
def WHILE(n):
	while EXPR(n['expr']):
		STMT(n['stmt'])

# FOR = for VAR in EXPR: STMT
def FOR(n):
	error('尚未實作')
	"""
	# emit('for (')
	id = VAR(n['var']['id'])
	# emit(' in ')
	EXPR(n['expr'])
	# emit(')')
	STMT(n['stmt'])
	"""

# IF = if EXPR: STMT (elif STMT)* (else STMT)?
def IF(n):
	e = EXPR(n['expr'])
	# print('IF:e=',e)
	if e: # EXPR(n['expr']):
		STMT(n['stmt'])
	else:
		for el in n['elifList']:
			if EXPR(el['expr']):
				STMT(el['stmt'])
		if n['elseStmt']:
			STMT(n['elseStmt'])

# RETURN = return EXPR
def RETURN(n):
	e = EXPR(n['expr'])
	env.returnValue = e
	env.returned = True
	return e

# ASSIGN = VAR = EXPR
def ASSIGN(n):
	r = VAR(n['var'])
	value = EXPR(n['expr'])
	r['value'] = value

# VAR = id (:id)?
def VAR(n):
	id = n["id"]
	r = env.find(id)
	if not r:
		r = {'class':'?', 'value':None}
		env.add(id, r)
	return r

def op2run(a, op, b):
	# print(f'a={a} op={op} b={b}')
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

def opListRun(n, ty):
	if n['type'] != ty:
		return run(n)
	list1 = n['list']
	len1 = len(list1)
	t1 = run(list1[0])
	li = 1
	while li + 1 < len1:
		op = list1[li]
		e2 = run(list1[li+1])
		t1 = op2run(t1, op, e2)
		li += 2
	return t1

# EXPR = BEXPR (if EXPR else EXPR)?
def EXPR(n):
	return BEXPR(n)	# (if EXPR else EXPR)? 尚未處理

# BEXPR  = CEXPR ((and|or) CEXPR)*
def BEXPR(n):
	return opListRun(n, 'bexpr')

# CEXPR = MEXPR (['==', '!=', '<=', '>=', '<', '>'] MEXPR)*
def CEXPR(n):
	return opListRun(n, 'cexpr')

# MEXPR = ITEM (['+', '-', '*', '/', '%'] ITEM)*
def MEXPR(n):
	return opListRun(n, 'mexpr')

# ITEM = LIST | DICT | FACTOR
def ITEM(n): # LIST | DICT | FACTOR
	return run(n)

def LREXPR(n): # LREXPR = ( EXPR )
	return EXPR(n['expr'])

def LIST(n): # LIST = [ (EXPR ,)* EXPR? ]
	elist = n['list']
	rlist = []
	if len(elist)>0:
		for expr in elist:
			rlist.append(EXPR(expr))
	return rlist

def DICT(n):
	pairs = n['pairs']
	rdict = {}
	for pair in pairs:
		value = EXPR(pair['value'])
		rdict[pair['key']] = value
	return rdict

# FACTOR = (!-~)* TERM
def FACTOR(n):
	return TERM(n) # 目前沒處理 (!-~)*

def TERM(n): # TERM   = OBJ ( [EXPR] | . id | (ARGS) )*
	global env
	tlist = n['list']
	obj = tlist[0]
	o = OBJ(obj) # run(obj['obj']) # 可能直接下降，不能用 OBJ() ...
	for t in tlist[1:]:
		op = t['type']
		if op == 'index':
			i = EXPR(t['expr'])
			o = o[i]
		elif op == 'member':
			# emit('.'+t['id'])
			error('TERM:member not support yet!')
		elif op == 'call':
			args = ARGS(t['args'])
			if isinstance(o, Function):
				env = Env(o.fname, env)
				PARAMS(o.node['params'], args) # ccc back
				BLOCK(o.node['block'])
				o = env.returnValue
				env = env.parent
			else: # Python 本身的函數
				args = ARGS(t['args'])
				o = o(*args)
		else:
			error(f'term: op = {op} 不合法！')
	return o

def ARGS(n): # ARGS = (EXPR ',')* EXPR? # args
	args = n['args']
	rlist = []
	if len(args)>0:
		for arg in args:
			rlist.append(EXPR(arg))
	return rlist

def OBJ(n): # OBJ = id | str | int | float | LREXPR
	if n['type'] == 'obj': # OBJ
		return OBJ(n['obj'])
	else: # 沒經過 OBJ 直接下降 (n 不是 OBJ)
		return run(n)

def FLOAT(n):
	return float(n['value'])

def INT(n):
	return int(n['value'])

def STR(n):
	return n['value'][1:-1]

def ID(n):
	obj = env.find(n['id'])
	return obj['value']

# code = 'print("Hello 你好！")'

code = """
def fib(n:int):
	if n == 0 or n == 1:
		return 1

	return fib(n - 1) + fib(n - 2)

print('fib(5)=', fib(5))
"""

# 測試詞彙掃描器
if __name__ == "__main__":
	# from test0 import code
	ast = parse(code)
	# astDump(ast)
	run(ast)
	# print(ast)
