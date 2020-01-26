"""
Author: Ikenna Ibezim
Write a program to classify triangles
Test cases for HW1
"""
import unittest
from HW_1_Ikenna_Ibezim_ST import classify_triangle

""" Iteration test for all functions"""

class TestTriangles(unittest.TestCase):

    def test_classify_triangles(self):
        """
        Testing classify triangles by comparing the program's output with the expected output
        """
        self.assertEqual(classify_triangle(1,1,1) , "Equilateral")
        self.assertEqual(classify_triangle(10,15,30) , "Scalene")
        self.assertEqual(classify_triangle(3,4,5) , "Right")
        self.assertEqual(classify_triangle(3,4,4) , "Isosceles")
        self.assertNotEqual(classify_triangle(3,4,4) , "Right")
        self.assertNotEqual(classify_triangle(1,1,1) , "Scalene")
        self.assertNotEqual(classify_triangle(10,15,30) , "Isoceles")
        self.assertNotEqual(classify_triangle(3,4,5) , "Scalene")

if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)


"""
    Deliverable 3:

1. The first encounter i had was thinking about how to test the code,
    writing the code was easy but thinking of testing it was abit confusing 
    until i found a way.

2. The requirements were very helpful and helped me position and structure my
    code in the right direction, but not everything was specified

3. I didn't encounter any challenges with the tools, I love unittest

4. 
    * I realised i was done when i exhausted all test cases by comparing all 
    expected outputs with the programs output and everything checked out  
    * I also tested for wrong inputs and wrong outputs making sure my program is 
    able to identify every triangle given to the program E.g 3,4,5 is a 
    right angle triangle

    * I used the Unittest and checked the equality with the expected output and 
    program output
    * I also checked for unequal outputs and made sure my program doesnt give 
    the wrong triangle name as an answer

    
    LAstly I tried several times to break the code and each time i was able to break
    the code i was also able to fix it and run a new test case to make sure it works

"""


