#include "sys0.h"

int main() {
    std::string str = "hello world !";
    std::string delimiter = " ";
    std::vector<std::string> v = split (str, delimiter);

    for (auto i : v) cout << i << endl;
    print("pi=", 3.14159, "e=", 2.71828);
    print(3.14159);

    std::map<std::string, std::string> e2cMap = {
        {"a", "一隻"},
        {"the", "這隻"},
        {"dog", "狗"},
        {"cat", "貓"},
        {"chase", "追"},
        {"eat", "吃"}
    };

    std::vector<std::string> eWords = split("a dog chase a cat", " ");
    std::vector<std::string> cWords;
    for (auto e: eWords) {
        auto c = e2cMap[e];
        cWords.push_back(c);
    }
    print(join(cWords, " "));
    return 0;
}