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

# Unittests
class gender_inheritance_tests(unittest.TestCase):

    def setUp(self):
        self.male = Male()
        self.female = Female()

    def test_gender_inheritance(self):
        self.assertEqual( self.male.getGender(), "Male" )
        self.assertEqual( self.female.getGender(), "Female")

if __name__ == '__main__':
    aFemale = Female()
    aMale = Male()
    print( aMale.getGender() )
    print( aFemale.getGender() )
    unittest.main()
