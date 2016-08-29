#
# Author: Jonathon Belotti <thundergolfer>
#
from __future__ import print_function
import os
from argparse import ArgumentParser

def main():

    parser = ArgumentParser(description='Get your search query')
    parser.add_argument('query', type=str, nargs='+', help='enter some tags to search for')
    list_of_arg_words = vars(parser.parse_args())['query'] # SO SORRY FOR THIS LINE. IN A RUSH DON'T JUDGE ME
    query = [tag.lower() for tag in list_of_arg_words] # search query as a list of 'tokens'. eg ['this','is','my','search']
    print("query is: ", query)

    file_matches = []
    # TODO: Make this code not kinda rubbish
    # Search through all questions in "problems" and "worded_questions"
    for folder, subfolders, files in os.walk(os.getcwd(), topdown=False):
        for f in files:
            fullpath = os.path.join(folder,f)
            if (('problems' in fullpath or 'worded_questions' in fullpath)
                and not fullpath.endswith('.md')):  # This will very likely admit TOO MANY files. TODO: fix it
                with open(fullpath, 'r') as question_file:
                    lines = question_file.readlines()
                    # if at least one tag matches, add the file with its tags to our list
                    matched_tags = match_tags( get_tags_from_file(lines), query)
                    if matched_tags:
                        file_matches.append( (matched_tags, '...' + fullpath[-60:] ) ) # TODO: fix this hammy way of handling filename

    # order the matched files by number of matched tags. Ascending order
    file_matches = sorted(file_matches, key=lambda x: len(x[0]), reverse=True)
    print("Look Here: ") # TODO replace this print to console bit with something more useful
    for i, match in enumerate(file_matches):
        tags, name = match[0], match[1]
        print(str(i), ': ', name)
        print("\tMatches on: " , tags)

def match_tags( tags, query_tags ):
    return [tag.lower() for tag in tags if tag.lower() in query_tags]

def get_tags_from_file( lines ):
    """
    Extract the tags from a file and return them as a list
    """
    tags_header = "##$$##"
    for i, line in enumerate(lines):
        if tags_header in line:
            break
    else: # didn't break out of loop so no tags header
        return []
    tags_line = lines[i+1]
    just_tags = (''.join(ch for ch in tags_line if (ch.isalnum()) or ch == ',')).split(',')
    return [word.strip() for word in just_tags] # remove trailing and leading whitespace

if __name__ == '__main__':
    main()
