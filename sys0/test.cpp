#include "sys0.h"

int main() {
    string str = "hello world !";
    vector v = sys0::split (str, " ");

    for (auto i : v) cout << i << endl;
    sys0::print("pi=", 3.14159, "e=", 2.71828);
    sys0::print(3.14159);

    map<string, string> e2cMap = { // 這邊的 <string, string> 也去不掉，會錯！
        {"a", "一隻"},
        {"the", "這隻"},
        {"dog", "狗"},
        {"cat", "貓"},
        {"chase", "追"},
        {"eat", "吃"}
    };

    vector eWords = sys0::split("a dog chase a cat", " ");
    vector<string> cWords; // 這邊的 <string> 去不掉，也不能用 any  ... 會錯
    for (auto e: eWords) {
        string c = e2cMap[e];
        sys0::push(cWords, c);
    }
    sys0::print(sys0::join(cWords, " "));
    return 0;
}