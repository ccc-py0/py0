from lib0 import *
from parser0 import parse
from genx import GenX

class GenC(GenX):
	def IMPORT(self, n):
		id = n['id']
		self.emit(f'#include <{id}.h>')

	def FUNC(self, n):
		self.emit(f'{n["class"]} {n["id"]}(')
		self.gen(n['params'])
		self.emit(f')')
		self.gen(n['block'])

	def PARAMS(self, n):
		params = n['params']
		if len(params) == 0: return
		for i, param in enumerate(params):
			self.emit(f'{param["class"]} {param["id"]}')
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

	def FOR(self, n):
		self.emit('for (')
		self.gen(n['var'])
		self.emit(' of ')
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
