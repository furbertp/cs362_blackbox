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

    def test_two_ccv(self):
        """Visa Test"""
        self.assertTrue(credit_card_validator('4521009777447437'), msg='Expected {}, Recieved{}'.format(True, credit_card_validator('4521009777447437')))

    def test_three_ccv(self):
        """Master Card Test"""
        self.assertTrue(credit_card_validator('5402410866908738'), msg='Expected {}, Recieved{}'.format(True, credit_card_validator('5402410866908738')))

    def test_four_ccv(self):
        """American Express Card Test"""
        self.assertTrue(credit_card_validator('340954407803631'), msg='Expected {}, Recieved{}'.format(True, credit_card_validator('340954407803631')))



    def random_visa_number(self):
        """returns random_visa_number"""
        return '4' + str(random.randint(0,999999999999999))

    def random_master_card_number(self):
        """returns random_master_card_number"""
        pass

#Main conditional
if __name__ == "__main__":
    unittest.main()
