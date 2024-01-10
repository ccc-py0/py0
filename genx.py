from lib0 import *
from env import Env

class GenX:
	def __init__(self, typed=False):
		self.level = 0
		self.emits = []
		self.env = Env(None)
		self.typed = typed

	def STMTS(self, n):
		for stmt in n['stmts']:
			self.gen(stmt)

	def STMT(self, n):
		if n['stmt']['type'] != 'block': # block 也是一種 stmt，但不需要換行，因為裡面的 stmt* 每個都會換
			self.emit(f'\n{self.indent()}')
		self.gen(n['stmt'])

	def IMPORT(self, n):
		self.emit(f'import {n["id"]}')

	def WHILE(self, n):
		self.emit('while (')
		self.gen(n['expr'])
		self.emit(')')
		self.gen(n['stmt'])

	def FOR(self, n): # FOR = for VAR in EXPR: STMT
		self.emit('for (')
		self.gen(n['var'])
		self.emit(' in ')
		self.gen(n['expr'])
		self.emit(')')
		self.gen(n['stmt'])

	def IF(self, n):
		self.emit('if (')
		self.gen(n['expr'])
		self.emit(')')
		self.gen(n['stmt'])
		for el in n['elifList']:
			self.emit('else if ')
			self.gen(el['expr'])
			self.gen(el['stmt'])
		if n['elseStmt']:
			self.emit('else')
			self.gen(n['elseStmt'])

	def RETURN(self, n):
		self.emit('return ')
		self.gen(n['expr'])

	def ASSIGN(self, n):
		self.gen(n['var'])
		self.emit(' = ')
		self.gen(n['expr'])

	def VAR(self, n, isNew):
		if isNew: self.emit('var ')
		self.emit(n['id'])
		if self.typed: self.emit(':'+n['class'])

	def FUNC(self, n):
		self.emit(f'function {n["id"]}(')
		self.gen(n['params'])
		self.emit(')')
		self.gen(n['block'])

	def PARAMS(self, n):
		params = n['params']
		if len(params) == 0: return
		for param in params[0:-1]:
			self.gen(param)
			self.emit(',')
		self.gen(params[-1])

	def PARAM(self, n):
		self.emit(n['id'])

	def BLOCK(self, n): # BLOCK  = begin STMTS end
		self.emit(' {')
		self.level += 1
		# print('block:level=', self.level)
		self.gen(n['stmts'])
		# print('block:level=', self.level)
		self.level -= 1
		self.emit('\n'+self.indent()+'}')
		self.emit('\n')

	def EXPR(self, n): # EXPR = BEXPR (if EXPR else EXPR)?
		self.gen(n['bexpr'])
		# (if EXPR else EXPR)? 尚未處理

	def MEXPR(self, n):
		for e in n['list']:
			if isinstance(e, str): # op
				self.emit(f' {e} ')
			else:
				self.gen(e)

	def CEXPR(self, n):
		self.MEXPR(n)

	def BEXPR(self, n):
		self.MEXPR(n)

	def LREXPR(self, n): # LREXPR = ( EXPR )
		self.emit('(')
		self.gen(n['expr'])
		self.emit(')')

	def LIST(self, n): # LIST = [ (EXPR ,)* EXPR? ]
		self.emit('[')
		elist = n['list']
		if len(elist)>0:
			for expr in elist[0:-1]:
				self.gen(expr)
				self.emit(',')
			self.gen(elist[-1])
		self.emit(']')

	def DICT(self, n):
		self.emit('{')
		pairs = n['pairs']
		for pair in pairs[0:-1]:
			self.emit(pair['key']+':')
			self.gen(pair['value'])
			self.emit(',')
		self.emit(pairs[-1]['key']+':')
		self.gen(pairs[-1]['value'])
		self.emit('}')

	def OBJ(self, n): # OBJ = id | string | int | float | LREXPR
		if n['type'] == 'lrexpr':
			self.gen(n['expr'])
		else:
			self.emit(n['value'])

	def TERM(self, n): # TERM   = OBJ ( [EXPR] | . id | (ARGS) )*
		tlist = n['list']
		obj = tlist[0]
		self.gen(obj['obj'])
		for t in tlist[1:]:
			op = t['type']
			if op == 'index':
				self.emit('[')
				self.gen(t['expr'])
				self.emit(']')
			elif op == 'member':
				self.emit('.'+t['id'])
			elif op == 'call':
				self.emit('(')
				self.gen(t['args'])
				self.emit(')')
			else:
				error(f'term: op = {op} 不合法！')

	def ARGS(self, n): # ARGS = (EXPR ',')* EXPR? # args
		args = n['args']
		if len(args)>0:
			for arg in args[0:-1]:
				self.gen(arg)
				self.emit(' , ')
			self.gen(args[-1])

	def FLOAT(self, n):
		self.emit(n['value'])

	def INT(self, n):
		self.emit(n['value'])

	def STR(self, n):
		self.emit(n['value'])

	def ID(self, n):
		self.emit(n['id'])

	def emit(self, code):
		self.emits.append(code)

	def indent(self):
		return '\t'*self.level
	
	def emitCode(self):
		return ''.join(self.emits)
	
	def gen(self, n):
		t = n['type']
		match t:
			case 'stmts':
				self.STMTS(n)
			case 'stmt':
				self.STMT(n)
			case 'import':
				self.IMPORT(n)
			case 'while':
				self.WHILE(n)
			case 'for':
				self.FOR(n)
			case 'if':
				self.IF(n)
			case 'return':
				self.RETURN(n)
			case 'assign':
				self.ASSIGN(n)
			case 'func':
				# print('func:level=', self.level)
				self.env = Env(self.env) # 創建新的 Env
				params = n['params']['params']
				for param in params:
					# print('param=', param)
					self.env.add(param['id'], '?')
				self.FUNC(n)
				self.env = self.env.parent # 退出 Env
			case 'params':
				self.PARAMS(n)
			case 'param':
				self.PARAM(n)
			case 'block':
				self.BLOCK(n)
			case 'expr':
				self.EXPR(n)
			case 'mexpr':
				self.MEXPR(n)
			case 'cexpr':
				self.CEXPR(n)
			case 'bexpr':
				self.BEXPR(n)
			case 'lrexpr': 
				self.LREXPR(n)
			case 'list':
				self.LIST(n)
			case 'dict':
				self.DICT(n)
			case 'obj':
				self.OBJ(n)
			case 'term':
				self.TERM(n)
			case 'args': 
				self.ARGS(n)
			case 'float':
				self.FLOAT(n)
			case 'int':
				self.INT(n)
			case 'str':
				self.STR(n)
			case 'id':
				self.ID(n)
			case 'var':
				id = n["id"]
				isNew = not self.env.findEnv(id)
				if isNew:
					self.env.add(id, '?')
				self.VAR(n, isNew)
