# Author: Patrick Furbert
# Date: 18-Oct-20

# Testing Methodology
# Testing included correct and incorrect checksums. Checked empty string ini
# validator. Checked all prefix ranges and out of all prefix ranges. 

# Required Modules
import unittest
import random
from unittest import TestCase
from credit_card_validator import credit_card_validator


# Class Definitions
class Test_Credit_Card_Validator(TestCase):
    """Represents a test suite for trying to
    unconver bugs in Credit_Card_Validator"""

    # bug3
    def test_ccv_visa(self):
        """Visa Test"""
        self.assertTrue(credit_card_validator('4521009777447437'),
                        msg='Expected {}, Recieved{}'.format(True,
                        credit_card_validator('4521009777447437')))

    def test_ccv_master_card_4(self):
        """Master Card Test"""
        self.assertTrue(credit_card_validator('5402410866908738'),
                        msg='Expected {}, Recieved{}'.format(True,
                        credit_card_validator('5402410866908738')))

    # bug4
    def test_ccv_amex_1(self):
        """American Express Card Test"""
        self.assertTrue(credit_card_validator('340954407803631'),
                        msg='Expected {}, Recieved{}'.format(True,
                        credit_card_validator('340954407803631')))

    # bug4
    def test_ccv_amex_2(self):
        """American Express Card Test"""
        self.assertTrue(credit_card_validator('370954407803631'),
                        msg='Expected {}, Recieved{}'.format(True,
                        credit_card_validator('370954407803631')))

    # bug1
    def test_ccv_length_zero(self):
        """Test an empty string"""
        self.assertTrue(credit_card_validator(""),
                        msg='Expected {}, Recieved {}'.format(False,
                        credit_card_validator("")))

    def test_ccv_length_one(self):
        """Test a one digit string"""
        self.assertTrue(credit_card_validator("0"),
                        msg='Expected {}, Recieved {}'.format(False,
                        credit_card_validator("0")))
    
    def test_ccv_2_visa_correct_cs(self):
        """test a two digit visa with correct checksum"""
        self.assertTrue(credit_card_validator("42"),
                        msg='Expected {}, Recieved {}'.format(False,
                        credit_card_validator("42")))

    def test_ccv_2_visa_incorrect_cs(self):
        """test a two digit visa with incorrect checksum"""
        self.assertTrue(credit_card_validator("46"),
                        msg='Expected {}, Recieved {}'.format(False,
                        credit_card_validator("46")))

    def test_ccv_2_amex_correct_cs(self):
        """test a two digit amex with correct checksum"""
        self.assertTrue(credit_card_validator("34"),
                        msg='Expected {}, Recieved {}'.format(False,
                        credit_card_validator("34")))

# VISA 4 Range

    def test_ccv_visa_correct_cs_15_digits_4(self):
        """test 15 digit visa with correct checksum"""
        self.assertTrue(credit_card_validator("444926557220183"),
                        msg='Expected {}, Recieved {}'.format(False,
                        credit_card_validator("444926557220183")))
        
    def test_ccv_visa_incorrect_cs_15_digits_4(self):
        """test 15 digit visa with incorrect checksum"""
        self.assertTrue(credit_card_validator("444926557222183"),
                        msg='Expected {}, Recieved {}'.format(False,
                        credit_card_validator("444926557222183")))

    def test_ccv_visa_correct_cs_16_digits_4(self):
        """test 16 digit visa with correct checksum"""
        self.assertTrue(credit_card_validator("4449265572210300"),
                        msg='Expected {}, Recieved {}'.format(True,
                        credit_card_validator("4449265572210300")))

    def test_ccv_visa_incorrect_cs_16_digits_4(self):
        """test 16 digit visa with incorrect checksum"""
        self.assertTrue(credit_card_validator("4449265572210320"),
                        msg='Expected {}, Recieved {}'.format(False,
                        credit_card_validator("4449265572210320")))

    def test_ccv_visa_correct_cs_17_digits_4(self):
        """test 17 digit visa with correct checksum"""
        self.assertTrue(credit_card_validator("44492655722100272"),
                        msg='Expected {}, Recieved {}'.format(False,
                        credit_card_validator("44492655722100272")))

    def test_ccv_visa_incorrect_cs_17_digits_4(self):
        """test 17 digit visa with incorrect checksum"""
        self.assertTrue(credit_card_validator("44492655722100282"),
                        msg='Expected {}, Recieved {}'.format(False,
                        credit_card_validator("44492655722100282")))

