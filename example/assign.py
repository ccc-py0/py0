import sys
sys.path.append("sys0")

a:int = 5
b:int = a + 3
c:bool = a == 5
d:bool = a == 5 or b == 8
msg:str = 'a<=5'
if a <= 5:
	print(msg)
