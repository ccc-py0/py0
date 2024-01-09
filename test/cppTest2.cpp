#include <iostream>
#include <map>
#include <string>
#include <string_view>
 
void print_map(std::string_view comment, const std::map<std::string, int>& m)
{
    std::cout << comment;
    // Iterate using C++17 facilities
    for (const auto& [key, value] : m)
        std::cout << '[' << key << "] = " << value << "; ";
 
// C++11 alternative:
//  for (const auto& n : m)
//      std::cout << n.first << " = " << n.second << "; ";
//
// C++98 alternative:
//  for (std::map<std::string, int>::const_iterator it = m.begin(); it != m.end(); ++it)
//      std::cout << it->first << " = " << it->second << "; ";
 
    std::cout << '\n';
}
 
int main()
{
    // Create a map of three (string, int) pairs
    std::map<std::string, int> m{{"CPU", 10}, {"GPU", 15}, {"RAM", 20}};
 
    print_map("1) Initial map: ", m);
 
    m["CPU"] = 25; // update an existing value
    m["SSD"] = 30; // insert a new value
    print_map("2) Updated map: ", m);
 
    // Using operator[] with non-existent key always performs an insert
    std::cout << "3) m[UPS] = " << m["UPS"] << '\n';
    print_map("4) Updated map: ", m);
 
    m.erase("GPU");
    print_map("5) After erase: ", m);
  
    m.clear();
    std::cout << std::boolalpha << "8) Map is empty: " << m.empty() << '\n';
}