import unittest

def remove_duplicates( l ):
    return list(set(l))

def remove_duplicates_badSolution( li ):
    """ DO NOT DO THIS. It shows a lack of understanding of set(). """
    newli=[]
    seen = set()
    for item in li:
        if item not in seen:
            seen.add( item )
            newli.append(item)

    return newli

if __name__ == '__main__':
    singles = remove_duplicates( [1,2,3,3,4,55,5,66,66,77,4])
    print(singles)
