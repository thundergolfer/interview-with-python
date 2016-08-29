#
# Create a file in each problem directory named <PROBLEM-NAME>-answer.py, if that file doesn't already exist.
#
# Author: Jonathon Belotti <thundergolfer>
#
import os

tags_header = "##$$## ---------- TAGS ----------- ##$$##\n"
tags_footer = "##$$## --------- ENDTAGS --------- ##$$##\n"
user_prompt = "###### - Write your answer below - ######\n"

for root, dirs, files in os.walk(".", topdown=False):
    for name in dirs:
        new_fp = os.path.join(root,name, name + '-answer.py')
        if not os.path.isfile(new_fp):
            with open(new_fp, 'w') as newfile:
                # write the directory name in as tags
                tag_tokens = name.split('-')
                newfile.write(tags_header)
                newfile.write('##$$## ' + ','.join(tag_tokens)+'\n')
                newfile.write(tags_footer)
                newfile.write('\n')
                newfile.write(user_prompt)
