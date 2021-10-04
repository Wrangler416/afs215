import unittest
import fizzbuzz

class FirstTest(unittest.TestCase):
    
    def test_one_oneIsOne(self):
        result = fizzbuzz.findAnswer(1)
        self.assertIs(result, 1) 
        self.assertIs(result, 2 )

    def test_two(self):
        assert 1 == 1
        
         
if __name__ == '__main__':
    unittest.main()
    
