from lib0 import *
from parser0 import parse
from genx import GenX

class GenJs(GenX):
	def IMPORT(self, n):
		id = n['id']
		self.emit(f'import * as {id} from "{id}/{id}.js"')

	def VAR(self, n, isNew):
		if isNew: self.emit('var ')
		super().VAR(n, isNew)

	def FOR(self, n):
		self.emit('for (')
		self.gen(n['var'])
		self.emit(' of ')
		self.gen(n['expr'])
		self.emit(')')
		self.gen(n['stmt'])

	def BEXPR(self, n):
		jsOp = {'and':'&&', 'or':'||'}
		for e in n['list']:
			if isinstance(e, str): # op
				self.emit(f' {jsOp[e]} ')
			else:
				self.gen(e)
