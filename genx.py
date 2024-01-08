from gen import gen
from lib0 import *

class GenX:
	def __init__(self):
		self.level = 0

	def indent(self):
		return '\t'*self.level

	def STMTS(self, n):
		for stmt in n['stmts']:
			gen(stmt, self)

	def STMT(self, n):
		if n['stmt']['type'] != 'block': # block 也是一種 stmt，但不需要換行，因為裡面的 stmt* 每個都會換
			emit(f'\n{self.indent()}')
		gen(n['stmt'], self)

	def WHILE(self, n):
		emit('while (')
		gen(n['expr'], self)
		emit(')')
		gen(n['stmt'], self)

	def FOR(self, n):
		emit('for (')
		emit(n['id'])
		emit(' in ')
		gen(n['expr'], self)
		emit(')')
		gen(n['stmt'], self)

	def IF(self, n):
		emit('if (')
		gen(n['expr'], self)
		emit(')')
		gen(n['stmt'], self)
		for el in n['elifList']:
			emit('else if ')
			gen(el['expr'], self)
			gen(el['stmt'], self)
		if n['elseStmt']:
			emit('else')
			gen(n['elseStmt'], self)

	def RETURN(self, n):
		emit('return ')
		gen(n['expr'], self)

	def ASSIGN(self, n):
		emit(f'{n["id"]} = ')
		gen(n['expr'], self)

	def FUNC(self, n):
		emit(f'function {n["id"]}(')
		gen(n['params'], self)
		emit(')')
		gen(n['block'], self)

	def PARAMS(self, n):
		params = n['params']
		for param in params[0:-1]:
			gen(param, self)
			emit(',')
		gen(params[-1], self)

	def PARAM(self, n):
		emit(n['id'])

	def BLOCK(self, n): # BLOCK  = begin STMTS end
		emit(' {')
		self.level += 1
		gen(n['stmts'], self)
		self.level -= 1
		emit('\n'+self.indent()+'}')
		emit('\n')

	def EXPR(self, n): # EXPR = BEXPR (if EXPR else EXPR)?
		gen(n['bexpr'], self)
		# (if EXPR else EXPR)? 尚未處理

	def MEXPR(self, n):
		for e in n['list']:
			if isinstance(e, str): # op
				emit(f' {e} ')
			else:
				gen(e, self)

	def CEXPR(self, n):
		self.MEXPR(n)

	def BEXPR(self, n):
		self.MEXPR(n)

	def LREXPR(self, n): # LREXPR = ( EXPR )
		emit('(')
		gen(n['expr'], self)
		emit(')')

	def ARRAY(self, n): # ARRAY = [ (EXPR ,)* EXPR? ]
		emit('[')
		elist = n['list']
		if len(elist)>0:
			for expr in elist[0:-1]:
				gen(expr, self)
				emit(',')
			gen(elist[-1], self)
		emit(']')

	def MAP(self, n):
		emit('{')
		pairs = n['pairs']
		for pair in pairs[0:-1]:
			emit(pair['key']+':')
			gen(pair['value'], self)
			emit(',')
		emit(pairs[-1]['key']+':')
		gen(pairs[-1]['value'], self)
		emit('}')

	def OBJ(self, n): # OBJ = id | string | int | float | LREXPR
		if n['type'] == 'lrexpr':
			gen(n['expr'], self)
		else:
			emit(n['value'])

	def TERM(self, n): # TERM   = OBJ ( [EXPR] | . id | (ARGS) )*
		tlist = n['list']
		obj = tlist[0]
		gen(obj['obj'], self)
		for t in tlist[1:]:
			op = t['type']
			if op == 'index':
				emit('[')
				gen(t['expr'], self)
				emit(']')
			elif op == 'member':
				emit('.'+t['id'])
			elif op == 'call':
				emit('(')
				gen(t['args'], self)
				emit(')')
			else:
				error(f'term: op = {op} 不合法！')

	def ARGS(self, n): # ARGS = (EXPR ',')* EXPR? # args
		args = n['args']
		if len(args)>0:
			for arg in args[0:-1]:
				gen(arg, self)
				emit(' , ')
			gen(args[-1], self)

	def FLOAT(self, n):
		emit(n['value'])

	def INTEGER(self, n):
		emit(n['value'])

	def STRING(self, n):
		emit(n['value'])

	def ID(self, n):
		emit(n['id'])

