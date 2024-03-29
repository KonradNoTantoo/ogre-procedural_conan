from conans import ConanFile, CMake, tools
import os


class OgreProceduralConan(ConanFile):
    name = "ogre-procedural"
    version = "0.3.220412"
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
        "revision": "e3fe5b69a32faa3a66fed4a94bd1bce90e3ee7b9",
        "submodule": "recursive" 
    }


    def requirements(self):
        self.requires("ogre3d/13.4.0@utopia/testing")


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

        if self.settings.compiler == "Visual Studio":
            self.cpp_info.bindirs.append(os.path.join("bin", str(self.settings.build_type)))
            self.cpp_info.libdirs.append(os.path.join("lib", str(self.settings.build_type)))
