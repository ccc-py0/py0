#include "sys0.h"

const char* const spaces = " \t\n\r\f\v";

std::string join(const std::vector<std::string>& vec, const char* const separator) {
    std::ostringstream oss;
    std::copy(vec.begin(), vec.end(), std::ostream_iterator<std::string>(oss, separator));
    std::string s = trim(oss.str());  // 注意這裡將 trim 的結果賦值給一個新的字符串
    return "[" + s + "]";
}

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

void print()
{
    cout << endl;
}


/*
template <typename T, typename... Types>
void print(T var1, Types... var2)
{
    cout << var1 << ' ';
    print(var2...);
}
*/