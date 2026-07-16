  
def greet(name):
    print("Hello World!")
    print(f"Hello {name}")

greet("giorgi")  




def double(number):
    return number ** 2

 
result = double(5)
print(result)  




def checkOdd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

print(checkOdd(4))   
print(checkOdd(7))


 
def BMI(height, weight):
    return weight / (height * height)

 
my_bmi = BMI(1.80, 75)
print(my_bmi)   