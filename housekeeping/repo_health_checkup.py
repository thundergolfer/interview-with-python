#
# Script to check repo for formatting problems, missing sections, spelling errors etc.
#
import os
import re
import sys, token, tokenize

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

def check_markdown( lines ):
    """
    Check that markdown files has all components present and sticks to
    standard format for this repo.
    """
    return True # TODO

def check_amount_of_commenting( readable ):
    """
    Check lines of file to see whether it has a lot of commenting in it,
    which we take to mean the presence of code explanation.
    """
    prev_toktype = token.INDENT
    first_line = None
    last_lineno = -1
    last_col = 0
    comment_lines = 0
    tokgen = tokenize.generate_tokens( readable )
    for toktype, ttext, (slineno, scol), (elineno, ecol), ltext in tokgen:
        if 1:   # Change to if 1 to see the tokens fly by.
            print("%10s %-14s %-20r %r" % (
                tokenize.tok_name.get(toktype, toktype),
                "%d.%d-%d.%d" % (slineno, scol, elineno, ecol),
                ttext, ltext
                ))
        if slineno > last_lineno:
            last_col = 0
        if scol > last_col:
            comment_lines += scol - last_col
        if toktype == token.STRING and prev_toktype == token.INDENT:
            # Docstring
            mod.write("#--")
        elif toktype == tokenize.COMMENT:
            # Comment
            comment_lines += 1
        prev_toktype = toktype
        last_col = ecol
        last_lineno = elineno
    # TODO // fix this function

def check_for_tags( lines ):
    """ Check if a problems answer file has tags in it. True, if yes. """
    match = re.search(r'##\$\$##(\s\S+,)+(\s\S+)', lines )
    return True if match else False

def check_for_code_output_example( lines ):
    """
    Check a Markdown problem description file for the presence of a code input to
    output example. ie. file should have something like: double_this(4) # > 8
    """
    match = re.search(r'`{3}.+\s`{3}', lines, re.DOTALL)
    return True if match else False

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
