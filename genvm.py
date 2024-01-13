from lib0 import *
from env import Env
from genx import GenX

class GenVm(GenX):
	def __init__(self, typed=False, classMap=None, vm=None):
		super().__init__(typed, classMap)
		self.vm = vm

	def emitCode(self):
		return self.vm.emitCode()

	def STMTS(self, n):
		for stmt in n['stmts']:
			self.gen(stmt)

	def STMT(self, n):
		# if n['stmt']['type'] != 'block': # block 也是一種 stmt，但不需要換行，因為裡面的 stmt* 每個都會換
		# 	self.emit(f'\n{self.indent()}')
		self.gen(n['stmt'])

	def IMPORT(self, n):
		self.vm.include(n["id"])

	def WHILE(self, n):
		vm = self.vm
		labelStart = vm.newLabel()
		labelEnd = vm.newLabel()
		vm.label(labelStart)
		e = self.gen(n['expr'])
		vm.jne(e, labelEnd)
		self.gen(n['stmt'])
		vm.label(labelEnd)
	
	def FOR(self, n): # FOR = for VAR in EXPR: STMT
		error('尚未實作')
	"""
		self.emit('for (')
		self.gen(n['var'])
		self.emit(' in ')
		self.gen(n['expr'])
		self.emit(')')
		self.gen(n['stmt'])
	"""

	def IF(self, n):
		vm = self.vm
		e = self.gen(n['expr'])
		nextLabel = vm.newLabel()
		vm.jne(e, nextLabel)
		self.gen(n['stmt'])
		vm.label(nextLabel)
		for el in n['elifList']:
			e = self.gen(el['expr'])
			nextLabel = vm.newLabel()
			vm.jne(e, nextLabel)
			self.gen(el['stmt'])
			vm.label(nextLabel)
		if n['elseStmt']:
			e = self.gen(n['elseStmt'])

	def RETURN(self, n):
		e = self.gen(n['expr'])
		self.vm.ret(e)

	def ASSIGN(self, n):
		v = self.gen(n['var'])
		e = self.gen(n['expr'])
		self.assign(v, e)

	def VAR(self, n, isNew):
		return n['id']
		# if isNew and self.typed and n['class']: # 第一次出現的變數(新的) ，要輸出 class，而且有 class 了
			# self.emit(':'+self.mapClass(n['class']))

	def PARAM(self, n):
		self.vm.param(n['id'])
		# if self.typed and n['class']:
		#	self.emit(':'+n['class'])

	def FUNC(self, n):
		vm = self.vm
		vm.func(n['id'])
		self.gen(n['params'])
		self.gen(n['block'])
		vm.fend()

	def PARAMS(self, n):
		params = n['params']
		if len(params) == 0: return
		for param in params[0:-1]:
			self.gen(param)
		self.gen(params[-1])

	def BLOCK(self, n): # BLOCK  = begin STMTS end
		self.level += 1
		self.gen(n['stmts'])
		self.level -= 1

	def EXPR(self, n): # EXPR = BEXPR (if EXPR else EXPR)?
		return self.gen(n['bexpr'])
		# (if EXPR else EXPR)? 尚未處理

	def opListGen(self, n):
		vm = self.vm
		list1 = n['list']
		len1 = len(list1)
		t1 = self.gen(list1[0])
		li = 1
		while li + 1 < len1:
			op = list1[li]
			e2 = self.gen(list1[li+1])
			t3 = vm.newTemp()
			vm.op2(op, t1, e2, t3)
			t1 = t3
			li += 2
		return t1

	def MEXPR(self, n):
		return self.opListGen(n)

	def CEXPR(self, n):
		return self.opListGen(n)

	def BEXPR(self, n):
		return self.opListGen(n)

	def LREXPR(self, n): # LREXPR = ( EXPR )
		return self.gen(n['expr'])

	"""
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
	"""

	def OBJ(self, n): # OBJ = id | str | int | float | LREXPR
		vm = self.vm
		# print(f'OBJ:n={n}')
		ty = n['obj']['type']
		match ty:
			case 'lrexpr':
				return self.gen(n['expr'])
			case 'id':
				return n['value']
			case 'str' | 'int' | 'float':
				t = self.newTemp()
				vm.assign(t, n["value"])
				return t

	def ARGS(self, n): # ARGS = (EXPR ',')* EXPR? # args
		args = n['args']
		if len(args)>0:
			for arg in args:
				e = self.gen(arg)
				self.vm.arg(e)


	def TERM(self, n): # TERM   = OBJ ( [EXPR] | . id | (ARGS) )*
		vm = self.vm
		tlist = n['list']
		obj = tlist[0]
		o = self.gen(obj['obj'])
		for t in tlist[1:]:
			op = t['type']
			if op == 'index':
				idx = self.gen(t['expr'])
				tmp = self.newTemp()
				vm.index(o, idx, tmp)
			elif op == 'member':
				tmp = self.newTemp()
				vm.member(o, t['id'], tmp)
			elif op == 'call':
				self.gen(t['args'])
				tmp = vm.newTemp()
				vm.call(o, tmp)
			else:
				error(f'term: op = {op} 不合法！')
			o = tmp
		return o

	def FLOAT(self, n):
		return n['value']

	def INT(self, n):
		return n['value']

	def STR(self, n):
		return n['value']

	def ID(self, n):
		return n['id']
