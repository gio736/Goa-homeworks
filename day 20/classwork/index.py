  
 
name = "GIORGI" 

print(name.lower())

color = 'orange'

print(color.upper())


city = "batumi"

print(city.capitalize())


  

info = "error 404: page not found"

print(info.index("404"))


sentence = "მე მიყვარს ვაშლი და მსხალი."


print(sentence.find("ბანანი"))


word = "Programming" 


print(word.index( "r" ))



email = "student@university.ge"


print(email.index('@'))
  

url = "https://www.google.com"

print(url.startswith("https://"))


phone = "+995555123456"

print(phone.startswith("+995"))


filename = "document.pdf"

print(filename.endswith(".pdf")) 


 

word = "abracadabra" 

print(word.count("a"))


data = "100110101011"

print(data.count("1"))


#16) წარმოიდგინე, რომ მუშაობ მონაცემთა ბაზის ადმინისტრატორად და სისტემა გიბრუნებს log-ების (ჩანაწერების) დაუმუშავებელ ტექსტს. შენი მიზანია ამ ერთი ტექსტიდან საჭირო ინფორმაციის ამოღება, შემოწმება და ფორმატირება მოცემული 9 ფუნქციის გამოყენებით.

#log_record = ">ERROR: user MARIAM@COMPANY.GE failed to load the backup file. #backup #Server #backup #urgent"

 
 
  
 

log_record = ">ERROR: user MARIAM@COMPANY.GE failed to load the backup file. #backup #Server #backup #urgent"


print(log_record.startswith(">ERROR:")) 
 
 
startswidth = "True"

print("არის ეს ერორის ლოგი? - True")

log_record = ">ERROR: user MARIAM@COMPANY.GE failed to load the backup file. #backup #Server #backup #urgent"

print(log_record.endswith('#urgent'))

log_record = ">ERROR: user MARIAM@COMPANY.GE failed to load the backup file. #backup #Server #backup #urgent"

print(log_record.count("#backup"))

print(2)

log_record = ">ERROR: user MARIAM@COMPANY.GE failed to load the backup file. #backup #Server #backup #urgent"

print(log_record.index("failed"))

print(31)


log_record = ">ERROR: user MARIAM@COMPANY.GE failed to load the backup file. #backup #Server #backup #urgent"

print(log_record.index("@"))





























