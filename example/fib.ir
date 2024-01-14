  func fib
  param n
  == n 0 T0
  == n 1 T1
  or T0 T1 T2
  jne T2 L0
  ret 1
L0:
  - n 1 T3
  arg T3
  call fib T4
  - n 2 T5
  arg T5
  call fib T6
  + T4 T6 T7
  ret T7
  fend