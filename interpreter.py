from lib0 import *
from env import Env

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
			# print('func:level=', level)
			env = Env(n['id'], env) # 創建新的 Env
			params = n['params']['params']
			for param in params:
				# print('param=', param)
				env.add(param['id'], '?')
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
				env.add(id, '?')
			VAR(n, isNew)

def STMTS(n):
	for stmt in n['stmts']:
		run(stmt)

def STMT(n):
	run(n['stmt'])

def IMPORT(n):
	emit(f'import {n["id"]}')

def WHILE(n):
	emit('while (')
	run(n['expr'])
	emit(')')
	run(n['stmt'])

def FOR(n): # FOR = for VAR in EXPR: STMT
	emit('for (')
	run(n['var'])
	emit(' in ')
	run(n['expr'])
	emit(')')
	run(n['stmt'])

def IF(n):
	emit('if (')
	run(n['expr'])
	emit(')')
	run(n['stmt'])
	for el in n['elifList']:
		emit('else if ')
		run(el['expr'])
		run(el['stmt'])
	if n['elseStmt']:
		emit('else')
		run(n['elseStmt'])

def RETURN(n):
	emit('return ')
	run(n['expr'])

def ASSIGN(n):
	run(n['var'])
	emit(' = ')
	run(n['expr'])

def VAR(n, isNew):
	emit(n['id'])
	if isNew and n['class']: # 第一次出現的變數(新的) ，要輸出 class，而且有 class 了
		pass
		# emit(':'+mapClass(n['class']))

def PARAM(n):
	emit(n['id'])
	if n['class']:
		emit(':'+n['class'])

def FUNC(n):
	emit('def ')
	emit(f'{n["id"]}(')
	run(n['params'])
	if n['class']:
		emit(f')->{n["class"]}:')
	else:
		emit(f'):')
	run(n['block'])

def PARAMS(n):
	params = n['params']
	if len(params) == 0: return
	for param in params[0:-1]:
		run(param)
		emit(',')
	run(params[-1])

def BLOCK(n): # BLOCK  = begin STMTS end
	emit(' {')
	level += 1
	# print('block:level=', level)
	run(n['stmts'])
	# print('block:level=', level)
	level -= 1
	emit('\n'+indent()+'}')
	emit('\n')

def EXPR(n): # EXPR = BEXPR (if EXPR else EXPR)?
	run(n['bexpr'])
	# (if EXPR else EXPR)? 尚未處理

def MEXPR(n):
	for e in n['list']:
		if isinstance(e, str): # op
			emit(f' {e} ')
		else:
			run(e)

def CEXPR(n):
	MEXPR(n)

def BEXPR(n):
	MEXPR(n)

def LREXPR(n): # LREXPR = ( EXPR )
	emit('(')
	run(n['expr'])
	emit(')')

def LIST(n): # LIST = [ (EXPR ,)* EXPR? ]
	emit('[')
	elist = n['list']
	if len(elist)>0:
		for expr in elist[0:-1]:
			run(expr)
			emit(',')
		run(elist[-1])
	emit(']')

def DICT(n):
	emit('{')
	pairs = n['pairs']
	for pair in pairs[0:-1]:
		emit(pair['key']+':')
		run(pair['value'])
		emit(',')
	emit(pairs[-1]['key']+':')
	run(pairs[-1]['value'])
	emit('}')

def OBJ(n): # OBJ = id | string | int | float | LREXPR
	if n['type'] == 'lrexpr':
		run(n['expr'])
	else:
		emit(n['value'])

def TERM(n): # TERM   = OBJ ( [EXPR] | . id | (ARGS) )*
	tlist = n['list']
	obj = tlist[0]
	run(obj['obj'])
	for t in tlist[1:]:
		op = t['type']
		if op == 'index':
			emit('[')
			run(t['expr'])
			emit(']')
		elif op == 'member':
			emit('.'+t['id'])
		elif op == 'call':
			emit('(')
			run(t['args'])
			emit(')')
		else:
			error(f'term: op = {op} 不合法！')

def ARGS(n): # ARGS = (EXPR ',')* EXPR? # args
	args = n['args']
	if len(args)>0:
		for arg in args[0:-1]:
			run(arg)
			emit(' , ')
		run(args[-1])

def FLOAT(n):
	emit(n['value'])

def INT(n):
	emit(n['value'])

def STR(n):
	emit(n['value'])

def ID(n):
	emit(n['id'])


