
* https://stackoverflow.com/questions/1657883/variable-number-of-arguments-in-c

## c++ 23 有支援 print

In C++23 you'll be able to use std::print to print most standard types including std::vector. For example:

```
import std;

int main() {
  auto v = std::vector{1, 2, 3};
  std::print("{}", v);
}
```