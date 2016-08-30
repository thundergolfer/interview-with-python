import unittest

class Person(object):
    def getGender( self ):
        return "Unknown"

class Male( Person ):
    def getGender( self ):
        return "Male"

class Female( Person ):
    def getGender( self ):
        return "Female"

if __name__ == '__main__':
    aFemale = Female()
    aMale = aMale()
    print( aMale.getGender() )
    print( aFemale.getGender() )
