#
# Script to check repo for formatting problems, missing sections, spelling errors etc.
#
import os
import re
import sys, token, tokenize

def main():
    search_dir = os.path.dirname(os.getcwd()) # we want the parent directory
    for folder, subfolders, files in os.walk(search_dir, topdown=False):
        for f in files:
            fullpath = os.path.join(folder,f)
            if not fullpath.endswith('.py') and not fullpath.endswith('.md'): continue # ignore .git hidden folder files
            print(fullpath) # just to check where we're walking
            with open(fullpath, 'r') as f:
                try:
                    lines = f.readlines()
                except UnicodeDecodeError: continue
                file_health = fullpath + '\n'
                # HEALTH CHECK FLOW
                #
                # if: README for a problem check for -> formatting, spelling, and a code output example
                if fullpath[-2:] == 'md':
                    file_health += "" if check_for_code_output_example(lines) else "missing output ex.\n"
                    # TODO: Add the rest of the checks
                # if: problem solution source code file then check for -> tags, unit tests, spelling
                elif fullpath.endswith('-answer.py'):
                    file_health += "" if check_for_tags(lines) else "missing tags!\n"
                    file_health += "" if check_for_unittests(lines) else "missing unittests!\n"
                    # TODO: Add spelling check
                # and... any other file check for -> spelling, "TODO" markers, amount of commenting
                else:
                    has_todos, _ = check_for_todos(lines)
                    if has_todos: file_health += "has TODOs to complete.\n"
                    comment_lines, total_lines = check_amount_of_commenting( f.readline )
                    if comment_lines / total_lines < 0.15: # arbitrary limit
                        file_health += "low commenting! " + str(comment_lines / total_lines) + "\n"
            if file_health != fullpath + '\n':
                print(file_health)

def check_markdown( lines ):
    """
    Check that markdown files has all components present and sticks to
    standard format for this repo.
    """
    return True # TODO

def check_for_todos( lines ): # TODO: It is inefficient to re-read through lines to check for different things
    """ Check for presence of 'TODO' markers in files. """
    todos = []
    for line in lines:
        if 'TODO' in line:
            todos.append(line[line.index('TODO'):])
    if not todos:
        return False, None
    else:
        return True, todos


def check_amount_of_commenting( readable ):
    """
    Check lines of file to see whether it has a lot of commenting in it,
    which we take to mean the presence of code explanation.
    """
    # TODO: I have hacked this code together and it could be silly and buggy.
    #       It does seem to get things roughly correct, which is good enough for the moment
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
        if toktype == token.STRING and prev_toktype == token.INDENT:
            # Docstring
            comment_lines += 1
        elif toktype == tokenize.COMMENT:
            # Comment
            comment_lines += 1
        prev_toktype = toktype
        last_col = ecol
        last_lineno = elineno
    return comment_lines, last_lineno # roughly num of comment lines divided by num of lines

def check_for_tags( lines ):
    """ Check if a problems answer file has tags in it. True, if yes. """
    lines = ''.join(lines)
    match = re.search(r'##\$\$##(\s\S+,)+(\s\S+)', lines )
    return True if match else False

def check_for_code_output_example( lines ):
    """
    Check a Markdown problem description file for the presence of a code input to
    output example. ie. file should have something like: double_this(4) # > 8
    """
    lines = ''.join(lines)
    match = re.search(r'`{3}.+\s`{3}', lines, re.DOTALL)
    return True if match else False

def check_for_unittests( lines ):
    """ Check python source code for unittests. """
    return True # TODO: Implement this

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
