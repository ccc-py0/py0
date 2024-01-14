import operator as op

isa = isinstance
Symbol = str
Number = (int, float)

# 定義一些基本的運算符
ENV = {
    '+': op.add, '-': op.sub, '*': op.mul, '/': op.truediv,
    '>':op.gt, '<':op.lt, '>=':op.ge, '<=':op.le, '=':op.eq, 
    'abs': abs,
    'append':  op.add,  
    'apply':   lambda f, args: f(*args),
    'begin':   lambda *x: x[-1],
    'car':     lambda x: x[0],
    'cdr':     lambda x: x[1:], 
    'cons':    lambda x,y: [x] + y,
    'eq?':     op.is_, 
    'equal?':  op.eq, 
    'length':  len, 
    'list':    lambda *x: list(x), 
    'list?':   lambda x: isinstance(x,list), 
    'map':     map,
    'max':     max,
    'min':     min,
    'not':     op.not_,
    'null?':   lambda x: x == [], 
    'number?': lambda x: isinstance(x, Number),   
    'procedure?': callable,
    'round':   round,
    'symbol?': lambda x: isinstance(x, Symbol),
}

def print2(*args):
    print(*args)

print3 = lambda *args: print(*args)
exec("""
def fname(*args):
    print(*args)
""")

print4 = fname

print2('print2', 5)
print3('print3', 5)
print4('print4', 5)