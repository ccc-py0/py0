from vm import Vm
from genvm import GenVm

class GenAsm(GenVm):
	def __init__(self, typed):
		super().__init__(self, typed, vm=Asm())
	
	def emitCode(self):
		return self.vm.emitCode()

class Asm(Vm):
	def __init__(self):
		super().__init__()

	def emitCode(self):
		return '\n'.join(self.emits)

	def newLabel(self):
		self.labelId += 1
		return f'L{self.labelId}'

	def newTemp(self):
		self.tempId += 1
		# print(f'T{self.tempId}')
		return f'T{self.tempId}'

	def include(self, lib):
		self.emit(f'#include <{lib}')

	def jne(self, id, label):
		self.emit(f'jne {id} {label}')

	def jeq(self, id, label):
		self.emit(f'jeq {id} {label}')

	def op2(self, op, id1, id2, id):
		self.emit(f'{op} {id1} {id2} {id}')

	def label(self, id):
		self.emit(f'({id})')

	def ret(self, id):
		self.emit(f'ret {id}')

	def assign(self, v, e):
		self.emit(f'{v} = {e}')

	def func(self, id):
		self.emit(f'function {id}')

	def param(self, id):
		self.emit(f'param {id}')

	def fend(self):
		self.emit(f'fend')

	def arg(self, id):
		self.emit(f'arg {id}')

	def index(self, o, idx, r):
		self.emit(f'index {o} {idx} {r}')

	def member(self, o, key, r):
		self.emit(f'member {o} {key} {r}')

	def call(self, f, r):
		self.emit(f'call {f} {r}')


	