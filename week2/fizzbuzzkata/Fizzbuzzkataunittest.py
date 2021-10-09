import unittest 
import fizzbuzz


class Test_FizzBuzz(unittest.TestCase):
    
        def test_One_Fizzbuzz(self):
                result = fizzbuzz.findAnswer(1)
                assert result == 1

        def test_Two_Fizzbuzz(self):
                result = fizzbuzz.findAnswer(2) 
                assert result == 2

        def test_Three_Fizzbuzz(self):
                result = fizzbuzz.findAnswer(3)   
                assert result == "fizz"  

        def test_Four_Fizzbuzz(self):
                result = fizzbuzz.findAnswer(5)
                assert result == "buzz"

        def test_Five_Fizzbuzz(self):
                result = fizzbuzz.findAnswer(6)
                assert result == "fizz"
        
        def test_Six_Fizzbuzz(self):
                result = fizzbuzz.findAnswer(10)
                assert result == "buzz"

        def test_Seven_Fizzbuzz(self):
                result = fizzbuzz.findAnswer(15)
                assert result == "fizzbuzz"

    
if __name__ == '__main__':
    unittest.main()
    
