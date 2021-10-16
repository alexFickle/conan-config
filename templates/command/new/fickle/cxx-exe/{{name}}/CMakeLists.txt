cmake_minimum_required(VERSION 3.10)

project({{name}} CXX)

include(${CMAKE_CURRENT_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

add_library({{name}}-lib
    src/example.cpp
)
target_link_libraries({{name}}-lib PUBLIC ${CONAN_LIBS})

add_executable({{name}} src/main.cpp)
target_link_libraries({{name}} PUBLIC {{name}}-lib ${CONAN_LIBS})

# conditionally build unit tests
include(CTest)
if(BUILD_TESTING)
    add_subdirectory(test)
endif()

# conditionally enable code coverage
option(LCOV_ENABLED "enables code coverage with lcov" OFF)
if(LCOV_ENABLED)
    include(lcov)
    # including every local file except ones from the test directory
    lcov_enable(INCLUDE ** EXCLUDE test/**)
endif()

# support cmake --install
install(TARGETS {{name}}
    DESTINATION "."
    RUNTIME DESTINATION bin
    ARCHIVE DESTINATION lib
    LIBRARY DESTINATION lib
)
