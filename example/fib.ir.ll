define dso_local i32 fib(i32 n) #0 {
 T0 = icmp eq n 0
 T1 = icmp eq n 1
 T2 = or T0 T1
 br i1 ??, label T2
 ret i32 1
0:
 T3 = sub n 1
 call i32 @fib(T3)
 T5 = sub n 2
 call i32 @fib(T5)
 T7 = add T4 T6
 ret i32 T7
}
 call i32 @fib(5)
 call i32 @print('fib(5)=',T8)