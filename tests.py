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
    """Represents a test suite for trying to unconver bugs in Credit_Card_Validator"""

    #bug3
    def test_ccv_visa(self):
        """Visa Test"""
        self.assertTrue(credit_card_validator('4521009777447437'), msg='Expected {}, Recieved{}'.format(True, credit_card_validator('4521009777447437')))

    def test_ccv_master_card_4(self):
        """Master Card Test"""
        self.assertTrue(credit_card_validator('5402410866908738'), msg='Expected {}, Recieved{}'.format(True, credit_card_validator('5402410866908738')))

    #bug4
    def test_ccv_amex_1(self):
        """American Express Card Test"""
        self.assertTrue(credit_card_validator('340954407803631'), msg='Expected {}, Recieved{}'.format(True, credit_card_validator('340954407803631')))
    
    #bug4
    def test_ccv_amex_2(self):
        """American Express Card Test"""
        self.assertTrue(credit_card_validator('370954407803631'), msg='Expected {}, Recieved{}'.format(True, credit_card_validator('370954407803631')))

    #bug1
    def test_ccv_length_zero(self):
        """Test an empty string"""
        self.assertTrue(credit_card_validator(""), msg='Expected {}, Recieved {}'.format(False, credit_card_validator("")))

    def test_ccv_length_one(self):
        """Test a one digit string"""
        self.assertTrue(credit_card_validator("0"), msg='Expected {}, Recieved {}'.format(False, credit_card_validator("0")))
    
    def test_ccv_2_visa_correct_cs(self):
        """test a two digit visa with correct checksum"""
        self.assertTrue(credit_card_validator("42"), msg='Expected {}, Recieved {}'.format(False, credit_card_validator("42")))

    def test_ccv_2_visa_incorrect_cs(self):
        """test a two digit visa with incorrect checksum"""
        self.assertTrue(credit_card_validator("46"), msg='Expected {}, Recieved {}'.format(False, credit_card_validator("46")))

    def test_ccv_2_amex_correct_cs(self):
        """test a two digit amex with correct checksum"""
        self.assertTrue(credit_card_validator("34"), msg='Expected {}, Recieved {}'.format(False, credit_card_validator("34")))

#VISA 4 Range

    def test_ccv_visa_correct_cs_15_digits_4(self):
        """test 15 digit visa with correct checksum"""
        self.assertTrue(credit_card_validator("444926557220183"), msg='Expected {}, Recieved {}'.format(False, credit_card_validator("444926557220183")))
        
    def test_ccv_visa_incorrect_cs_15_digits_4(self):
        """test 15 digit visa with incorrect checksum"""
        self.assertTrue(credit_card_validator("444926557222183"), msg='Expected {}, Recieved {}'.format(False, credit_card_validator("444926557222183")))

    def test_ccv_visa_correct_cs_16_digits_4(self):
        """test 16 digit visa with correct checksum"""
        self.assertTrue(credit_card_validator("4449265572210300"), msg='Expected {}, Recieved {}'.format(True, credit_card_validator("4449265572210300")))

    def test_ccv_visa_incorrect_cs_16_digits_4(self):
        """test 16 digit visa with incorrect checksum"""
        self.assertTrue(credit_card_validator("4449265572210320"), msg='Expected {}, Recieved {}'.format(False, credit_card_validator("4449265572210320")))

    def test_ccv_visa_correct_cs_17_digits_4(self):
        """test 17 digit visa with correct checksum"""
        self.assertTrue(credit_card_validator("44492655722100272"), msg='Expected {}, Recieved {}'.format(False, credit_card_validator("44492655722100272")))

    def test_ccv_visa_incorrect_cs_17_digits_4(self):
        """test 17 digit visa with incorrect checksum"""
        self.assertTrue(credit_card_validator("44492655722100282"), msg='Expected {}, Recieved {}'.format(False, credit_card_validator("44492655722100282")))




