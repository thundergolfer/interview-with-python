#
# Remove of a user's code from the answer files in each folder.
#
# Author: Jonathon Belotti <thundergolfer>
import os

for root, dirs, files in os.walk(".", topdown=False):
    for name in dirs:
        if not os.path.isfile(os.path.join(root,name, name + '-answer.py')):
            with open(os.path.join(root, name, name+'-answer.py'), 'w') as newfile:
                # Remove everything below the tags section
                # *How to do this?*