# MC 2221-2720 Range

    def test_ccv_mc_correct_cs_15_digits_22xx(self):
        """test 15 digit mc with correct checksum"""
        self.assertTrue(credit_card_validator("227266379231628"),
                        msg='Expected {}, Recieved {}'.format(False,
                        credit_card_validator("227266379231628")))
        
    def test_ccv_mc_incorrect_cs_15_digits_22xx(self):
        """test 15 digit mc with incorrect checksum"""
        self.assertTrue(credit_card_validator("227266379231638"),
                        msg='Expected {}, Recieved {}'.format(False,
                        credit_card_validator("227266379231638")))

    def test_ccv_mc_correct_cs_16_digits_22xx(self):
        """test 16 digit mc with correct checksum"""
        self.assertTrue(credit_card_validator("2272663792310007"),
                        msg='Expected {}, Recieved {}'.format(True,
                        credit_card_validator("2272663792310007")))

    def test_ccv_mc_incorrect_cs_16_digits_22xx(self):
        """test 16 digit mc with incorrect checksum"""
        self.assertTrue(credit_card_validator("2272663792310207"),
                        msg='Expected {}, Recieved {}'.format(False,
                        credit_card_validator("2272663792310207")))

    def test_ccv_mc_correct_cs_17_digits_22xx(self):
        """test 17 digit mc with correct checksum"""
        self.assertTrue(credit_card_validator("22726637923180059"),
                        msg='Expected {}, Recieved {}'.format(False,
                        credit_card_validator("22726637923180059")))

    def test_ccv_mc_incorrect_cs_17_digits_22xx(self):
        """test 17 digit mc with incorrect checksum"""
        self.assertTrue(credit_card_validator("22726637923180159"),
                        msg='Expected {}, Recieved {}'.format(False,
                        credit_card_validator("22726637923180159")))

# MC 51-55 Range

    def test_ccv_mc_correct_cs_15_digits_5x(self):
        """test 15 digit mc with correct checksum"""
        self.assertTrue(credit_card_validator("536044062360012"),
                        msg='Expected {}, Recieved {}'.format(False,
                        credit_card_validator("536044062360012")))
        
    def test_ccv_mc_incorrect_cs_15_digits_5x(self):
        """test 15 digit mc with incorrect checksum"""
        self.assertTrue(credit_card_validator("536044062367012"),
                        msg='Expected {}, Recieved {}'.format(False,
                        credit_card_validator("536044062367012")))

    def test_ccv_mc_correct_cs_16_digits_5x(self):
        """test 16 digit mc with correct checksum"""
        self.assertTrue(credit_card_validator("5360440623640027"),
                        msg='Expected {}, Recieved {}'.format(True,
                        credit_card_validator("5360440623640027")))

    def test_ccv_mc_incorrect_cs_16_digits_5x(self):
        """test 16 digit mc with incorrect checksum"""
        self.assertTrue(credit_card_validator("5360440623640227"),
                        msg='Expected {}, Recieved {}'.format(False,
                        credit_card_validator("5360440623640227")))

    def test_ccv_mc_correct_cs_17_digits_5x(self):
        """test 17 digit mc with correct checksum"""
        self.assertTrue(credit_card_validator("53604406236450043"),
                        msg='Expected {}, Recieved {}'.format(False,
                        credit_card_validator("53604406236450043")))

    def test_ccv_mc_incorrect_cs_17_digits_5x(self):
        """test 17 digit mc with incorrect checksum"""
        self.assertTrue(credit_card_validator("53604406236453043"),
                        msg='Expected {}, Recieved {}'.format(False,
                        credit_card_validator("53604406236453043")))

