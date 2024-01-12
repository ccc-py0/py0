
import * as sys0 from "sys0/sys0.js"
var e2c = {'a':'一隻','dog':'狗','chase':'追','cat':'貓'}
print('e2c=' , e2c)
function mt(s) {
	var r = []
	var words = sys0.split(s , ' ')
	for (var e of words) {
		var c = e2c[e]
		sys0.push(r , c)
	}

	return sys0.join(r , ' ')
}

print('mt(a dog chase a cat)=' , mt('a dog chase a cat'))