class Vm:
	def __init__(self):
		self.emits = []
		self.labelId = 0
		self.tempId = 0

	def emit(self, code):
		codeIdx = len(self.emits)
		print(f'{codeIdx}:{code}')
		self.emits.append(code)
		return codeIdx

	def emitCode(self):
		return self.emits

	def newLabel(self):
		self.labelId += 1

	def newTemp(self):
		self.tempId += 1

	def include(self, lib):
		pass

	def jne(self, id, label):
		pass

	def jeq(self, id, label):
		pass

	def op2(self, op, id1, id2, id):
		pass

	def label(self, id):
		pass

	def ret(self, id):
		pass

	def assign(self, v, e):
		pass

	def func(self, id):
		pass

	def param(self, id):
		pass

	def fend(self):
		pass

	def arg(self, id):
		pass

	def index(self, o, idx, r):
		pass

	def member(self, o, key, r):
		pass

	def call(self, f, r):
		pass
	