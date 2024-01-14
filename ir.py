from lib0 import *
import json

class IR:
	def __init__(self, mode='irasm'):
		self.emits = []
		self.labelMap = {}
		self.labelId = 0
		self.tempId = 0
		self.mode = mode

	def emit(self, code):
		i = len(self.emits)
		debug(f'{i}:{code}')
		self.emits.append(code)
		return i

	def codeIdx(self):
		return len(self.emits)
	
	def newTemp(self):
		t = self.tempId
		self.tempId += 1
		return f'T{t}'

	def newLabel(self):
		label = f'L{self.labelId}'
		self.labelMap[label] = -1
		self.labelId += 1
		return label

	def label(self, lab):
		self.labelMap[lab] = self.codeIdx()
		self.emit(['label', lab])

	def include(self, lib):
		self.emit(['include', lib])

	def jne(self, id, label):
		self.emit(['jne', id, label])

	def jeq(self, id, label):
		self.emit(['jeq', id, label])

	def op2(self, op, id1, id2, id):
		self.emit([op, id1, id2, id])

	def ret(self, id):
		self.emit(['ret', id])

	def assign(self, v, e):
		self.emit(['assign', v, e])

	def func(self, id):
		self.emit(['func', id])

	def param(self, id):
		self.emit(['param', id])

	def fend(self):
		self.emit(['fend'])

	def arg(self, id):
		self.emit(['arg', id])

	def index(self, o, idx, r):
		self.emit(['index', o, idx, r])

	def member(self, o, key, r):
		self.emit(['member', o, key, r])

	def call(self, f, r):
		self.emit(['call', f, r])
	
	def toCode(self):
		# return json.dumps({'code':self.emits, 'labels':self.labels})
		if self.mode == 'irasm':
			return self.toAsm()
		else:
			return self.toObj()

	def toAsm(self):
		lines = []
		for i, ir in enumerate(self.emits):
			lines.append(irToAsm(ir))
		return '\n'.join(lines)

	def toObj(self):
		lines = []
		for i, code in enumerate(self.emits):
			lines.append(f'{i}:{json.dumps(code)}')
		return '\n'.join(lines)+'\nlabels='+json.dumps(self.labelMap)

def irToAsm(a):
	if a[0] == 'label':
		return f'{a[1]}:'
	else:
		r = [str(t) for t in a]
		return f'  {" ".join(r)}'