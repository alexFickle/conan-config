cmake_minimum_required(VERSION 3.10)

project({{name}} CXX)

include(${CMAKE_CURRENT_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

add_library({{name}}
    src/example.cpp
)
target_include_directories({{name}} PUBLIC include)
target_link_libraries({{name}} PUBLIC ${CONAN_LIBS})

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
file(GLOB_RECURSE {{name}}_headers
    include *.hpp *.h
)
set_target_properties({{name}}
    PROPERTIES PUBLIC_HEADER
    "{%raw%}${{%endraw%}{{name}}_headers{%raw%}}{%endraw%}"
)
install(TARGETS {{name}}
    DESTINATION "."
    PUBLIC_HEADER DESTINATION include
    RUNTIME DESTINATION bin
    ARCHIVE DESTINATION lib
    LIBRARY DESTINATION lib
)
