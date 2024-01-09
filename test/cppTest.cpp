#include <iostream>
#include <map>
#include <string>

using namespace std;

int main()
{
    map<string, string> e2c{{"a", "一"}, {"dog", "狗"}};

    cout << e2c["a"] << e2c["dog"] << endl;
}
