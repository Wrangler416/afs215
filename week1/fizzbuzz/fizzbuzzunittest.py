# can call fizz buzz 
# gets "1" when 1 is passed in
# gets 2 when 2 is passed in
#In the fizzbuzzunittest.py file, write a code that should achieve 
# above tests through failing test, all the way to refractor. 

import unittest
import fizzbuzz

class FirstTest(unittest.TestCase):
    def test_one_stringOne(self):
        fizzbuzz.findAnswer(1) == 1
        
if __name__ == '__main__':
    unittest.main()


  


    

    
