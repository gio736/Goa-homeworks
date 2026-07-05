 
# .append() — სიის ბოლოში ამატებს ახალ ელემენტს.
# .insert() — სიის კონკრეტულ ადგილას (ინდექსზე) ჩასვამს ელემენტს.
# .pop() — სიიდან შლის ელემენტს (თუ ინდექსს არ მივუთითებთ, შლის სულ ბოლოს).

 
 
colors = ["red", "green", "blue", "yellow", "purple"]


colors.pop(4)

print(colors)


animals = ["dog", "cat", "elephant", "lion"]

animals.insert(2,"monkey")

print(animals)


items = ["pen", "penciil", "ereicer"]

print(len(items)) 

 

nums = []


num1 = input("enter the first num:")

nums.append(num1)

num2 = input("enter the second num:")

nums.append(num2)

num3 = input("enter thr third num:")

nums.append(num3)

num4 = input("enter thr  fourth num:")

nums.append(num4)

num5 = input("enter thr  fifth num:")

nums.append(num5)
 
print(nums)  

 

students = []

 
student1 = input('enter first student name: ')  

students.append(student1)

student2 = input('enter second student name: ')

students.append(student2)

student3 = input('enter thirt student name: ')

students.append(student3) 

  

students.insert(0,"Teacher") 


students.pop()


print(len(students)) 
print(students)





 