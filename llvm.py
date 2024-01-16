import json

def ir2llvm(ir):
	print('ir2llvm()')
	lines = []
	for e in ir.emits:
		ll = toLlvm(e)
		lines.append(f'{ll}')
	return '\n'.join(lines)

def toLlvm(e):
	e.extend(['']*4)
	op, a1, a2, a3 = e[0:4]
	r = None
	match op:
		case 'func': r = f'define dso_local {a1}'
		case _: r = f'{op} {a1} {a2} {a3}'
	return r

#	return '\n'.join(lines)+'\nlabels='+json.dumps(ir.labelMap)


