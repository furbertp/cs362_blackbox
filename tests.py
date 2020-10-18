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
    
    def make_test_function(description, a):
        def test(self):
            self.assertTrue(credit_card_validator(a), description)
        return test


#    def test_two_ccv_visa(self):
#        """Visa Test"""
#        self.assertTrue(credit_card_validator('4521009777447437'), msg='Expected {}, Recieved{}'.format(True, credit_card_validator('4521009777447437')))

#    def test_three_ccv_master_card(self):
#        """Master Card Test"""
#        self.assertTrue(credit_card_validator('5402410866908738'), msg='Expected {}, Recieved{}'.format(True, credit_card_validator('5402410866908738')))

#    def test_four_ccv_amex(self):
#        """American Express Card Test"""
#        self.assertTrue(credit_card_validator('340954407803631'), msg='Expected {}, Recieved{}'.format(True, credit_card_validator('340954407803631')))



#    def random_visa_number(self):
#        """returns random_visa_number"""
#        return '4' + str(random.randint(0,999999999999999))

#    def random_master_card_number(self):
#        """returns random_master_card_number"""
#        pass

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

    #Create empty dictionary
    my_dict = {}

    #Create counter variable
    counter = 0

    #setup loop
    for num in generate_mc_nums():

        #add num to dictionary
        my_dict['mc_num_{}'.format(str(counter))] = num

        #increment counter
        counter = counter + 1

    #return dictionary
    return my_dict

#Main conditional
if __name__ == "__main__":
    #Create instance of Test_Credit_Card_Validator()
    my_tccv = Test_Credit_Card_Validator()

    #Create dictionary of mc card numbers with prefixes  2221-2720 inclusive
    testmap = generate_mc_dic()

    for name, param in testmap.items():
        test_func = my_tccv.make_test_function(name, param)
        klassname = 'Test_{}'.format(name)
        globals()[klassname] = type(klassname, (DynamicClassBase,),{'test_gen_{}'.format(name): test_func})


    unittest.main()
