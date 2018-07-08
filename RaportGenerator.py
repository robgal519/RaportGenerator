import os
from DataCollector import get_file_to_analyze, analyze_files, prepare_files_to_analyze, get_dir_to_analyze
from xlsxGenerator import generate_excel_workbook
import ArgumentManager
from sys import argv


def single_file_analysis():
    global file, analyze_unit, data_from_files, data
    file = get_file_to_analyze()
    analyze_unit = prepare_files_to_analyze(parser.recurrent, file)
    data_from_files = analyze_files(analyze_unit)
    path = os.path.normpath(file).split(os.path.sep)
    data = [[os.path.basename(file), data_from_files]]
    # noinspection SpellCheckingInspection
    generate_excel_workbook(str(path[-2]) + '.xlsx', data)


def directory_analysis():
    global file, data, analyze_unit, data_from_files
    directory = get_dir_to_analyze()
    all_files = os.listdir(directory)
    files = []
    for file in all_files:
        if ('.cpp' or '.C' or '.c' or '.hpp' or '.h') in file:
            files.append(file)
    data = []
    for base_file in files:
        analyze_unit = prepare_files_to_analyze(parser.recurrent, os.path.join(directory, base_file))
        data_from_files = analyze_files(analyze_unit)
        data.append([base_file, data_from_files])
    # noinspection SpellCheckingInspection
    generate_excel_workbook(str(os.path.basename(directory)) + '.xlsx', data)


if __name__ == '__main__':
    parser = ArgumentManager.generate_argument_parser(argv[1:])

    if parser.single_file:
        single_file_analysis()
    else:
        directory_analysis()
