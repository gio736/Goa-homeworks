
#5) მომხმარებელს შემოატანინეთ ელფოსტის მისამართი და გადაამოწმეთ შეიცავს თუ არა '@' სიმბოლოს, შედეგი კი დაბეჭდეთ  პატარა ასოებით



name = input("please enter your email: ") 
 
if '@' in name:   
     print(name.lower()) 

else: 
    print('incorrect email')