#MC 2221-2720 Range

    def test_ccv_mc_correct_cs_15_digits_22xx(self):
        """test 15 digit mc with correct checksum"""
        self.assertTrue(credit_card_validator("227266379231628"), msg='Expected {}, Recieved {}'.format(False, credit_card_validator("227266379231628")))
        
    def test_ccv_mc_incorrect_cs_15_digits_22xx(self):
        """test 15 digit mc with incorrect checksum"""
        self.assertTrue(credit_card_validator("227266379231638"), msg='Expected {}, Recieved {}'.format(False, credit_card_validator("227266379231638")))

    def test_ccv_mc_correct_cs_16_digits_22xx(self):
        """test 16 digit mc with correct checksum"""
        self.assertTrue(credit_card_validator("2272663792310007"), msg='Expected {}, Recieved {}'.format(True, credit_card_validator("2272663792310007")))

    def test_ccv_mc_incorrect_cs_16_digits_22xx(self):
        """test 16 digit mc with incorrect checksum"""
        self.assertTrue(credit_card_validator("2272663792310207"), msg='Expected {}, Recieved {}'.format(False, credit_card_validator("2272663792310207")))

    def test_ccv_mc_correct_cs_17_digits_22xx(self):
        """test 17 digit mc with correct checksum"""
        self.assertTrue(credit_card_validator("22726637923180059"), msg='Expected {}, Recieved {}'.format(False, credit_card_validator("22726637923180059")))

    def test_ccv_mc_incorrect_cs_17_digits_22xx(self):
        """test 17 digit mc with incorrect checksum"""
        self.assertTrue(credit_card_validator("22726637923180159"), msg='Expected {}, Recieved {}'.format(False, credit_card_validator("22726637923180159")))


#MC 51-55 Range

    def test_ccv_mc_correct_cs_15_digits_5x(self):
        """test 15 digit mc with correct checksum"""
        self.assertTrue(credit_card_validator("536044062360012"), msg='Expected {}, Recieved {}'.format(False, credit_card_validator("536044062360012")))
        
    def test_ccv_mc_incorrect_cs_15_digits_5x(self):
        """test 15 digit mc with incorrect checksum"""
        self.assertTrue(credit_card_validator("536044062367012"), msg='Expected {}, Recieved {}'.format(False, credit_card_validator("536044062367012")))

    def test_ccv_mc_correct_cs_16_digits_5x(self):
        """test 16 digit mc with correct checksum"""
        self.assertTrue(credit_card_validator("5360440623640027"), msg='Expected {}, Recieved {}'.format(True, credit_card_validator("5360440623640027")))

    def test_ccv_mc_incorrect_cs_16_digits_5x(self):
        """test 16 digit mc with incorrect checksum"""
        self.assertTrue(credit_card_validator("5360440623640227"), msg='Expected {}, Recieved {}'.format(False, credit_card_validator("5360440623640227")))

    def test_ccv_mc_correct_cs_17_digits_5x(self):
        """test 17 digit mc with correct checksum"""
        self.assertTrue(credit_card_validator("53604406236450043"), msg='Expected {}, Recieved {}'.format(False, credit_card_validator("53604406236450043")))

    def test_ccv_mc_incorrect_cs_17_digits_5x(self):
        """test 17 digit mc with incorrect checksum"""
        self.assertTrue(credit_card_validator("53604406236453043"), msg='Expected {}, Recieved {}'.format(False, credit_card_validator("53604406236453043")))


