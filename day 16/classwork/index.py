 
numbers = [10, 20, 30, 40, 50, 60, 70]

print(numbers[0:3]) 

  


colors = ["წითელი", "მწვანე", "ლურჯი", "ყვითელი", "შავი"]

print(colors[-1])

print(colors[-2])

 

short_nums = [1,2,3,4,90,8,72,31,74]


for i in short_nums:
     print (i)





text = "Hello, World!"
print(text[7])
print(text[8])
print(text[9])
print(text[10])
print(text[11])
 


short_nums = [1, 2, 3, 4, 90, 8, 72, 31, 74]

 
total_sum = 0

 
for num in short_nums:
    total_sum += num  

 
print("The sum of the numbers is:", total_sum) 


  

get_highets = [90, 81, 100, 23, 3, 98, 102, 90, 75]

max_num = get_highets[0]

for num in get_highets:
    if num > max_num:
        max_num = num   

print("The largest number is:", max_num)
