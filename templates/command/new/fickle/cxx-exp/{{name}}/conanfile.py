from conans import ConanFile, CMake

class {{package_name}}ConanFile(ConanFile):
    name = "{{name}}"
    version = "{{version}}"
    options = {"coverage": [None, "lcov"]}
    settings = "os", "arch", "compiler", "build_type"
    generators = "cmake"
    build_requires = "gtest/1.8.1@bincrafters/stable"

    def build_requirements(self):
        if self.options.coverage == "lcov":
            self.build_requires("lcov_cmake/0.1.0@fickle/testing")

    def build(self):
        cmake = CMake(self)
        if self.options.coverage == "lcov":
            cmake.definitions["LCOV_ENABLED"] = True
        cmake.configure()
        cmake.build()
        cmake.test(output_on_failure=True)
