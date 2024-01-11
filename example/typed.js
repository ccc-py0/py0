
import * as sys0 from "sys0/sys0.js"
var a = 1
var b = 2
var c = a + b
print('c=' , c)
function sum(n) {
	var s = 0
	for (var i of range(1 , n + 1)) {
		s = s + i
	}

	return s
}

print('sum(10)=' , sum(10))
var e2c = {'a':'一隻','dog':'狗','chase':'追','cat':'貓'}
print('e2c=' , e2c)
function mt(s) {
	var r = []
	var words = s.split(' ')
	for (var e of words) {
		c = e2c[e]
		sys0.push(r , c)
	}

	return sys0.join(r , ' ')
}

print('mt(a dog chase a cat)=' , mt('a dog chase a cat'))