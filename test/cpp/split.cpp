// https://stackoverflow.com/questions/14265581/parse-split-a-string-in-c-using-string-delimiter-standard-c
#include <iostream>
#include <sstream>
#include <vector>

using namespace std;

// for string delimiter
std::vector<std::string> split(std::string s, std::string delimiter) {
    size_t pos_start = 0, pos_end, delim_len = delimiter.length();
    std::string token;
    std::vector<std::string> res;

    while ((pos_end = s.find(delimiter, pos_start)) != std::string::npos) {
        token = s.substr (pos_start, pos_end - pos_start);
        pos_start = pos_end + delim_len;
        res.push_back (token);
    }

    res.push_back (s.substr (pos_start));
    return res;
}

int main() {
    std::string str = "adsf-+qwret-+nvfkbdsj-+orthdfjgh-+dfjrleih";
    std::string delimiter = "-+";
    std::vector<std::string> v = split (str, delimiter);

    for (auto i : v) cout << i << endl;

    return 0;
}