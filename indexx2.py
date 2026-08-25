
#ტერმინალის პროგრამა, რომელიც აერთიანებს მომხმარებლის ავტორიზაციას, ფინანსურ მენეჯერს, მათემატიკურ კალკულატორსა და სტატისტიკურ ანალიზატორს.
#ეტაპი 1: მომხმარებლის რეგისტრაცია და ავტორიზაცია
name = input("შეიყვანეთ სახელი: ")

surname = input("შეიყვანეთ გვარი: ")

age = int(input("შეიყვანეთ ასაკი: "))

city = input("შეიყვანეთ ქალაქი: ")

country = input("შეიყვანეთ ქვეყანა: ")

animal = input("საყვარელი ცხოველი: ")

sport = input("საყვარელი სპორტი: ")

balance = int(input("შეიყვანეთ საწყისი ბალანსი: "))


has_ticket = True

has_invitation = False


can_enter = has_ticket or has_invitation
print("ღონისძიებაზე დაშვება:", can_enter)


print(f"გამარჯობა  {name} {surname}, თქვენ ცხოვრობთ {city}, {country}-ში.")

password = ""
while password != "python123":
    password = input("შეიყვანეთ პაროლი (python123): ")
    if password == "python123":
        print("ავტორიზაცია წარმატებულია!")



#ეტაპი 1: მთავარი მენიუ (WHILE LOOP)
is_running = True

while is_running:
    print("--- მენიუ ---")
    print("1. საბანკო ოპერაციები")
    print("2. მათემატიკური ოპერაციები")
    print("3. სტატისტიკა და შეფასება")
    print("4. ციკლების ტესტი")
    print("5. გამოსვლა")

    choice = int(input("აირჩიეთ ოპერაცია (1-5): "))
#ეტაპი 2: ბანკი სისტემა
    if choice == 1:
        print(f"მიმდინარე ბალანსი: {balance}")

        withdraw = float(input("შეიყვანეთ გასატანი თანხა: "))

        if withdraw > 0:
            if withdraw <= balance:
                balance = balance - withdraw
                print(f"თანხა წარმატებით გაიტანეთ. ახალი ბალანსი: {balance}")
            else:
                print("არასაკმარისი ბალანსი")
        else:
            print("არასწორი თანხა")

        total_expenses = 0
        while True:
            expense = float(input("შეიყვანეთ ხარჯი (0 - დასრულება): "))
            if expense == 0:
                break
            if expense == 0:
                continue
            total_expenses = total_expenses + expense

        print(f"სულ დახარჯული თანხა: {total_expenses}")

#ეტაპი 3: მათემატიკური ჰაბი
    elif choice == 2:
        num1 = int(input("შეიყვანეთ პირველი რიცხვი: "))
        num2 = int(input("შეიყვანეთ მეორე რიცხვი: "))

        print(f"ჯამი: {num1 + num2}")
        print(f"სხვაობა: {num1 - num2}")
        print(f"ნამრავლი: {num1 * num2}")
        print(f"განაყოფი: {num1 / num2}")
        print(f"ნაშთი: {num1 % num2}")
        print(f"მთელზე გაყოფა: {num1 // num2}")
        print(f"ხარისხი: {num1 ** num2}")


        print(f"--- {num1}-ის გამრავლების ტაბულა ---")
        for i in range(1, 10):
            print(f"{num1} x {i} = {num1 * i}")
#ეტაპი 4: სტატისტიკა და შეფასება
    elif choice == 3:
        if age < 6:
            print("Kindergarten")
        elif age < 18:
            print("School")
        else:
            print("University or Work")


        score = int(input("შეიყვანეთ გამოცდის ქულა: "))
        if score >= 90:
            print("Grade A")
        elif score >= 70:
            print("Grade B")
        elif score >= 50:
            print("Grade C")
        else:
            print("Failed")


        if age >= 16 and age <= 60:
            print("შრომისუნარიანი ასაკი")
#ეტაპი 5: ციკლების ტესტი
    elif choice == 4:
        print("რიცხვები 20-დან 1-მდე:")
        count = 20
        while count > 0:
            print(count)
            count -= 1

        print("1-დან 50-მდე ლუწი რიცხვები:")
        for i in range(1, 50):
            if i % 2 == 0:
                print(i)

    elif choice == 5:
        print("პროგრამა დასრულდა.")
        is_running = False
    else:
        print("შენ არასწორი ციპრი აირჩიე 1დან-5")












