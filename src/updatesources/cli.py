from .internal import HelpFormatter
from .updatesources import update_sources
import argparse
import sys


_version = "0.1.0"
_default_input_file_name = ".sources"
_default_output_file_name = "sources.cmake"


def _setup_parser():
    parser = argparse.ArgumentParser(
        formatter_class=HelpFormatter,
        description=f'''
Reads a {_default_input_file_name} file to generate a {_default_output_file_name} file which populates CMake
variables with a list source files which can be used within a CMakeLists.txt file
''',
        epilog=f'''
Additional Information:
  Sample {_default_input_file_name} file format:

    PROJECT=CMAKE_VARIABLE_NAME
    ./myDirectory/CPPNonRecursiveFileSearch,*.cpp
    ./myDirectory/CPPRecursiveFileSearch,**.cpp
    ./myDirectory/CPPAndHeaderNonRecursiveFileSearch,*.cpp,*.h
    ./myDirectory/CPPAndHeaderRecursiveFileSearch,**.cpp,**.h OR ./myDirectory/CPPAndHeaderRecursiveFileSearch
    ./myDirectory/myCPPFile.cpp
    ./myDirectory/myHFile.h
    -./myDirectory/CPPNonRecursive/CPPIgnoredSubfolder,*.cpp
    -./myDirectory/ignoredHFile.h
    
  Note: Multiple projects can be defined within a single {_default_input_file_name} file 
''')

    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s v{_version}")
    parser.add_argument("path", nargs='?', default=".",
                        help=f"[Optional] Path to the directory that contains the {_default_input_file_name} file")
    parser.add_argument("-i", "--input", default=_default_input_file_name,
                        help=f"Specify the name of the input file")
    parser.add_argument("-o", "--output", default=_default_output_file_name,
                        help=f"Specify the name of the generated output file)")

    return parser


def main(args=None):
    parser = _setup_parser()

    if not args:
        args = sys.argv[1:]

    parsed = parser.parse_args(args)

    print(f"Generating {parsed.output} from {parsed.input}")
    update_sources(parsed)


if __name__ == "__main__":
    main()
