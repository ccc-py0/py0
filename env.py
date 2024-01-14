import json

class Env:
	def __init__(self, name, parent, returnClass=None):
		self.vars = {}
		self.name = name
		self.parent = parent
		self.returnClass = returnClass
		self.returnValue = None
		self.returned = False

	def add(self, name, obj):
		self.vars[name] = obj

	def findEnv(self, name):
		if name in self.vars:
			return self
		elif self.parent:
			# print('self=', self)
			# print('self.parent=', self.parent)
			return self.parent.findEnv(name)
		else:
			return None

	def find(self, name):
		env = self.findEnv(name)
		if env:
			return env.vars[name]
		else:
			return None

	def findClass(self, name):
		v = self.find(name)
		return v['class'] if v else None

	def __repr__(self):
		parent = self.parent.name if self.parent else None
		varsJson = json.dumps(self.vars, default=lambda o: f"<<non-serializable: {type(o).__qualname__}>>")
		return f'env:name={self.name} parent={parent} returnClass={self.returnClass}\nvars={varsJson}'

