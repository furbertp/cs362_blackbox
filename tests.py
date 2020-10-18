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
    def test_ccv_visa(self):
        """Visa Test"""
        self.assertTrue(credit_card_validator('4521009777447437'), msg='Expected {}, Recieved{}'.format(True, credit_card_validator('4521009777447437')))

    def test_ccv_master_card(self):
        """Master Card Test"""
        self.assertTrue(credit_card_validator('5402410866908738'), msg='Expected {}, Recieved{}'.format(True, credit_card_validator('5402410866908738')))

    def test_ccv_amex(self):
        """American Express Card Test"""
        self.assertTrue(credit_card_validator('340954407803631'), msg='Expected {}, Recieved{}'.format(True, credit_card_validator('340954407803631')))

#Test generator function
def test_generator(a):
    """Function that is used to generate tests"""
    def test(self):
        self.assertTrue(credit_card_validator(a), msg='Card Number = {}'.format(a))
    return test

#Generate random numbers
def generate_mc_nums():
    """Generate mc numbers with prefixes 2221 through 2720"""
    
    #Create empty list
    numbers = []

    #setup loop
    for prefix in range(2221, 2720 +1):
        
        #Create random number
        random_int = random.randint(000000000000, 999999999999)

        #convert int to string and attach to prefix
        new_number = str(prefix) + str(random_int)

        #append to the numbers list
        numbers.append(new_number)

    return numbers

#create_dictionary
def generate_mc_dic():
    """generates dictionary with all the mc numbers"""

    #create empty dictionary
    my_dict = {}

    #create counter variable
    counter = 0

    #setup loop
    for num in generate_mc_nums():

        #add num to dictionary
        my_dict['mc_num_{}'.format(str(counter))] = num

        #increment counter
        counter = counter + 1

    #return dictionary
    return my_dict

mc_dict_nums = generate_mc_dic()

#main conditional
if __name__ == "__main__":
    unittest.main()
