#Author: Patrick Furbert
#Date: 18-Oct-20

#Testing Methodology


"""
Visa
    Prefix(es): 4
    Length: 16
MasterCard
    Prefix(es): 51 through 55 and 2221 through 2720 
    Length: 16
American Express
    Prefix(es): 34 and 37
    Length: 15
"""

#Required Modules
import unittest, random
from unittest import TestCase
from credit_card_validator import credit_card_validator

#Class Definitions
class Test_Credit_Card_Validator(TestCase):
    """Represents a test suite for trying to unconver bugs in Test_Credit_Card_Validator"""

    def test_one_ccv(self):
        """Visa Test Example"""
        self.assertTrue(credit_card_validator(self.random_visa_number()), msg='Expected {}, Recieved{}'.format(True, credit_card_validator(self.random_visa_number())))

    def random_visa_number(self):
        """returns random_visa_number"""
        return '4' + str(random.randint(0,999999999999999))

#Main conditional
if __name__ == "__main__":
    unittest.main()
