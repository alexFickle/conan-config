cmake_minimum_required(VERSION 3.10)

include(GoogleTest)

add_executable(test_{{name}}
    src/example.cpp
)
target_link_libraries(test_{{name}} PRIVATE
    {{name}}-lib
    ${CONAN_LIBS}
)
target_include_directories(test_{{name}} PRIVATE ../src)
gtest_discover_tests(test_{{name}})
