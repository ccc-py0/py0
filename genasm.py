from vm import Vm
from genvm import GenVm

def toAsm(a):
	if a[0] == 'label':
		return f'{a[1]}:'
	else:
		r = [str(t) for t in a]
		return f'  {" ".join(r)}'

class GenAsm(GenVm):
	def __init__(self, typed):
		super().__init__(self, typed, vm=AsmVm())

class AsmVm(Vm):
	def __init__(self):
		super().__init__()

	def emitCode(self):
		lines = []
		for i, code in enumerate(self.emits):
			lines.append(toAsm(code))
		return '\n'.join(lines)
