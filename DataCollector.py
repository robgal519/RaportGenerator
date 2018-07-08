import os
import subprocess
import tkinter
from tkinter import filedialog


def get_file_to_analyze():
    tkinter.Tk().withdraw()
    return filedialog.askopenfilename(title="Source file for the rapport",
                                      filetypes=(
                                          ("C++ source file", "*.cpp"),
                                          ("C++ source file", "*.C"),
                                          ("C++ header file", "*.hpp"),
                                          ("C source file", "*.c"),
                                          ("C header file", "*.h")
                                                )
                                      )


def get_dir_to_analyze():
    tkinter.Tk().withdraw()
    return filedialog.askdirectory()


def get_all_included_files(path):
    relative_files = []
    with open(path) as input_file:
        for line in input_file:
            if "include" in line:
                included_file_relative_path = line.split('"')[1]
                if included_file_relative_path:
                    relative_files.append(included_file_relative_path)

    current_path = os.path.split(path)
    absolute_files = map(lambda x: os.path.join(current_path[0], x), relative_files)
    return list(absolute_files)


def recursive_include_analyze(path):
    final_result = []
    result = get_all_included_files(path)
    final_result.append(path)
    for file_path in result:
        final_result += recursive_include_analyze(file_path)
    return final_result


def strip_declaration_string_from_argument_names(declaration):
    a = declaration.split("(")
    b = a[1].split(")")
    begin = a[0]
    if b.__len__() >= 2:
        end = b[1]
    else:
        end = ""
    args = b[0].split(",")
    final_args = []
    for arg in args:
        k = arg.lstrip().split(" ")
        final_args.append(k[0])
    result = begin + "(" + ", ".join(final_args) + ")" + end
    return result.lstrip()


def extract_files_and_declarations(ctags_return_string):
    result = []
    for lines in ctags_return_string.split("\n")[:-1]:  # last line os empty
        foo = lines.split("\t")
        if foo[3] == "f":
            # remove everything after last ')', and two chars from begin added by ctags
            declaration = ")".join(foo[2].split(")")[:-1])[2:]
            # add filename and function declaration
            result.append([os.path.basename(foo[1]), strip_declaration_string_from_argument_names(declaration)])
    return result


def analyze_files(files):
    """
    analysis files from input
    finds function declarations, strips argument names leaving argument type

    This

    This function has requirement: ctags has to be installed in system
    :rtype: [[]] list of lists with file and function declaration
    :param files: list of files to analyze
    """
    if os.name == 'nt':  # windows case
        ctags_command = "ctags.exe"
    else:
        ctags_command = "ctags"

    arguments_of_call = ["-f", "-"] + files
    ctags_return_string = subprocess.check_output([ctags_command] + arguments_of_call).decode('utf-8')
    return extract_files_and_declarations(ctags_return_string)


def prepare_files_to_analyze(recursive, path):
    if recursive:
        files = recursive_include_analyze(path)
    else:
        if os.path.isfile(path):
            files = [path]
        else:
            raise ValueError("path is not a file")
    return files
