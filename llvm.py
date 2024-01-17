import json
from lib0 import *

bopMap = {
	'+': 'add',
	'-': 'sub',
	'*': 'mul',
	'/': 'div',
	'%': 'mod', # ??
	'==': 'icmp eq',
	'!=': 'icmp ne',
	'<': 'icmp lt',
	'>': 'icmp gt',
	'<=': 'icmp le',
	'>=': 'icmp ge',
	'and': 'and',
	'or': 'or'
}

def ir2llvm(ir):
	print('ir2llvm()')
	lines = []
	ei = 0
	eLen = len(ir.emits)
	args = []
	while ei < eLen:
		e = ir.emits[ei]
		e.extend(['']*4)
		op, a1, a2, a3 = e[0:4]
		r = None
		match op:
			case 'func':
				fname = a1
				params = []
				while ei < eLen-1:
					e = ir.emits[ei+1]
					print('e=', e)
					e.extend(['i32']*4)
					opx, a1, a2 = e[0:3]
					if opx != 'param':
						break
					params.append(f'{a2} {a1}')
					ei += 1
				r = f'define dso_local i32 {fname}({",".join(params)}) #0 '+'{'
				print('r=', r)
			case 'fend':
				r = '}'
			case 'label':
				r = f'{a1[1:]}:'
			case 'jeq':
				r = f' br i1 ??, label %{a1[1:]}' # ???
			case 'jne':
				r = f' br i1 ??, label {a1}' # ???
			case 'ret':
				r = f' ret i32 {a1}'
			case 'assign':
				r = f' store i32 {a1} {a2}'
			case 'arg':
				args.append(a1)
			case 'call':
				fname = a1
				nargs = int(a2)
				fargs = args[-nargs:]
				r = f' call i32 @{fname}({",".join(fargs)})'
				args = args[0:-nargs]
			case 'index':
				error('index ???')
			case 'member':
				error('member ???')
			case _:
				if op in bopMap:
					llop = bopMap[op]
					r = f' {a3} = {llop} {a1} {a2}'
				else:
					error(f'{op} ???, ei={ei}')
		ei += 1
		if r: lines.append(r)
	return '\n'.join(lines)

#	return '\n'.join(lines)+'\nlabels='+json.dumps(ir.labelMap)

"""
; ModuleID = 'fib.c'
source_filename = "fib.c"
target datalayout = "e-m:w-p270:32:32-p271:32:32-p272:64:64-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-windows-msys"

; Function Attrs: noinline nounwind optnone uwtable
define dso_local i32 @fib(i32 %0) #0 {
  %2 = alloca i32, align 4
  %3 = alloca i32, align 4
  store i32 %0, i32* %3, align 4
  %4 = load i32, i32* %3, align 4
  %5 = icmp eq i32 %4, 0
  br i1 %5, label %9, label %6

6:                                                ; preds = %1
  %7 = load i32, i32* %3, align 4
  %8 = icmp eq i32 %7, 1
  br i1 %8, label %9, label %10

9:                                                ; preds = %6, %1
  store i32 1, i32* %2, align 4
  br label %18

10:                                               ; preds = %6
  %11 = load i32, i32* %3, align 4
  %12 = sub nsw i32 %11, 1
  %13 = call i32 @fib(i32 %12)
  %14 = load i32, i32* %3, align 4
  %15 = sub nsw i32 %14, 2
  %16 = call i32 @fib(i32 %15)
  %17 = add nsw i32 %13, %16
  store i32 %17, i32* %2, align 4
  br label %18

18:                                               ; preds = %10, %9
  %19 = load i32, i32* %2, align 4
  ret i32 %19
}

attributes #0 = { noinline nounwind optnone uwtable "correctly-rounded-divide-sqrt-fp-math"="false" "disable-tail-calls"="false" "frame-pointer"="none" "less-precise-fpmad"="false" "min-legal-vector-width"="0" "no-infs-fp-math"="false" "no-jump-tables"="false" "no-nans-fp-math"="false" "no-signed-zeros-fp-math"="false" "no-trapping-math"="true" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+cx8,+fxsr,+mmx,+sse,+sse2,+x87" "unsafe-fp-math"="false" "use-soft-float"="false" }

!llvm.module.flags = !{!0, !1}
!llvm.ident = !{!2}

!0 = !{i32 1, !"wchar_size", i32 2}
!1 = !{i32 7, !"PIC Level", i32 2}
!2 = !{!"clang version 11.0.0 (https://github.com/msys2/MSYS2-packages 9ef552a3c4cc9410d2b1fb6f22a0cdda3bc09a64)"}

"""
