cmake_minimum_required(VERSION 3.10)

include(${CMAKE_CURRENT_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

add_executable({{name}} {{name}}.cpp)
target_link_libraries({{name}} PRIVATE ${CONAN_LIBS})

include(CTest)
include(GoogleTest)
gtest_discover_tests({{name}})

# conditionally enable code coverage
option(LCOV_ENABLED "enables code coverage with lcov" OFF)
if(LCOV_ENABLED)
    include(lcov)
    lcov_enable(INCLUDE {{name}}.cpp)
endif()
