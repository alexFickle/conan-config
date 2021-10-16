cmake_minimum_required(VERSION 3.10)

include(GoogleTest)

add_executable(test_{{name}}
    src/example.cpp
)
target_link_libraries(test_{{name}} PRIVATE
    {{name}}
    ${CONAN_LIBS}
)
gtest_discover_tests(test_{{name}})
