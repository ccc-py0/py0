isDebugOn = False

def debug(*msg):
	if isDebugOn: print(*msg)

def emit(msg):
	print(msg, end='')

def error(msg):
	print(msg)
	raise Exception('parse error')

def readTextFile(fname):
	with open(fname, 'r', encoding='utf-8') as file:
		text = file.read()
	return text

def writeTextFile(fname, text):
	with open(fname, 'w', encoding='utf-8') as file:
		file.write(text)
