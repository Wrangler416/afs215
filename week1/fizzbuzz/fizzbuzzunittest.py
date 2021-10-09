import unittest
import fizzbuzz

class FirstTest(unittest.TestCase):
    
    def test_one_oneIsOne(self):
        result = fizzbuzz.findAnswer(1)
        self.assertIs(result, 1) 

    def test_two_twoIsTwo(self):
        result = fizzbuzz.findAnswer(2)
        self.assertIs(result, 2 )

    def test_isPerfect(self):
        result = fizzbuzz.perfectNumber(6)
        assert result == True
        

if __name__ == '__main__':
    unittest.main()
    
