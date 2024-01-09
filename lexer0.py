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
	keywords = {'def', 'if', 'while', 'for', 'return', 'and', 'or', 'not', 'yield', 'raise', 'continue', 'break'}
	token_specification = [
		('STRING',   r'(".*?")|(\'.*?\')'),        # String
		('FLOAT',    r'\d+\.\d*'),     # Float
		('INTEGER',  r'\d+'),          # Integer
		('ID',       r'[A-Za-z_]\w*'), # Identifiers
		('OP2',      r'(==)|(!=)|(<=)|(>=)'),    # Arithmetic operators
		('INDENT',   r'\n\t*'),        # Line indent
		('SPACE',    r'[ \t]+'),       # Skip over spaces and tabs
		('CHAR',     r'[{}()\[\]\+\-\*/=!:<>,&|^~.]'), # 
		('MISMATCH', r'.'),            # Any other character
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
		if kind == 'MISMATCH':
			error(f'{value} unexpected on line {line_num}')
		elif kind == 'INDENT':
			line_num += 1
			line_level = len(value)-1
			if line_level == level+1:
				level += 1
				kind = 'BEGIN'
				# print(kind, level)
			elif line_level == level-1:
				kind = 'END'
				# print(kind, level)
				level -= 1
			else:
				kind = 'INDENT'
				continue
				
			line_start = mo.start() + 1 # mo.end()
		else:
			if kind == 'SPACE':
				continue
			if line_level != level:
				error(f'line {line_num}, level misatch ...\n{line_num-1}:{lines[line_num-1]}\n{line_num}:{lines[line_num]}')
			debug('tk:', value)
			if kind == 'ID' and value in keywords:
				kind = value
		tk = Token(kind, value, line_num, column, level)
		yield tk

def lex(code):
	tokens = []
	for tk in tokenize(code):
		tokens.append(tk)
	return tokens

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
		if t.type in ['BEGIN', 'END']:
			print(t.type)
		else:
			print(t.value, end=' ')
	# fcode = format(code)
	# print(fcode)
