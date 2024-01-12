#ifndef __SYS0_H__
#define __SYS0_H__

#include <iostream>
#include <sstream>
#include <vector>
#include <map>
#include <any>

using namespace std;

extern const char* const spaces;

inline std::string trim(std::string s, const char* t = spaces) {
    s.erase(0, s.find_first_not_of(t));
    s.erase(s.find_last_not_of(t) + 1);
    return s;
}

std::string join(const std::vector<std::string>& vec, const char* const separator);
std::vector<std::string> split(std::string s, std::string delimiter);

void print();

template <typename T, typename... Types>
void print(T var1, Types... var2)
{
    cout << var1 << ' ';
    print(var2...);
}

#endif
