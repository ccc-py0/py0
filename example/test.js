
import * as sys0 from "sys0/sys0.js"
function fib(n) {
	if (n == 0 || n == 1) {
		return 1
	}

	return fib(n - 1) + fib(n - 2)
}

function sum(n) {
	var s = 0
	var i = 1
	while (i <= n) {
		s = s + i
		i = i + 1
	}

	return s
}

var e2c = {'a':'一隻','dog':'狗','chase':'追','cat':'貓'}
print('e2c=' , e2c)
function mt(s) {
	var r = []
	var words = s.split(' ')
	for (var e of words) {
		var c = e2c[e]
		sys0.push(r , c)
	}

	return sys0.join(r , ' ')
}

print("fib(5)=" , fib(5))
print('sum(10)=' , sum(10))
print('mt(a dog chase a cat)=' , mt('a dog chase a cat'))
var a = [1,2,3]
print('a=' , a)