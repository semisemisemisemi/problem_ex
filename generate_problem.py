import openai
import os

def generate_problem(prompt):
    openai.api_key = os.getenv('OPENAI_API_KEY')
    
    response = openai.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    
    return response.choices[0].message['content'].strip()

def update_files(problem_text):
    parts = problem_text.split('---')
    if len(parts) < 4:
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
1. 자연어 문제 설명
2. 문제 코드
3. 정답 코드
4. 테스트 케이스
---

"""
problem = generate_problem(prompt)
update_files(problem)
