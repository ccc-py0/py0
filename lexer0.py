from typing import NamedTuple
import re
from lib0 import error, debug

class Token(NamedTuple):
	type: str
	value: str
	line: int
	column: int
	level: int

lines = None

def tokenize(code):
	lines = code.split('\n')
	lines = ['']+lines
	"""
	keywords = {
		'def', 'if', 'while', 'for', 'return', 'and', 'or', 'not', 
	    'as', 'assert', 'class', 'del', 'except', 'finally', 'from', 'global', 
	    'yield', 'raise', 'continue', 'break', 'import', 'in', 'is', 'lambda', 
		'nonlocal', 'local', 'pass', 'try', 'with', 
	    'False', 'True', 'None', 
		}
	"""
	token_specification = [
		('str',   r'(".*?")|(\'.*?\')'),        # String
		('float',    r'\d+\.\d*'),     # Float
		('int',  r'\d+'),          # Integer
		('id',       r'[A-Za-z_]\w*'), # Identifiers
		('op2',      r'(==)|(!=)|(<=)|(>=)'),    # Arithmetic operators
		('indent',   r'\n\t*'),        # Line indent
		('space',    r'[ \t]+'),       # Skip over spaces and tabs
		('char',     r'[{}()\[\]\+\-\*/=!:<>,&|^~.]'), # 
		('mismatch', r'.'),            # Any other character
	]
	tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_specification)
	line_num = 1
	line_start = 0
	level = 0
	line_level = 0
	for mo in re.finditer(tok_regex, code):
		kind = mo.lastgroup
		value = mo.group()
		column = mo.start() - line_start
		if kind == 'mismatch':
			error(f'{value} unexpected on line {line_num}')
		elif kind == 'indent':
			line_num += 1
			line_level = len(value)-1
			if line_level == level+1:
				level += 1
				kind = 'begin'
				# print(kind, level)
			elif line_level == level-1:
				kind = 'end'
				# print(kind, level)
				level -= 1
			else:
				kind = 'indent'
				continue
				
			line_start = mo.start() + 1 # mo.end()
		else:
			if kind == 'space':
				continue
			if line_level != level:
				error(f'line {line_num}, level misatch ...\n{line_num-1}:{lines[line_num-1]}\n{line_num}:{lines[line_num]}')
			debug('tk:', value)
			# if kind == 'id' and value in keywords:
			#	kind = value
		tk = Token(kind, value, line_num, column, level)
		yield tk

def lex(code):
	code = code.replace('    ', '\t')
	tokens = []
	for tk in tokenize(code):
		tokens.append(tk)
	return tokens

def lexDump(tokens):
	for i,t in enumerate(tokens):
		print(f'{i}:{t.value}')

"""
def format(code):
	words = []
	for tk in tokenize(code):
		tabs = '\t'*tk.level
		if tk.type == 'BEGIN':
			words.append('\n'+tabs+'\t')# words.append('\n'+tabs+'begin\n'+tabs+'\t') # 多一個 \t ，因為 begin 後內縮一層
		elif tk.type == 'END':
			words.append('\n'+tabs+'\n'+tabs) # words.append('\n'+tabs+'end\n'+tabs)
		elif tk.type == 'NEWLINE':
			words.append('\n'+tabs)
		else:
			words.append(tk.value+' ')
	return ''.join(words)
"""

# 測試詞彙掃描器
if __name__ == "__main__":
	from test0 import code
	tokens = lex(code)
	for t in tokens:
		if t.type in ['begin', 'end']:
			print(t.type)
		else:
			print(t.value, end=' ')
	# fcode = format(code)
	# print(fcode)
