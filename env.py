import json

class Env:
	def __init__(self, name, parent, returnClass=None):
		self.vars = {}
		self.name = name
		self.parent = parent
		self.returnClass = returnClass

	def add(self, name, type):
		self.vars[name] = type

	def find(self, name):
		env = self.findEnv(name)
		if env:
			return env.vars[name]
		else:
			return None

	def findClass(self, name):
		v = self.find(name)
		return v['class'] if v else None

	def findEnv(self, name):
		if name in self.vars:
			return self
		elif self.parent:
			return self.parent.findEnv(name)
		else:
			return None
		
	def __repr__(self):
		return f'env:name={self.name} parent={self.parent.name} returnClass={self.returnClass}\nvars={json.dumps(self.vars)}'

