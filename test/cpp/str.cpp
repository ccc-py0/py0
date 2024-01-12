#include <iostream>
#include <sstream>
#include <vector>
#include <map>
#include <any>

using namespace std; 

const char* spaces = " \t\n\r\f\v";

// trim from end of string (right)
inline std::string &rtrim(std::string& s, const char* t = spaces)
{
    string r = s;
    r.erase(r.find_last_not_of(t) + 1);
    return r;
}

// trim from beginning of string (left)
inline std::string &ltrim(std::string& s, const char* t = spaces)
{
    string r = s;
    r.erase(0, r.find_first_not_of(t));
    return r;
}

// trim from both ends of string (right then left)
inline std::string &trim(std::string& s, const char* t = spaces)
{
    return ltrim(rtrim(s, t), t);
}

string join(vector<string> vec, const char* const seperator) {
    ostringstream oss;
    copy(vec.begin(), vec.end(), ostream_iterator<string>(oss, seperator));
    string s = trim(oss.str(), spaces)
    return "["+s+"]";
}

int main() 
{ 
    // Initializing vector with A..E characters 
    vector<string> vec = { "aaa", "bbb" }; 
    // string constructor used to convert the vector into string 
    string str = join(vec, " ");
  
    cout << str << endl; 
  
    return 0; 
}