import math

cdef public int complex_and_slow_calc_c(int x, int a, int b):
  return round(math.sqrt(a * x + b))