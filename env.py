class Env:
	def __init__(self, parent):
		self.vars = {}
		self.parent = parent

	def add(self, name, type):
		self.vars[name] = type

	def findClass(self, name):
		env = self.findEnv(name)
		if env:
			return env.vars[name]
		else:
			return None

	def findEnv(self, name):
		if name in self.vars:
			return self
		elif self.parent:
			return self.parent.findEnv(name)
		else:
			return None

