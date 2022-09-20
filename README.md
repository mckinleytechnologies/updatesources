# cmaketools

## Tools
+ updatesources: Generates a sources.cmake file which lists all the source files in the project


### updatesources

When using CMake, using `file(GLOB)` to find all the source files in project is not recommended (https://cmake.org/cmake/help/latest/command/file.html?highlight=glob#glob). 
However, manually adding all files to the CMakeLists.txt file is tedious and error-prone. This tool generates a `sources.cmake` file,
which can be referenced using `include()`, that contains all the source files in a project as a way to avoid using `file(GLOB)` while also 
avoiding having to manually specify files. The search paths for the source files and the cmake variable to populate is specified using
a `.sources` file.



