# Check if a string is composed of all unique characters
# author: Matt Box

def all_unique(string):
    letters = sorted(string)
    for i in range(len(letters) - 1):
        if letters[i] == letters[i + 1]:
            return False
    return True

