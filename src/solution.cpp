2. 문제 코드
아래는 프로그램의 대략적인 구조를 보여주는 기본 코드입니다. 
```cpp
#include <iostream>
#include <string>
#include <cctype>
using namespace std;

int countSubstring(const string& book, const string& target) {
    // 여기에 코드를 작성하세요.
}

int main() {
    string book, target;
    cout << "Enter the book content: ";
    getline(cin, book);
    cout << "Enter the target substring: ";
    cin >> target;
    cout << "The frequency of target substring is: " << countSubstring(book, target) << endl;
    return 0;
}
```