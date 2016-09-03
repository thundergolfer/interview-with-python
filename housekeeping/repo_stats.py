# Get stats on the number of questions, answers, lines of code etc etc in the repo.

import os
import sys
from os import listdir
from os.path import isfile, isdir, join, splitext

def main():
    """ Run through all relevant files in the projet and print to console some stats. """
    nloc_in_project, num_problems, num_questions = 0,0,0
    search_dir = os.path.dirname(os.getcwd()) # we want the parent directory
    for folder, subfolders, files in os.walk(search_dir, topdown=False):
        for f in files:
            fullpath = os.path.join(folder,f)
            if (not fullpath.endswith('.py')
                and not fullpath.endswith('.ipynb')
                and not fullpath.endswith('.md')): continue # ignore .git hidden folder files and others
            with open(fullpath, 'r') as f:
                try:
                    lines = f.readlines()
                except UnicodeDecodeError: continue
                if fullpath.endswith('.py'): nloc_in_project += len(lines)
                if fullpath.endswith('.py') and '-answer' in fullpath: num_problems += 1
                if fullpath.endswith('.ipynb'): num_questions += 1

    print("Lines of code in project: ", nloc_in_project)
    print("Number of Code Exercises: ", num_problems)
    print("Number of Worded Questions: ", num_questions )



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
