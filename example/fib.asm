function fib
param n
== n 0 T1
== n 1 T2
or T1 T2 T3
jne T3 L1
ret 1
(L1)
- n 1 T4
arg T4
call fib T5
- n 2 T6
arg T6
call fib T7
+ T5 T7 T8
ret T8
fend