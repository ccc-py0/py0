#ifndef __SYS0_H__
#define __SYS0_H__

#include <iostream>
#include <sstream>
#include <vector>
#include <map>
#include <any>
#include <iterator>

using namespace std;

namespace sys0 
{
    extern const char* const spaces;

    inline string trim(string s, const char* t = spaces) {
        s.erase(0, s.find_first_not_of(t));
        s.erase(s.find_last_not_of(t) + 1);
        return s;
    }

    string join(const vector<string>& vec, const char* const separator);
    vector<string> split(string s, string delimiter);

    extern void print();

    template <typename T, typename... Types>
    void print(T var1, Types... var2)
    {
        cout << var1 << ' ';
        print(var2...);
    }

    template <typename T>
    void push(vector<T> &a, T o) {
        a.push_back(o);
    }

}
#endif
