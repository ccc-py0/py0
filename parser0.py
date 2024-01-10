import sys
from lib0 import *
from lexer0 import lex
from env import Env

tokens = None
lines = None
file = None
ti = None
env = None

# prog = stmts
def parse(code, fname='<unknown file>'):
	global tokens, ti, lines, file, env
	file = fname
	lines = code.split('\n')
	lines = ['']+lines
	tokens = lex(code)
	ti = 0
	env = Env(None)
	return STMTS()

def perror(msg):
	tk = getTk()
	print(f'line {tk.line}\n{lines[tk.line]}\n{msg}')
	# sys.exit(1)
	raise Exception('perror')

def back():
	global ti
	ti -= 1

def isNextT(type):
	global tokens, ti
	if isEnd(): return False
	return tokens[ti].type == type
	
def isNext(value):
	global tokens, ti
	if isEnd(): return False
	return tokens[ti].value == value

def isNextSet(vset):
	global tokens, ti
	if isEnd(): return False
	return tokens[ti].value in vset

def isNextTSet(tset):
	global tokens, ti
	if isEnd(): return False
	return tokens[ti].type in tset

def isEnd():
	global tokens, ti
	return ti >= len(tokens)

def getTk():
	return tokens[ti]

def nextT(type):
	global tokens, ti
	if isEnd(): return False
	tk = tokens[ti]
	if isNextT(type):
		debug('tk = ', tk)
		ti += 1
		return tk.value
	else:
		perror(f'next should be {type}')

def next(value=None):
	global tokens, ti
	tk = tokens[ti]
	if value == None or isNext(value):
		debug('tk = ', tk)
		ti += 1
		return tk.value
	else:
		perror(f'parse:next error!')

# STMTS = STMT*
def STMTS():
	global ti
	stmts = []
	while not isEnd() and not isNextT('end'):
		s = STMT()
		stmts.append(s)
	return {'type':'stmts', 'stmts':stmts}

# STMT = BLOCK | FUNC | IF | WHILE | RETURN | ASSIGN | CALL

def STMT():
	s = None
	# print('STMT(): tk=', tokens[ti])
	if isNextT("begin"):
		s = BLOCK()
	elif isNext("import"):
		s = IMPORT()
	elif isNext("def"):
		s = FUNC()
	elif isNext("if"):
		s = IF()
	elif isNext("while"):
		s = WHILE()
	elif isNext("for"):
		s = FOR()
	elif isNext("return"):
		s = RETURN()
	elif isNextT("id"):
		id = next()
		if isNext("="):
			back()
			s = ASSIGN()
		else:
			back()
			s = TERM()
	else:
		perror('is not a statement (不是一個陳述！)')
	return {'type':'stmt', 'stmt':s}

def IMPORT():
	next('import')
	id = nextT('id')
	return  {'type':'import', 'id':id }

# FUNC = def id(PARAMS): BLOCK
def FUNC():
	global env
	fenv = Env(env)
	next('def')
	id = nextT('id')
	env.add(id, 'func')
	next('(')
	params = PARAMS()
	next(')')
	next(':')
	block = BLOCK()
	env = fenv
	return {'type':'func', 'class':'func', 'id':id, 'params':params, 'block':block}

# IF = if expr: stmt (elif stmt)* (else stmt)?
def IF():
	next('if')
	expr = EXPR()
	next(':')
	stmt = STMT()
	
	elifList = []
	while isNext('elif'):
		next('elif')
		e = EXPR()
		next(':')
		s = STMT()
		elifList.extend({'type':'elif', 'expr':e, 'stmt':s})
		
	elseStmt = None
	if isNext('else'):
		next('else')
		elseStmt = STMT()
	return {'type':'if', 'expr':expr, 'stmt':stmt, 'elifList':elifList, 'elseStmt':elseStmt}

# WHILE = while expr: stmt
def WHILE():
	next('while')
	e = EXPR()
	next(':')
	s = STMT()
	return {'type':'while', 'expr':e, 'stmt':s}

# FOR = for VAR in EXPR: STMT
def FOR():
	next('for')
	v = VAR()
	next('in')
	e = EXPR()
	next(':')
	s = STMT()
	return {'type':'for', 'var':v, 'expr': e, 'stmt':s }

# RETURN = return expr 
def RETURN():
	next('return')
	e = EXPR()
	return {'type':'return', 'expr':e}

# ASSIGN = VAR = EXPR
def ASSIGN():
	global env
	v = VAR()
	next('=')
	e = EXPR()

	vClass = env.findClass(v['id'])
	if vClass:
		v['class']=vClass
	else:
		v['class'] = e['class']

	return {'type':'assign', 'var':v, 'expr':e}

# PARAMS = PARAM*
def PARAMS():
	params = []
	while not isNext(")"):
		p = PARAM()
		params.append(p)
	return {'type':'params', 'params':params}

# PARAM = id
def PARAM():
	id = nextT('id')
	return {'type':'param', 'id':id}

"""
# TYPE = id
def TYPE():
	ty = nextT('id')
	return {'type':'type', 'class':ty}
"""

level = 0
# BLOCK = begin STMTS end
def BLOCK():
	nextT('begin')
	s = STMTS()
	nextT('end')
	return {'type':'block', 'stmts':s }

