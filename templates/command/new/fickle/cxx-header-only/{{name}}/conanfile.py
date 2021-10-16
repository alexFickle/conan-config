from conans import ConanFile, CMake, tools

class {{package_name}}ConanFile(ConanFile):
    name = "{{name}}"
    version = "{{version}}"
    options = {"coverage": [None, "lcov"]}
    settings = "os", "arch", "compiler", "build_type"
    generators = "cmake"
    exports_sources = "include/*", "test/*", "CMakeLists.txt"

    def _is_testing(self):
        return not tools.cross_building(self.settings)
    
    def build_requirements(self):
        if self.options.coverage == "lcov":
            self.build_requires("lcov_cmake/0.1.0@fickle/testing")
        if self._is_testing():
            self.build_requires("gtest/1.8.1@bincrafters/stable")

    def _configure(self):
        cmake = CMake(self)
        if self.options.coverage == "lcov":
            cmake.definitions["LCOV_ENABLED"] = True
        if not self._is_testing():
            cmake.definitions["BUILD_TESTING"] = False
        cmake.configure()
        return cmake

    def build(self):
        cmake = self._configure()
        cmake.build()
        if self._is_testing():
            cmake.test(output_on_failure=True)
    
    def package(self):
        cmake = self._configure()
        cmake.install()
    
    def package_info(self):
        self.info.header_only()
