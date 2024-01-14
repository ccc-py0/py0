# py0 -- EBNF

```
STMTS  = STMT*                                            # list
STMT   = BLOCK | FUNC | IF | WHILE | RETURN | ASSIGN | CALL | IMPORT
IMPORT = import id
IF     = if EXPR: STMT (elif STMT)* (else STMT)?
WHILE  = while EXPR: STMT
FOR    = for VAR in EXPR: STMT
RETURN = return EXPR
ASSIGN = VAR = EXPR
CALL   = id(ARGS)
FUNC   = def id(PARAMS): BLOCK
PARAMS = PARAM*                                           # list
PARAM  = id
BLOCK  = begin STMTS end
EXPR   = BEXPR (if EXPR else EXPR)?
BEXPR  = CEXPR ((and|or) CEXPR)*                           # list
CEXPR  = MEXPR (['==', '!=', '<=', '>=', '<', '>'] MEXPR)* # list
MEXPR  = ITEM (['+', '-', '*', '/', '%'] ITEM)*            # list
ITEM   = LIST | DICT | FACTOR
FACTOR = (!-~)* TERM
TERM   = OBJ ( [EXPR] | . id | (ARGS) )*
OBJ    = id | string | int | float | LREXPR
LREXPR = ( EXPR )
CALL   = id(ARGS)
ARGS   = (EXPR ,)* EXPR?
ARRAY  = [ (EXPR ,)* EXPR? ]
DICT   = { (PAIR ,)* PAIR? }
PAIR   = string : EXPR
VAR    = id
```