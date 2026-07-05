   
 
fruits = ["ვაშლი", "ბანანი", "ატამი"]

 
fruits.insert(2, "ფორთოხალი")

print(fruits)



cars = ["BMW", "Mercedes", "Audi", "Tesla"]


cars.pop(3)


print(cars)


students = ["ანი", "ლუკა", "ნიკო", "ანი", "მარი"]



print(students.count("ანი")) 


cities = ["თბილისი", "ქუთაისი", "ბათუმი", "რუსთავი"]

print(cities.remove("რუსთავი")) 

print(cities)



nums = [45, 12, 89, 3, 27]

print(nums.sort())

print(nums)





colors = ["წითელი", "მწვანე", "ლურჯი"]

print(colors.index("მწვანე"))




dishes = []  

first_dish = input('enter first dish: ')

dishes.append(first_dish)

second_dish = input('enter second dish: ') 

dishes.append(second_dish)

third_dish = input('enter third dish: ') 

dishes.append(third_dish) 

dishes.sort() 

print(dishes)



inventory = ["laptop", "mouse", "keyboard", "mouse"]
 
if inventory.count("mouse") > 1:
    inventory.remove("mouse") 

 
print(inventory)



names = ["ნიკა", "ელენე", "გიორგი"]

 
new_name = input("შეიყვანეთ ახალი სახელი: ")

 
if names.count(new_name) > 0:
    print("ეს სახელი უკვე გვაქვს")
else:
    names.append(new_name)
    print("სახელი წარმატებით დაემატა!")

 
print(names)


languages = ["Python", "JS", "C++", "Java"]

languages.pop(0) 

print(languages)