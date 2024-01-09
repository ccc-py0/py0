#include <iostream>
#include <map>
#include <string>
#include <vector>
// #include <boost/algorithm/string/join.hpp>
#include <iterator>
using namespace std;

map<string, string> e2c{{"a", "一"}, {"dog", "狗"}};
/*
string mt(string s) {
    vector<string> r;
    int pos = 0;
    while(pos < s.size()){
        pos = s.find("%20");
        r.push_back(s.substr(0,pos));
        s.erase(0,pos+3); // 3 is the length of the delimiter, "%20"
    }
    return r;
}
*/
int main()
{
    cout << e2c["a"] << e2c["dog"] << endl;
    vector<string> words { "a", "dog" };
    cout << words[0] << endl;
/*
    ostringstream ostream;
    copy(words.begin(), words.end(), ostream_iterator<string>(ostream, ' '));
    // cout << ostream << endl;
*/
}
