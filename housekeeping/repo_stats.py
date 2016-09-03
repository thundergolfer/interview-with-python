# Get stats on the number of questions, answers, lines of code etc etc in the repo.

import os
import sys
from os import listdir
from os.path import isfile, isdir, join, splitext

def main():
    pass

def line_count_file(file_path, flags=None):
    """ Counts lines for given file in file_name """
    try:
        count = 0
        with open(file_path) as current_file:
            for line in current_file:
                if line.strip() == "" and flags != None and \
                   "--noempty" in flags:
                    continue
                count += 1

        return count
    except IOError:
        return -1

def line_count_files(file_name_list, flags=None):
    """ Counts lines for given set of files """
    total = 0
    for file_name in file_name_list:
        current = line_count_file(file_name, flags)
        if current >= 0:
            total += current
            print("%6d lines in %s" % (current, file_name))
        else:
            print("error: file not found (" + file_name + ")")
    return total

def line_count_dir(dir_path, flags, filters):
    """ Counts lines for files which are in given directory path and matches
        filter requirements """
    total = 0

    if "--filter" in flags:
        file_list = [join(dir_path, file_p) for file_p in listdir(dir_path)
                     if isfile(join(dir_path, file_p)) and
                     splitext(join(dir_path, file_p))[1] in filters]
    else:
        file_list = [join(dir_path, file_p) for file_p in listdir(dir_path)
                     if isfile(join(dir_path, file_p))]

    total += line_count_files(file_list, flags)

    if "-r" in flags:
        dir_list = [join(dir_path, directory) for directory in listdir(dir_path)
                    if isdir(join(dir_path, directory))]
        for directory in dir_list:
            total += line_count_dir(directory, flags, filters)

    return total

if __name__ == '__main__':
    main()