# EXPR = BEXPR (if EXPR else EXPR)?
def EXPR():
	bexpr = BEXPR()
	"""
	這段不能加，否則像是 
		msg = 'a<5'
		if a < 5: print(msg)
	這樣的程式，就會被誤認然後發生解析錯誤了。 真正的 python 不會
	if isNext('if'):
		next('if')
		expr1 = EXPR()
		next('else')
		expr2 = EXPR()
		return {'type':'expr', 'bexpr':bexpr, 'expr1':expr1, 'expr2':expr2 }
	else:
	"""
	return bexpr

# BEXPR = CEXPR ((and|or) CEXPR)*
def BEXPR():
	e = CEXPR()
	elist = [e]
	while isNextSet(['and', 'or']):
		op = next()
		e = CEXPR()
		elist.extend([op, e])
	return e if len(elist)==1 else {'type':'bexpr', 'class':'bool', 'list':elist}

# CEXPR = MEXPR (['==', '!=', '<=', '>=', '<', '>'] MEXPR)*
def CEXPR():
	e = MEXPR()
	elist = [e]
	while isNextSet(['==', '!=', '<=', '>=', '<', '>']):
		op = next()
		e = MEXPR()
		elist.extend([op, e])
	return e if len(elist)==1 else {'type':'cexpr', 'class':'bool', 'list':elist}

# MEXPR = ITEM (['+', '-', '*', '/', '%'] ITEM)*
def MEXPR():
	e = ITEM()
	elist = [e]
	while isNextSet(['+', '-', '*', '/', '%']):
		op = next()
		e = ITEM()
		elist.extend([op,e])
	return e if len(elist)==1 else {'type':'mexpr', 'class': e['class'], 'list':elist}

# ITEM = LIST | DICT | FACTOR
def ITEM():
	if isNext('['):
		e = LIST()
	elif isNext('{'):
		e = DICT()
	else:
		e = FACTOR()
	return e

# LIST  = [ (EXPR ,)* EXPR? ]
def LIST():
	next('[')
	elist = []
	while not isNext(']'):
		e = EXPR()
		elist.append(e)
		if not isNext(']'):
			next(',')
	next(']')
	return {'type':'list', 'class':'list', 'list': elist}

# DICT = { (PAIR ,)* PAIR? }
def DICT():
	next('{')
	pairs = []
	while not isNext('}'):
		key = nextT('str')
		next(':')
		value = EXPR()
		pairs.append({'type':'pair', 'key':key, 'value': value})
		if not isNext('}'): next(',')
	next('}')
	return  {'type':'dict', 'class':'dict', 'pairs':pairs}

# FACTOR = (!-~)* TERM
def FACTOR():
	e = TERM()
	return e

# TERM   = OBJ ( [EXPR] | . id | (ARGS) )*
def TERM():
	obj = OBJ()
	tlist = [obj]
	while isNextSet(['(', '.', '[']):
		if isNext('('):
			next('(')
			args = ARGS()
			next(')')
			tlist.append({'type':'call', 'args':args})
		elif isNext('['):
			next('[')
			e = EXPR()
			next(']')
			tlist.append({'type':'index', 'expr':e})
		elif isNext('.'): # member
			next('.')
			id = nextT('id')
			tlist.append({'type':'member', 'id':id})
	return  {'type':'term', 'class':obj['class'], 'list':tlist}

# OBJ = id | string | integer | float | LREXPR
# LREXPR = ( expr )
def OBJ():
	obj = None
	tk = getTk()
	ty = tk.type
	if ty in ['str', 'int', 'float']:
		next()
		obj = {'type':ty, 'class':ty, 'value':tk.value}
	elif isNextT('id'):
		id = next()
		obj = {'type':'id', 'class':env.findClass(id), 'id':id}
	elif isNext('('):
		next('(')
		e = EXPR()
		next(')')
		obj = {'type':'lrexpr', 'class':e['class'], 'expr':e}
	else:
		error(f'OBJ:type={ty} 錯誤！')
	return {'type':'obj', 'class':obj['class'], 'obj':obj }

# array = [ expr* ]

# map = { (str:expr)* }

# ARGS  = (EXPR ',')* EXPR?
def ARGS():
	args = []
	while not isNext(')'):
		e = EXPR()
		args.append(e)
		if isNext(','):
			next(',')
	return {'type':'args', 'args':args}

def VAR():
	id = nextT('id')
	return {'type':'var', 'class':env.findClass(id), 'id':id}

def nodeDump(node, level):
	if not isinstance(node, dict):
		print(f'{"  "*level}{node}')
		return
	
	for _, (k, v) in enumerate(node.items()):
		if v==None or isinstance(v, str):
			print(f'{"  "*level}{k}:{v}')
		elif isinstance(v, list):
			for o in v:
				nodeDump(o, level+1)
		else:
			print(f'{"  "*level}{k}:')
			nodeDump(v, level+1)

def astDump(ast):
	nodeDump(ast, 0)

# 測試詞彙掃描器
if __name__ == "__main__":
	from test0 import code
	ast = parse(code)
	astDump(ast)
	# print(ast)
