import openai
import os

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

prompt = """
다음을 포함한 C++ 프로그래밍 문제를 생성하세요:
1. 자연어 문제 설명(끝에 '---'로 구분)
 사용자로부터 정수 n을 입력 받아서 그 정수값의 팩토리얼을 구하는 프로그램을 작성하세요. 팩토리얼이란 자연수 n에 대해서 1부터 n까지의 모든 자연수를 곱하는 것을 합니다. 예를 들어, 5의 팩토리얼은 5 x 4 x 3 x 2 x 1 = 120입니다.
---
2. 문제 코드(끝에 '---'로 구분)
아래는 프로그램의 대략적인 구조를 보여주는 기본 코드입니다.
```cpp
#include <iostream>
using namespace std;
int factorial(int n) {
    // 여기에 코드를 구현하세요.
}
int main() {
    int n;
    cin >> n;
    cout << factorial(n) << endl;
    return 0;
}
```
---
3. 정답 코드(끝에 '---'로 구분)
아래는 정답 코드입니다.
```cpp
#include <iostream>
using namespace std;
int factorial(int n) {
    if (n == 0)
        return 1;
    else
        return n * factorial(n - 1);
}
int main() {
    int n;
    cin >> n;
    cout << factorial(n) << endl;
    return 0;
}
```
---
4. 테스트 케이스(끝에 '---'로 구분)
입력:
5
출력:
120
입력:
10
출력:
3628800
입력:
0
출력:
1
입력:
1
출력:
1
---
"""  # 닫는 삼중 따옴표
problem = generate_problem(prompt)
update_files(problem)
