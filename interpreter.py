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

def run(n):
	global env
	ty = n['type']
	match ty:
		case 'stmts':
			STMTS(n)
		case 'expr':
			return EXPR(n)
		case 'mexpr':
			return MEXPR(n)
		case 'cexpr':
			return CEXPR(n)
		case 'bexpr':
			return BEXPR(n)
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
			FUNC(n)
		case 'params':
			PARAMS(n)
		case 'param':
			PARAM(n)
		case 'block':
			BLOCK(n)
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
				env.add(id, {'class':'?', 'value':None})
			VAR(n, isNew)
		case _:
			error(n, f'run: type {ty} not found')

def STMTS(n):
	# print('STMTS:env=', env)
	for stmt in n['stmts']:
		STMT(stmt)

def STMT(n):
	run(n['stmt'])

def FUNC(n):
	fname = n['id']
	f = Function(fname, n, env)
	env.add(fname, {'class':'func', 'value':f})

def PARAMS(n, args):
	params = n['params']
	for i, param in enumerate(params):
		env.add(param['id'], {'class':'?', 'value':args[i]})
		# PARAM(param)

# def PARAM(n):

def BLOCK(n): # BLOCK  = begin STMTS end
	global level
	level += 1
	# print('BLOCK: begin')
	# print('BLOCK:env=', env)
	run(n['stmts'])
	# print('BLOCK: end')
	level -= 1

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
	e = EXPR(n['expr'])
	print('IF:e=',e)
	if e: # EXPR(n['expr']):
		STMT(n['stmt'])
	else:
		for el in n['elifList']:
			if EXPR(el['expr']):
				STMT(el['stmt'])
		if n['elseStmt']:
			STMT(n['elseStmt'])

def RETURN(n): # ccc , return 沒跳出函數
	# emit('return ')
	return run(n['expr'])

def ASSIGN(n): # VAR = EXPR
	id = run(n['var'])
	value = run(n['expr'])
	var = env.find(id)
	if var:
		var['value'] = value

def VAR(n, isNew):
	return n['id']

def EXPR(n): # EXPR = BEXPR (if EXPR else EXPR)?
	# print('EXPR:n=', n)
	return BEXPR(n)
	# (if EXPR else EXPR)? 尚未處理

def op2run(a, op, b):
	print(f'a={a} op={op} b={b}')
	if a == -2: error('op2run: exceed!')
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
		t1 = op2run(t1, op, e2)
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

def TERM(n): # TERM   = OBJ ( [EXPR] | . id | (ARGS) )*
	global env
	tlist = n['list']
	obj = tlist[0]
	o = run(obj['obj'])
	for t in tlist[1:]:
		op = t['type']
		if op == 'index':
			i = run(t['expr'])
			o = o[i]
		elif op == 'member':
			# emit('.'+t['id'])
			error('TERM:member not support yet!')
		elif op == 'call':
			args = run(t['args'])
			# print(f'o={o} call {args}')
			if isinstance(o, Function):
				fname = obj['obj']['id']
				# print('TERM: fname=', fname)
				env = Env(o.fname, env)
				# print('call: env=', env)
				# print('run:params')
				PARAMS(o.node['params'], args) # ccc back
				# print('call: after params env=', env)
				# print('run:block')
				run(o.node['block']) # ccc: 在執行函數到一半，如何讓 return 跳出函數。
				# 想法，在 env 中設一變數，當該變數為 return 狀態時，所有 stmt 都會直接不執行。
				env = env.parent
			else: # Python 本身的函數
				args = run(t['args'])
				o = o(*args)
		else:
			error(f'term: op = {op} 不合法！')
	return o

def ARGS(n): # ARGS = (EXPR ',')* EXPR? # args
	args = n['args']
	rlist = []
	if len(args)>0:
		for arg in args:
			rlist.append(run(arg))
	return rlist

def OBJ(n): # OBJ = id | str | int | float | LREXPR
	ty = n['type']
	print(f'OBJ:n={n}')
	match ty:
		case 'lrexpr': return run(n['expr'])
		case 'id': return VAR(n)
		case 'int': return INT(n)
		case 'float': return FLOAT(n)
		case 'str': return STR(n)
		case _: error(f'OBJ:type error, type={ty} unknown')

def FLOAT(n):
	return float(n['value'])

def INT(n):
	return int(n['value'])

def STR(n):
	return n['value'][1:-1]

def ID(n):
	print('ID: id=', n['id'])
	# print(f'ID: env={env}')
	obj = env.find(n['id'])
	print('ID:obj=', obj)
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
