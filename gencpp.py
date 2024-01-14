from lib0 import *
from parser0 import parse
from genx import *

class GenCpp(GenX):
	def __init__(self):
		map = {
			"None": "any",
			"int":"int",
			"str":"string",
			"float":"float",
			"list":"vector",
			"dict":"map"
		}
		super().__init__(typed=True, classMap=map)

	def IMPORT(self, n):
		id = n['id']
		self.emit(f'#include <{id}.h>')

	def VAR(self, n, isNew):
		if isNew and self.typed and n['class']: # 第一次出現的變數(新的) ，要輸出 class，而且有 class 了
			self.emit(self.mapClass(n['class'])+' ')
		self.emit(n['id'])

	def LIST(self, n): # LIST = [ (EXPR ,)* EXPR? ]
		self.emit('{')
		elist = n['list']
		if len(elist)>0:
			for expr in elist[0:-1]:
				self.gen(expr)
				self.emit(',')
			self.gen(elist[-1])
		self.emit('}')

	def FUNC(self, n):
		self.emit(f'{self.mapClass(n["class"])} {n["id"]}(')
		self.gen(n['params'])
		self.emit(f')')
		self.gen(n['block'])

	def PARAMS(self, n):
		params = n['params']
		if len(params) == 0: return
		for i, param in enumerate(params):
			self.emit(f'{self.mapClass(param["class"])} {param["id"]}')
			if i != len(params)-1:
				self.emit(',')

	def STMT(self, n):
		ty = n['stmt']['type']
		if ty != 'block': # block 也是一種 stmt，但不需要換行，因為裡面的 stmt* 每個都會換
			self.emit(f'\n{self.indent()}')
		self.gen(n['stmt'])
		if not ty in ['block', 'if', 'while', 'func', 'for', 'import']:
			self.emit(';')
		
	def STR(self, n):
		self.emit(n['value'].replace("'",'"'))

	def FOR(self, n): # FOR = for VAR in EXPR: STMT
		self.emit('for (auto ')
		self.gen(n['var'])
		self.emit(' : ')
		self.gen(n['expr'])
		self.emit(')')
		self.gen(n['stmt'])

	def BEXPR(self, n):
		opMap = {'and':'&&', 'or':'||'}
		for e in n['list']:
			if isinstance(e, str): # op
				self.emit(f' {opMap[e]} ')
			else:
				self.gen(e)
