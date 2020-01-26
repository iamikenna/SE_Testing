"""
Author: Ikenna Ibezim
Write a program to classify triangles
"""

def classify_triangle(a,b,c): #The 3 parameters represent the length of the traingles
    """
    equilateral triangles have all three sides with the same length
    isosceles triangles have two sides with the same length
    scalene triangles have three sides with different lengths
    right triangles have three sides with lengths, a, b, and c where a2 + b2 = c2
    """
    if a == b and b == c and a == c: #Checking for Equilateral triangles
        return "Equilateral"
    elif ( a ** 2 + b ** 2) == c ** 2: #Checking for Right triangles
        return "Right"
    elif a == b and a != c and b != c: #Checking for Isoscles triangles
        return "Isosceles"
    elif a != b and a == c and b != c: #Checking for Isoscles triangles
        return "Isosceles"
    elif a != b and b == c and a != c: #Checking for Isoscles triangles
        return "Isosceles"
    elif a != b and a != c and b != c: #Checking for Scalene triangles
        return "Scalene"
    # else:
    #     return "NotATriangle"
           
def main():
    """
    Test cases
    """  
    print(classify_triangle(3,4,5))
    print(classify_triangle(3,44,5))
    print(classify_triangle(1,1,1))
    print(classify_triangle(10,10,40))
    print(classify_triangle(10,15,30))
    
if __name__ == "__main__":
    main()          
            
    