# AMEX 34 Range

    def test_ccv_amex_correct_cs_14_digits_34(self):
        """test 14 digit amex with correct checksum"""
        self.assertTrue(credit_card_validator("34814453743118"),
                        msg='Expected {}, Recieved {}'.format(False,
                        credit_card_validator("34814453743118")))
        
    def test_ccv_amex_incorrect_cs_14_digits_34(self):
        """test 14 digit amex with incorrect checksum"""
        self.assertTrue(credit_card_validator("34814453743128"),
                        msg='Expected {}, Recieved {}'.format(False,
                        credit_card_validator("34814453743128")))

    def test_ccv_amex_correct_cs_15_digits_34(self):
        """test 15 digit amex with correct checksum"""
        self.assertTrue(credit_card_validator("348144537430115"),
                        msg='Expected {}, Recieved {}'.format(True,
                        credit_card_validator("348144537430115")))

    def test_ccv_amex_incorrect_cs_15_digits_34(self):
        """test 15 digit amex with incorrect checksum"""
        self.assertTrue(credit_card_validator("348144537432115"),
                        msg='Expected {}, Recieved {}'.format(False,
                        credit_card_validator("348144537432115")))

    def test_ccv_amex_correct_cs_16_digits_34(self):
        """test 16 digit amex with correct checksum"""
        self.assertTrue(credit_card_validator("3481445374301538"),
                        msg='Expected {}, Recieved {}'.format(False,
                        credit_card_validator("3481445374301538")))

    def test_ccv_amex_incorrect_cs_16_digits_34(self):
        """test 16 digit amex with incorrect checksum"""
        self.assertTrue(credit_card_validator("3481445374301548"),
                        msg='Expected {}, Recieved {}'.format(False,
                        credit_card_validator("3481445374301548")))

# AMEX 37 Range

    def test_ccv_amex_correct_cs_14_digits_37(self):
        """test 14 digit amex with correct checksum"""
        self.assertTrue(credit_card_validator("37485687150490"),
                        msg='Expected {}, Recieved {}'.format(False,
                        credit_card_validator("37485687150490")))
        
    def test_ccv_amex_incorrect_cs_14_digits_37(self):
        """test 14 digit amex with incorrect checksum"""
        self.assertTrue(credit_card_validator("37485687151490"),
                        msg='Expected {}, Recieved {}'.format(False,
                        credit_card_validator("37485687151490")))

    def test_ccv_amex_correct_cs_15_digits_37(self):
        """test 15 digit amex with correct checksum"""
        self.assertTrue(credit_card_validator("374856871581024"),
                        msg='Expected {}, Recieved {}'.format(True,
                        credit_card_validator("374856871581024")))

    def test_ccv_amex_incorrect_cs_15_digits_37(self):
        """test 15 digit amex with incorrect checksum"""
        self.assertTrue(credit_card_validator("374856871581524"),
                        msg='Expected {}, Recieved {}'.format(False,
                        credit_card_validator("374856871581524")))

    def test_ccv_amex_correct_cs_16_digits_37(self):
        """test 16 digit amex with correct checksum"""
        self.assertTrue(credit_card_validator("3748568715081615"),
                        msg='Expected {}, Recieved {}'.format(False,
                        credit_card_validator("3748568715081615")))

    def test_ccv_amex_incorrect_cs_16_digits_37(self):
        """test 16 digit amex with incorrect checksum"""
        self.assertTrue(credit_card_validator("3748568715781615"),
                        msg='Expected {}, Recieved {}'.format(False,
                        credit_card_validator("3748568715781615")))

