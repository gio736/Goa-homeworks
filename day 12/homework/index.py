
number = 15

if number > 10:
    print("more than 10")
else:
    print("less than 10")


user_num = int(input("enter number: "))

if user_num == 15:
    print("equal to 15")
else:
    print("not equal to 15")



user_string = input("enter  string: ")

if user_string == "group92":
    print("you are correct")
else:
    print("you are wrong")


 
for i in range(50, 100, 5):
    print(i)

 

name = "Giorgi" 
surname = " dolidze " 


for  i in name:
    print(i)

for i in surname:
    print(i)






 
i = 20
while i < 50:
    print(i)
    i += 1 


 
for i in range(0, 100):
    print(i)

 
i = 0
while i < 100:
    print(i)
    i +=  1

 
for i in range(0, 101):
    print(i)

 
i = 0
while i <= 100:
    print(i)
    i += 1


 
for i in range(10, 20):
    print(i)

 
i = 10
while i < 20:
    print(i)
    i += 1


  
for i in range(100, 201, 5):
    print(i)
 
i = 100
while i <= 200:
    print(i)
    i += 5


 
for i in range(10, -1, -1):
    print(i)

 
i = 10
while i >= 0:
    print(i)
    i -= 1


num = float(input("enter number : "))

if num > 0:
    print("This number is a positive number")
elif num < 0:
    print("This number is a negative number")
else:
    print("This number is zero")



age = int(input("შემოაყვანეთ თქვენი ასაკი: "))

if age < 0:
    print("არასწორი ინფო")
elif age <= 12:
    print("ბავშვი ხარ")
elif age <= 19:
    print("მოზარდი/თინეიჯერი ხარ")
elif age <= 64:
    print("ზრდასრული ხართ")
elif age <= 120:
    print("ხანში შესული ხართ")
else:
    print("გურუ ან ჯადოქარი")



num1 = float(input("შემოიტანეთ პირველი რიცხვი: "))
num2 = float(input("შემოიტანეთ მეორე რიცხვი: "))
num3 = float(input("შემოიტანეთ მესამე რიცხვი: "))

 
largest = max(num1, num2, num3)

print("უდიდესი რიცხვია:", largest)


day = int(input("შემოიტანეთ რიცხვი 1-დან 7-ის ჩათვლით: "))

if day == 1:
    print("ორშაბათი")
elif day == 2:
    print("სამშაბათი")
elif day == 3:
    print("ოთხშაბათი")
elif day == 4:
    print("ხუთშაბათი")
elif day == 5:
    print("პარასკევი")
elif day == 6:
    print("შაბათი")
elif day == 7:
    print("კვირა")
else:
    print("არ ვიცი ეგ რა დღეა")




num = float(input("შემოიტანეთ რიცხვი: "))

if num > 50:
    print(num * 5)
else:
    print(num ** 2) 



password = input("შემოიტანეთ პაროლი: ")

if password == "goa123":
    print("Password is correct!")
else:
    print("Incorrect password!")


limit = int(input("შემოიტანეთ რიცხვი: "))
total_sum = 0
 
for i in range(1, limit + 1):
    total_sum += i
print("1-დან თქვენს რიცხვამდე ყველა ციფრის ჯამია:", total_sum)
 


for ticket in range(1, 5001):
    if ticket == 2024:
        print("ჯეკპოტი! მომგებიანი ბილეთი ნაპოვნია")
        break   


for num in range(1, 301):
    if num % 4 == 0 and num % 7 == 0:
        print("პირველივე რიცხვი, რომელიც იყოფა 4-ზეც და 7-ზეც არის:", num)
        break 



for i in range(1, 51):
    if i % 10 == 0:
        continue 
    print(i)

 
 