#AMEX 34 Range

    def test_ccv_amex_correct_cs_14_digits_34(self):
        """test 14 digit amex with correct checksum"""
        self.assertTrue(credit_card_validator("34814453743118"), msg='Expected {}, Recieved {}'.format(False, credit_card_validator("34814453743118")))
        
    def test_ccv_amex_incorrect_cs_14_digits_34(self):
        """test 14 digit amex with incorrect checksum"""
        self.assertTrue(credit_card_validator("34814453743128"), msg='Expected {}, Recieved {}'.format(False, credit_card_validator("34814453743128")))

    def test_ccv_amex_correct_cs_15_digits_34(self):
        """test 15 digit amex with correct checksum"""
        self.assertTrue(credit_card_validator("348144537430115"), msg='Expected {}, Recieved {}'.format(True, credit_card_validator("348144537430115")))

    def test_ccv_amex_incorrect_cs_15_digits_34(self):
        """test 15 digit amex with incorrect checksum"""
        self.assertTrue(credit_card_validator("348144537432115"), msg='Expected {}, Recieved {}'.format(False, credit_card_validator("348144537432115")))

    def test_ccv_amex_correct_cs_16_digits_34(self):
        """test 16 digit amex with correct checksum"""
        self.assertTrue(credit_card_validator("3481445374301538"), msg='Expected {}, Recieved {}'.format(False, credit_card_validator("3481445374301538")))

    def test_ccv_amex_incorrect_cs_16_digits_34(self):
        """test 16 digit amex with incorrect checksum"""
        self.assertTrue(credit_card_validator("3481445374301548"), msg='Expected {}, Recieved {}'.format(False, credit_card_validator("3481445374301548")))


#AMEX 37 Range

    def test_ccv_amex_correct_cs_14_digits_37(self):
        """test 14 digit amex with correct checksum"""
        self.assertTrue(credit_card_validator("37485687150490"), msg='Expected {}, Recieved {}'.format(False, credit_card_validator("37485687150490")))
        
    def test_ccv_amex_incorrect_cs_14_digits_37(self):
        """test 14 digit amex with incorrect checksum"""
        self.assertTrue(credit_card_validator("37485687151490"), msg='Expected {}, Recieved {}'.format(False, credit_card_validator("37485687151490")))

    def test_ccv_amex_correct_cs_15_digits_37(self):
        """test 15 digit amex with correct checksum"""
        self.assertTrue(credit_card_validator("374856871581024"), msg='Expected {}, Recieved {}'.format(True, credit_card_validator("374856871581024")))

    def test_ccv_amex_incorrect_cs_15_digits_37(self):
        """test 15 digit amex with incorrect checksum"""
        self.assertTrue(credit_card_validator("374856871581524"), msg='Expected {}, Recieved {}'.format(False, credit_card_validator("374856871581524")))

    def test_ccv_amex_correct_cs_16_digits_37(self):
        """test 16 digit amex with correct checksum"""
        self.assertTrue(credit_card_validator("3748568715081615"), msg='Expected {}, Recieved {}'.format(False, credit_card_validator("3748568715081615")))

    def test_ccv_amex_incorrect_cs_16_digits_37(self):
        """test 16 digit amex with incorrect checksum"""
        self.assertTrue(credit_card_validator("3748568715781615"), msg='Expected {}, Recieved {}'.format(False, credit_card_validator("3748568715781615")))

