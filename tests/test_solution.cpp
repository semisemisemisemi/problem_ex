4. 테스트 케이스
```cpp
#include <iostream>
#include <cassert>
#include <string>
using namespace std;

int countSubstring(const string& book, const string& target);

void test_countSubstring() {
    assert(countSubstring("Hello World, Hello!", "hello") == 2);
    assert(countSubstring("Lorem Ipsum", "ipsum") == 1);
    assert(countSubstring("Lorem Ipsum", "Lorem") == 1);
    assert(countSubstring("LoremLorem Lorem", "lorem") == 3);
    assert(countSubstring("A quick brown fox jumps over the lazy dog.", "fox") == 1);
    cout << "All test cases passed!" << endl;
}

int main() {
    test_countSubstring();
    return 0;
}
```