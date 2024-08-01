cmake_minimum_required(VERSION 3.10)

# 프로젝트 이름과 버전 설정
project(Solution VERSION 1.0)

# C++ 표준 설정
set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED True)

# 소스 파일 추가
add_executable(solution src/solution.cpp)

# Google Test 설정
enable_testing()
find_package(GTest REQUIRED)
include_directories(${GTEST_INCLUDE_DIRS})

# 테스트 파일 추가
add_executable(test_solution tests/test_solution.cpp)
target_link_libraries(test_solution ${GTEST_LIBRARIES} pthread)
add_test(NAME test_solution COMMAND test_solution)
