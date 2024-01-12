#include <iostream>
#include <sstream>
#include <vector>
#include <algorithm>

const char* const spaces = " \t\n\r\f\v";

inline std::string trim(std::string s, const char* t = spaces) {
    s.erase(0, s.find_first_not_of(t));
    s.erase(s.find_last_not_of(t) + 1);
    return s;
}

std::string join(const std::vector<std::string>& vec, const char* const separator) {
    std::ostringstream oss;
    std::copy(vec.begin(), vec.end(), std::ostream_iterator<std::string>(oss, separator));
    std::string s = trim(oss.str());  // 注意這裡將 trim 的結果賦值給一個新的字符串
    return "[" + s + "]";
}

int main() {
    std::vector<std::string> vec = {"apple", "orange", "banana"};
    std::string result = join(vec, ", ");
    std::cout << result << std::endl;
    return 0;
}
