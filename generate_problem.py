import openai
import os
import subprocess

def generate_problem(prompt):
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        raise ValueError("API key is missing or invalid")
    openai.api_key = api_key
    
    response = openai.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    
    return response.choices[0].message.content.strip()

def update_files(problem_text):
    parts = problem_text.split('---')
    print(parts)
    if len(parts) < 4:
        print("생성된 텍스트:", problem_text)
        raise ValueError("생성된 문제 텍스트 형식이 올바르지 않습니다.")
    
    problem_description, problem_code, solution_code, test_case_code = parts[:4]

    with open('README.md', 'w') as readme_file:
        readme_file.write(f"# 과제 설명\n\n## 문제 설명\n{problem_description.strip()}\n\n## 제출 방법\n1. `src/solution.cpp` 파일을 수정하여 문제를 해결하세요.\n2. `tests/test_solution.cpp` 파일을 통해 테스트를 확인하세요.\n3. 완료되면, 변경 사항을 커밋하고 푸시하세요.\n")

    with open('src/solution.cpp', 'w') as solution_file:
        solution_file.write(problem_code.strip())

    with open('tests/test_solution.cpp', 'w') as test_file:
        test_file.write(test_case_code.strip())

def compile_and_run_cpp(file_path):
    # Compile the C++ code
    compile_command = f"g++ {file_path} -o test_program"
    compile_process = subprocess.run(compile_command, shell=True, capture_output=True, text=True)

    if compile_process.returncode != 0:
        print("컴파일 오류:", compile_process.stderr)
        return

    # Run the compiled program
    run_process = subprocess.run("./test_program", shell=True, capture_output=True, text=True)
    
    if run_process.returncode != 0:
        print("프로그램 실행 오류:", run_process.stderr)
        return False
    else:
        print("프로그램 실행 결과:", run_process.stdout)
        return "All test cases passed!" in run_process.stdout

prompt = """
C++ 프로그래밍 문제를 생성하세요. 난이도는 다음과 같습니다. 아래 문제와 비슷한 난이도로 만들어주세요:
용모는 오늘 객체지향프로그래밍1 시간에 포인터에 대해 배웠다. 포인터란, 프로그래밍 언어에서 다른 변수, 혹은 그 변수의 메모리 공간주소를 가리키는 변수를 의미한다.

C/C++에서 포인터는 (자료형) *(변수명)으로 선언할 수 있으며 값은 &(이미 선언된 변수명)으로 지정할 수 있다. 이때 변수 선언에서 '*' 기호는 이 변수가 포인터임을 의미하고, '&' 기호는 변수의 메모리 주소값을 의미한다.

예를 들어, int형 변수 a에 대한 포인터 ptr을 다음과 같이 선언할 수 있다. 이때 ptr은 a가 저장된 메모리의 주소를 가리키고 있다.

int a;
int *ptr = &a;
또한 포인터의 포인터를 선언하는 식으로 다중 포인터를 선언하는 것이 가능하다. int형 변수 a에 대해 4중 포인터를 만들려 하는 경우 다음과 같이 코드를 작성해야 한다. 이중 포인터인 ptr2는 a의 포인터인 ptr의 주소를, 삼중 포인터인 ptr3는 이중 포인터인 ptr2의 주소를 가리키는 식으로 특정 변수에 대해 다중 포인터를 끝없이 선언할 수 있다.

int a;
int *ptr = &a;
int **ptr2 = &ptr;
int ***ptr3 = &ptr2;
int ****ptr4 = &ptr3;
용모는 int형 변수 a에 대해 N중 포인터를 선언하는 코드를 작성할 때 필요한 변수 선언문들을 작성해야 하는 과제를 받았다. 이때 위 다중 포인터 선언 예시와 같이 각 포인터 변수의 이름은 "ptr", "ptr2", ..., "ptrN" (N은 수)이 되어야 하고, 코드 형식은 위 예시와 동일해야 한다.

하지만 공부가 너무 싫고 게임을 너무나 좋아했던 용모는 코드를 치는 시간이 아까웠기 때문에 과제의 코드를 대신 출력해주는 프로그램을 작성하고 게임을 하러 가기로 하였다.

용모가 작성할 프로그램을 여러분도 작성해보자.

아래는 형식을 보여주는 예시 코드입니다. 위의 문제 난이도로 아래 형식을 지키면서 아래 문제가 아닌 새로운 문제를 생성해주세요. 그리고 ---로 각각의 번호를 구분할겁니다. 각 번호가 끝날 때마다 ---을 넣어주세요.:
1. 자연어 문제 설명
알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 단, 대문자와 소문자를 구분하지 않는다. 

---

2. 문제 코드
아래는 프로그램의 대략적인 구조를 보여주는 기본 코드입니다.
```cpp
#include <iostream>
#include <string>
#include <map>
using namespace std;

char mostFrequentChar(const string& str) {
    // 여기에 코드를 작성하세요.
}

int main() {
    string input;
    cout << "Enter a word: ";
    cin >> input;
    cout << "The most frequent character is: " << mostFrequentChar(input) << endl;
    return 0;
}
```

---

3. 정답 코드
아래는 정답 코드입니다.
```cpp
#include <iostream>
#include <string>
#include <map>
#include <cctype>
using namespace std;

char mostFrequentChar(const string& str) {
    map<char, int> frequency;
    for (char c : str) {
        c = tolower(c); // 대소문자 구분을 없애기 위해 소문자로 변환
        frequency[c]++;
    }

    char mostFrequent = ' ';
    int maxCount = 0;
    for (const auto& pair : frequency) {
        if (pair.second > maxCount) {
            mostFrequent = pair.first;
            maxCount = pair.second;
        }
    }

    return mostFrequent;
}

int main() {
    string input;
    cout << "Enter a word: ";
    cin >> input;
    cout << "The most frequent character is: " << mostFrequentChar(input) << endl;
    return 0;
}

```

---

4. 테스트 케이스
#include <iostream>
#include <cassert>
#include <string>
using namespace std;

char mostFrequentChar(const string& str);

void test_mostFrequentChar() {
    assert(mostFrequentChar("hello") == 'l');
    assert(mostFrequentChar("Hello") == 'l'); // 대소문자 구분 안 함
    assert(mostFrequentChar("HELLO") == 'l'); // 대소문자 구분 안 함
    assert(mostFrequentChar("test") == 't');
    assert(mostFrequentChar("TeSt") == 't');
    assert(mostFrequentChar("abcde") == 'a'); // 모든 문자가 동일한 빈도일 때 첫 문자 반환
    cout << "All test cases passed!" << endl;
}

int main() {
    test_mostFrequentChar();
    return 0;
}


"""  # 닫는 삼중 따옴표
problem = generate_problem(prompt)
update_files(problem)

# Test the generated solution
if compile_and_run_cpp('tests/test_solution.cpp'):
    print("모든 테스트 케이스가 성공적으로 통과되었습니다!")
else:
    print("테스트 케이스가 실패했습니다.")
