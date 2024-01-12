
#include <sys0.h>
map e2c = {'a':"一隻",'dog':"狗",'chase':"追",'cat':"貓"};
print("e2c=" , e2c);
string mt(string s) {
	vector r = {};
	words = sys0.split(s , " ");
	for (auto e : words) {
		string c = e2c[e];
		sys0.push(r , c);
	}

	return sys0.join(r , " ");
}

print("mt(a dog chase a cat)=" , mt("a dog chase a cat"));