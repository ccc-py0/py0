import json
from genvm import GenVm
from vm import Vm

class GenObj(GenVm):
	def __init__(self, typed):
		super().__init__(self, typed, vm=ObjVm())

class ObjVm(Vm):
	def __init__(self):
		super().__init__()
	
	def toCode(self):
		lines = []
		for i, code in enumerate(self.emits):
			lines.append(f'{i}:{json.dumps(code)}')
		return '\n'.join(lines)+'\nlabels='+json.dumps(self.labelMap)
