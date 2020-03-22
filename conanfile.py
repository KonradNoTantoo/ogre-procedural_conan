from conans import ConanFile, CMake, tools
import os


class OgreProceduralConan(ConanFile):
    name = "ogre-procedural"
    version = "0.3.200322"
    license = "MIT"
    author = "konrad.no.tantoo"
    url = "https://github.com/KonradNoTantoo/ogreprocedural_conan"
    description = "Ogre Procedural is a C++ library which aims to produce procedural geometry for Ogre3D."
    topics = ("Procedural", "Procedural geometry", "Ogre3D", "conan")
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = {"shared": False}
    generators = "cmake"
    folder_name = "{}-{}".format(name, version)

    scm = {
        "type": "git",
        "subfolder": folder_name,
        "url": "https://github.com/OGRECave/ogre-procedural.git",
        "revision": "89b9abca873925e344d0c4e0e6d4dd7390e41c5b",
        "submodule": "recursive" 
    }


    def requirements(self):
        self.requires("ogre3d/1.12.5@utopia/testing")


    def source(self):
        tools.replace_in_file("{}/CMakeLists.txt".format(self.folder_name), "project(OgreProcedural)",
                              '''project(OgreProcedural)
include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()''')


    def configure_cmake(self):
        cmake = CMake(self)

        # put definitions here so that they are re-used in cmake between
        # build() and package()
        cmake.definitions["OgreProcedural_STATIC"] = "ON" if self.options.shared else "OFF"
        cmake.definitions["OgreProcedural_BUILD_SAMPLES"] = "OFF"

        cmake.configure(source_folder=self.folder_name)
        return cmake


    def build(self):
        cmake = self.configure_cmake()
        cmake.build()


    def package(self):
        cmake = self.configure_cmake()
        cmake.install()


    def package_info(self):
        self.cpp_info.libs = ["OgreProcedural_d" if self.settings.build_type == "Debug" else "OgreProcedural"]
