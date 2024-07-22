''' Assignment_5
Question:- write a function called max_of_three that takes three parameters as inputs and returns the largest of the three. The function should use conditional statements to compare the values and determine the greatest.  
-Ensure that your function handles edge cases, such as when two or more numbers are equal.'''


def max_of_three(a,b,c):
    
    if a >= b and a >=c:
        print(a)
        
    elif b >= a and b >= c:
        print(b)
    
    else:
        print(c)        
        
max_of_three(4,4,10)
max_of_three(10,4,10)
max_of_three(20,20,20)

print("hello world")

def max_of_three(x,y,z):
    
    if x >= y and x >= z:
        print(x)
        
    elif y >= x and y >= z:
        print(y)
        
    else:
        print(z)


max_of_three(20,25,20)
max_of_three(3,4,50)
max_of_three(44,44,30)