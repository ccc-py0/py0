#include "sys0.h"

using namespace sys0;

const char* const sys0::spaces = " \t\n\r\f\v";

string sys0::join(const vector<string>& vec, const char* const separator) {
    ostringstream oss;
    copy(vec.begin(), vec.end(), ostream_iterator<string>(oss, separator));
    string s = trim(oss.str());  // 注意這裡將 trim 的結果賦值給一個新的字符串
    return "[" + s + "]";
}

// for string delimiter
vector<string> sys0::split(string s, string delimiter) {
    size_t pos_start = 0, pos_end, delim_len = delimiter.length();
    string token;
    vector<string> res;

    while ((pos_end = s.find(delimiter, pos_start)) != string::npos) {
        token = s.substr (pos_start, pos_end - pos_start);
        pos_start = pos_end + delim_len;
        res.push_back (token);
    }

    res.push_back(s.substr (pos_start));
    return res;
}

void sys0::print()
{
    cout << endl;
}
