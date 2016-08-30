#
# Script to check repo for formatting problems, missing sections, spelling errors etc.
#
import os

def main():
    for folder, subfolders, files in os.walk(os.getcwd(), topdown=False):
        for f in files:
            fullpath = os.path.join(folder,f)
            if '.git' in fullpath: continue # ignore .git hidden folder files
            print(fullpath) # just to check where we're walking
            # HEALTH CHECK FLOW
            #
            # if: README for a problem check for -> formatting, spelling, and a code output example

            # if: problem solution source code file then check for -> tags, unit tests, spelling

            # and... any other file check for -> spelling, "TODO" markers, amount of commenting


def check_amount_of_commenting( lines ):
    """
    Check lines of file to see whether it has a lot of commenting in it,
    which we take to mean the presence of code explanation.
    """
    raise NotImplementedError

def check_for_tags( lines ):
    """ Check if a problem solution file has tags in it. True, if yes. """
    raise NotImplementedError

def check_for_code_output_example( lines ):
    """
    Check a Markdown problem description file for the presence of a code input to
    output example. ie. file should have something like: double_this(4) # > 8
    """
    raise NotImplementedError


def check_spelling( lines ):
    """ Check the spelling of all words in the lines provided. """
    lines_to_check = []
    # We only want docstrings and #comment lines
    for line in lines:
        if '#' in line: # TODO: make this work properly for C++ files as well
            start_comment = line.index('#')
            lines_to_check.append(line[start_comment:])
        elif line.startswith('"""') and line.rstrip().endswith('"""'):
            lines_to_check.append(line) # single line docstring
        # TODO: Find and add multiline docstrings

def check_word( word ):
    """ Check spelling of a single word. """
    # TODO: Implement this function
    return word # just return the word for the moment


if __name__ == '__main__':
    main()
