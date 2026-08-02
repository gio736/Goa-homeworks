
def simple_multiplication(number):
    if number % 2 == 0:
        return number * 8
    else:
        return number * 9


print(simple_multiplication(4))   
print(simple_multiplication(5))





def is_even(n):
    return n % 2 == 0

 

print(is_even(4))  
print(is_even(7))    
print(is_even(0))   




def basic_op(operator, value1, value2):
    if operator == '+':
        return value1 + value2
    elif operator == '-':
        return value1 - value2
    elif operator == '*':
        return value1 * value2
    elif operator == '/':
        return value1 / value2


print(basic_op('+', 4, 7))    
print(basic_op('-', 15, 18))  
print(basic_op('*', 5, 5))    
print(basic_op('/', 49, 7))




def bool_to_word(boolean):
    if boolean:
        return "Yes"
    else:
        return "No"


print(bool_to_word(True))    
print(bool_to_word(False))





def find_average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)    

print(find_average([1, 2, 3, 4]))  
print(find_average([]))            




