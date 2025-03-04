def user_registration():
    # ფიქსირებული სახელები და პაროლები
    valid_username = "user123"
    valid_password = "password123"

    # მომხმარებლის შევსება
    username = input("შეიყვანეთ თქვენი სახელი: ")
    password = input("შეიყვანეთ თქვენი პაროლი: ")

    # შესვლა თუ არა სწორი მონაცემები
    if username == valid_username and password == valid_password:
        print("გილოცავთ, თქვენ წარმატებით შევსიეთ რეგისტრაცია!")
    else:
        print("მინიშნული სახელი ან პაროლი არასწორია. სცადეთ ხელახლა.")
