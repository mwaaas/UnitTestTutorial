'''
Created on Jan 3, 2014

@author: mwas
'''
import  unittest
import random
import even


class evenCheck(unittest.TestCase):
    def test_even(self):
        #"""find_even should always return True for numbers divisible by 2"""
        random_integer = random.randint(0,1000)
        a = random_integer/2.0
        self.assertEqual((a == int(a)),even.find_even(random_integer), "wrong answer for "+str(random_integer))


        
class test_input(unittest.TestCase):
    
    
        
    def test_nonInteger(self):
        "find_even should only accept integers only"
        l = ['a','2.0']
        for a in l:
            self.assertRaises(even.NonIntegerError, even.find_even, a )
    
if __name__ == "__main__":
    unittest.main()
        
        
        
        
        