# Prefix Range Testing
    
    # Visa 16 digits

    # Above 4
    def test_ccv_visa_correct_cs_16_digits_3(self):
        """test 16 digit visa with correct checksum"""
        self.assertTrue(credit_card_validator("3052380846991740"),
                        msg='Expected {}, Recieved {}'.format(True,
                        credit_card_validator("3052380846991740")))

    def test_ccv_visa_incorrect_cs_16_digits_3(self):
        """test 16 digit visa with incorrect checksum"""
        self.assertTrue(credit_card_validator("3052380841991740"),
                        msg='Expected {}, Recieved {}'.format(True,
                        credit_card_validator("3052380841991740")))

    # Below 4
    def test_ccv_visa_correct_cs_16_digits_5(self):
        """test 16 digit visa with correct checksum"""
        self.assertTrue(credit_card_validator("5052380846990572"),
                        msg='Expected {}, Recieved {}'.format(True,
                        credit_card_validator("5052380846990572")))

    def test_ccv_visa_incorrect_cs_16_digits_5(self):
        """test 16 digit visa with incorrect checksum"""
        self.assertTrue(credit_card_validator("5052380845990572"),
                        msg='Expected {}, Recieved {}'.format(True,
                        credit_card_validator("5052380845990572")))

    # MasterCard 16 digits

    # Below 51
    # done in visa test

    # Above 54
    def test_ccv_mc_correct_cs_16_digits_gt_54(self):
        """test 16 digit mc with correct checksum"""
        self.assertTrue(credit_card_validator("6052380846990414"),
                        msg='Expected {}, Recieved {}'.format(True,
                        credit_card_validator("6052380846990414")))
    
    def test_ccv_mc_incorrect_cs_16_digits_gt_54(self):
        """test 16 digit mc with incorrect checksum"""
        self.assertTrue(credit_card_validator("6052310846990414"),
                        msg='Expected {}, Recieved {}'.format(True,
                        credit_card_validator("6052310846990414")))

    # Below 2221
    def test_ccv_mc_correct_cs_16_digits_lt_2221(self):
        """test 16 digit mc with correct checksum"""
        self.assertTrue(credit_card_validator("2220380846990758"),
                        msg='Expected {}, Recieved {}'.format(True,
                        credit_card_validator("2220380846990758")))

    def test_ccv_mc_incorrect_cs_16_digits_lt_2221(self):
        """test 16 digit mc with incorrect checksum"""
        self.assertTrue(credit_card_validator("2220310846990758"),
                        msg='Expected {}, Recieved {}'.format(True,
                        credit_card_validator("2220310846990758")))

    # Above 2720
    def test_ccv_mc_correct_cs_16_digits_gt_2270(self):
        """test 16 digit mc with correct checksum"""
        self.assertTrue(credit_card_validator("2721380846990687"),
                        msg='Expected {}, Recieved {}'.format(True,
                        credit_card_validator("2721380846990687")))
    
    def test_ccv_mc_incorrect_cs_16_digits_gt_2270(self):
        """test 16 digit mc with incorrect checksum"""
        self.assertTrue(credit_card_validator("2721310846990687"),
                        msg='Expected {}, Recieved {}'.format(True,
                        credit_card_validator("2721310846990687")))

    # Amex 15 digits

    # Below 34
    def test_ccv_amex_correct_cs_15_digits_lt_34(self):
        """test 15 digit amex with correct checksum"""
        self.assertTrue(credit_card_validator("332138084699682"),
                        msg='Expected {}, Recieved {}'.format(True,
                        credit_card_validator("332138084699682")))
    
    def test_ccv_amex_incorrect_cs_15_digits_lt_34(self):
        """test 15 digit amex with incorrect checksum"""
        self.assertTrue(credit_card_validator("332131084699682"),
                        msg='Expected {}, Recieved {}'.format(True,
                        credit_card_validator("332131084699682")))

    # Between 34 - 37
    def test_ccv_amex_correct_cs_15_digits_34_37(self):
        """test 15 digit amex with correct checksum"""
        self.assertTrue(credit_card_validator("352138084699406"),
                        msg='Expected {}, Recieved {}'.format(True,
                        credit_card_validator("352138084699406")))

    def test_ccv_amex_incorrect_cs_15_digits_34_37(self):
        """test 15 digit amex with incorrect checksum"""
        self.assertTrue(credit_card_validator("352138084899406"),
                        msg='Expected {}, Recieved {}'.format(True,
                        credit_card_validator("352138084899406")))

    # Above 37
    def test_ccv_amex_correct_cs_15_digits_gt_37(self):
        """test 15 digit amex with correct checksum"""
        self.assertTrue(credit_card_validator("382138084699491"),
                        msg='Expected {}, Recieved {}'.format(True,
                        credit_card_validator("382138084699491")))

    def test_ccv_amex_incorrect_cs_15_digits_gt_37(self):
        """test 15 digit amex with incorrect checksum"""
        self.assertTrue(credit_card_validator("382131084699491"),
                        msg='Expected {}, Recieved {}'.format(True,
                        credit_card_validator("382131084699491")))

    # my own random tests
    def all_zeros_15(self):
        """test all zeros for length 15"""
        self.assertTrue(credit_card_validator("000000000000000"),
                        msg='Expected {}, Recieved {}'.format(True,
                        credit_card_validator("000000000000000")))
        
    def all_zeros_16(self):
        """test all zeros for length 15"""
        self.assertTrue(credit_card_validator("0000000000000000"),
                        msg='Expected {}, Recieved {}'.format(True,
                        credit_card_validator("0000000000000000")))
    
    # Last Resort
    def test_1(self):
        """quick testing"""
        self.assertTrue(credit_card_validator("339582641610117"))

    def test_2(self):
        """quick testing"""
        self.assertTrue(credit_card_validator("339582641611117"))

    def test_3(self):
        """quick testing"""
        self.assertTrue(credit_card_validator("359582641610138"))

    def test_4(self):
        """quick testing"""
        self.assertTrue(credit_card_validator("359582641611138"))
    
    def test_5(self):
        """quick testing"""
        self.assertTrue(credit_card_validator("369582641610128"))
    
    def test_6(self):
        """quick testing"""
        self.assertTrue(credit_card_validator("369582641611128"))
    
    def test_7(self):
        """quick testing"""
        self.assertTrue(credit_card_validator("389582641610199"))
    
    def test_8(self):
        """quick testing"""
        self.assertTrue(credit_card_validator("389582641612199"))

    def test_9(self):
        """quick testing"""
        self.assertTrue(credit_card_validator("5097191570140418"))

    def test_10(self):
        """quick testing"""
        self.assertTrue(credit_card_validator("5097191570141418"))

    def test_11(self):
        """quick testing"""
        self.assertTrue(credit_card_validator("5697191570140248"))

    def test_12(self):
        """quick testing"""
        self.assertTrue(credit_card_validator("5697191570141248"))
    
    def test_13(self):
        """quick testing"""
        self.assertTrue(credit_card_validator("5797191570140106"))
    
    def test_14(self):
        """quick testing"""
        self.assertTrue(credit_card_validator("5797191570141106"))
    
    def test_15(self):
        """quick testing"""
        self.assertTrue(credit_card_validator("5897191570140121"))
    
    def test_16(self):
        """quick testing"""
        self.assertTrue(credit_card_validator("5897191572140121"))

    def test_17(self):
        """quick testing"""
        self.assertTrue(credit_card_validator("2121191570140118"))

    def test_18(self):
        """quick testing"""
        self.assertTrue(credit_card_validator("2121191570141118"))

    def test_19(self):
        """quick testing"""
        self.assertTrue(credit_card_validator("2211191570140358"))

    def test_20(self):
        """quick testing"""
        self.assertTrue(credit_card_validator("2211191570141358"))

    def test_21(self):
        """quick testing"""
        self.assertTrue(credit_card_validator("2220191570140340"))

    def test_22(self):
        """quick testing"""
        self.assertTrue(credit_card_validator("2220191570110340"))

    def test_23(self):
        """quick testing"""
        self.assertTrue(credit_card_validator("1221191570140184"))

    def test_24(self):
        """quick testing"""
        self.assertTrue(credit_card_validator("1221191570141184"))

    def test_25(self):
        """quick testing"""
        self.assertTrue(credit_card_validator("2820191570140211"))

    def test_26(self):
        """quick testing"""
        self.assertTrue(credit_card_validator("2820191570141211"))

    def test_27(self):
        """quick testing"""
        self.assertTrue(credit_card_validator("2780191570140110"))

    def test_28(self):
        """quick testing"""
        self.assertTrue(credit_card_validator("2780191570141110"))

    def test_29(self):
        """quick testing"""
        self.assertTrue(credit_card_validator("2721191570140088"))

    def test_30(self):
        """quick testing"""
        self.assertTrue(credit_card_validator("2721191570141088"))

# main conditional
if __name__ == "__main__":
    unittest.main()