#Prefix Range Testing
    
    #Visa 16 digits

    #Above 4
    def test_ccv_visa_correct_cs_16_digits_3(self):
        """test 16 digit visa with correct checksum"""
        self.assertTrue(credit_card_validator("3052380846991740"), msg='Expected {}, Recieved {}'.format(True, credit_card_validator("3052380846991740")))

    def test_ccv_visa_incorrect_cs_16_digits_3(self):
        """test 16 digit visa with incorrect checksum"""
        self.assertTrue(credit_card_validator("3052380841991740"), msg='Expected {}, Recieved {}'.format(True, credit_card_validator("3052380841991740")))


    #Below 4
    def test_ccv_visa_correct_cs_16_digits_5(self):
        """test 16 digit visa with correct checksum"""
        self.assertTrue(credit_card_validator("5052380846990572"), msg='Expected {}, Recieved {}'.format(True, credit_card_validator("5052380846990572")))

    def test_ccv_visa_incorrect_cs_16_digits_5(self):
        """test 16 digit visa with incorrect checksum"""
        self.assertTrue(credit_card_validator("5052380845990572"), msg='Expected {}, Recieved {}'.format(True, credit_card_validator("5052380845990572")))


    #MasterCard 16 digits

    #Below 51
    #done in visa test

    #Above 54
    def test_ccv_mc_correct_cs_16_digits_gt_54(self):
        """test 16 digit mc with correct checksum"""
        self.assertTrue(credit_card_validator("6052380846990414"), msg='Expected {}, Recieved {}'.format(True, credit_card_validator("6052380846990414")))
    
    def test_ccv_mc_incorrect_cs_16_digits_gt_54(self):
        """test 16 digit mc with incorrect checksum"""
        self.assertTrue(credit_card_validator("6052310846990414"), msg='Expected {}, Recieved {}'.format(True, credit_card_validator("6052310846990414")))


    #Below 2221
    def test_ccv_mc_correct_cs_16_digits_lt_2221(self):
        """test 16 digit mc with correct checksum"""
        self.assertTrue(credit_card_validator("2220380846990758"), msg='Expected {}, Recieved {}'.format(True, credit_card_validator("2220380846990758")))

    def test_ccv_mc_incorrect_cs_16_digits_lt_2221(self):
        """test 16 digit mc with incorrect checksum"""
        self.assertTrue(credit_card_validator("2220310846990758"), msg='Expected {}, Recieved {}'.format(True, credit_card_validator("2220310846990758")))

    #Above 2720
    def test_ccv_mc_correct_cs_16_digits_gt_2270(self):
        """test 16 digit mc with correct checksum"""
        self.assertTrue(credit_card_validator("2721380846990687"), msg='Expected {}, Recieved {}'.format(True, credit_card_validator("2721380846990687")))
    
    def test_ccv_mc_incorrect_cs_16_digits_gt_2270(self):
        """test 16 digit mc with incorrect checksum"""
        self.assertTrue(credit_card_validator("2721310846990687"), msg='Expected {}, Recieved {}'.format(True, credit_card_validator("2721310846990687")))



    #Amex 15 digits

    #Below 34
    def test_ccv_amex_correct_cs_15_digits_lt_34(self):
        """test 15 digit amex with correct checksum"""
        self.assertTrue(credit_card_validator("332138084699682"), msg='Expected {}, Recieved {}'.format(True, credit_card_validator("332138084699682")))
    
    def test_ccv_amex_incorrect_cs_15_digits_lt_34(self):
        """test 15 digit amex with incorrect checksum"""
        self.assertTrue(credit_card_validator("332131084699682"), msg='Expected {}, Recieved {}'.format(True, credit_card_validator("332131084699682")))


    #Between 34 - 37
    def test_ccv_amex_correct_cs_15_digits_34_37(self):
        """test 15 digit amex with correct checksum"""
        self.assertTrue(credit_card_validator("352138084699406"), msg='Expected {}, Recieved {}'.format(True, credit_card_validator("352138084699406")))

    def test_ccv_amex_incorrect_cs_15_digits_34_37(self):
        """test 15 digit amex with incorrect checksum"""
        self.assertTrue(credit_card_validator("352138084899406"), msg='Expected {}, Recieved {}'.format(True, credit_card_validator("352138084899406")))

    #Above 37
    def test_ccv_amex_correct_cs_15_digits_gt_37(self):
        """test 15 digit amex with correct checksum"""
        self.assertTrue(credit_card_validator("382138084699491"), msg='Expected {}, Recieved {}'.format(True, credit_card_validator("382138084699491")))

    def test_ccv_amex_incorrect_cs_15_digits_gt_37(self):
        """test 15 digit amex with incorrect checksum"""
        self.assertTrue(credit_card_validator("382131084699491"), msg='Expected {}, Recieved {}'.format(True, credit_card_validator("382131084699491")))



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
