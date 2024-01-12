function fib
param n
T1 = n == 0
T2 = n == 1
T3 = T1 or T2
if_not T3 goto L1
return 1
(L1)
T4 = n - 1
push T4
T5 = call fib
T6 = n - 2
push T6
T7 = call fib
T8 = T5 + T7
return T8
fend