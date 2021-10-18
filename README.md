Conan Configuration that can be installed with the
`conan config install` command.

**Do Not Use!**  This configuration is still in development and 
depends on not yet released conan packages.  During development
there will be breaking changes.  Additionally this configuration
is opinionated to my personal preferences.  Feel free to fork
or copy to customize.

# Conan New Templates

Conan can generate a project structure using `conan new`.
A template can be provided to this command to customize the
generated project structure.
These templates can be distributed in a conan configuration
by placing them at `./templates/command/new`.

## fickle/cxx-lib
Usage: `conan new <name>/<version> --template fickle/cxx-lib`

This template generates a C++ library that uses conan and CMake.

It includes:
* unit testing with gtest
* optional code coverage with lcov using https://github.com/alexFickle/lcov-cmake
* Doxygen configuration
* clang format configuration
* README.md

The generated project additionally contains a simple, working example.

## fickle/cxx-header-only
Usage: `conan new <name>/<version> --template fickle/cxx-header-only`

Identical features to cxx-lib, just for a header only C++ library.

## fickle/cxx-exe
Usage: `conan new <name>/version --template fickle/cxx-exe`

Identical features to cxx-lib, just for C++ executables.

Splits source files into two targets.
The first is a static library that can have unit tests written
for it.
The second is the executable that must have main in it but probably
no other source files.

## fickle/cxx-exp
Usage: `conan new <name>/<version> --template fickle/cxx-exp`

Very simple project structure intended to quickly experiment with something.
Has no directories and a single source file.
The code you are experimenting with and its tests go in the same source file.

Features:
* unit testing with gtest
* optional code coverage with lcov using https://github.com/alexFickle/lcov-cmake
* clang format configuration
