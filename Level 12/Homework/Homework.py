#1)


a = 10
b = 20

if a > b:
    print("a არის მეტი")
else:
    print("b არის მეტი")


#2)


number = 7

if number % 2 == 0:
    print("რიცხვი არის ბიორზე")
else:
    print("რიცხვი არის რიცხვი")


#3)


num = -5

if num > 0:
    print("რიცხვი დადებითია")
else:
    print("რიცხვი უარყოფითია ან ნულია")


#4)


number = 5.5

if number.is_integer():
    print("ეს რიცხვი არის მთელი")
else:
    print("ეს რიცხვი არაა მთელი")


#5)


month = 6

if month in [12, 1, 2]:
    print("ზამთარი")
elif month in [3, 4, 5]:
    print("გაზაფხული")
elif month in [6, 7, 8]:
    print("ზაფხული")
else:
    print("შემოდგომა")


#6)


num = 30

if num % 10 == 0:
    print(f"{num} ეხმარება 10-ის")
else:
    print(f"{num} არ ეხმარება 10-ის")


#7)


age = 16

if age >= 18:
    print("თქვენ შეგიძლიათ ხართ უფროსი ასაკით")
else:
    print("თქვენი ასაკი არ საკმარისია")


#8)


job = "Developer"

if job == "Developer":
    print("თქვენ სამუშაოზე მიდიხართ როგორც დეველოპერი")
elif job == "Manager":
    print("თქვენ სამუშაოზე მიდიხართ როგორც მენეჯერი")
else:
    print("თქვენ გაქვთ სხვა პროფესია")


#9)


username = "admin"
password = "admin123"

if username == "admin" and password == "admin123":
    print("თქვენ წარმატებით შევდივართ სისტემაში")
else:
    print("სახელი ან პაროლი არასწორია")


#10)


x = 30
y = 25

if x > y:
    print(f"{x} დიდია {y}-ზე")
elif x < y:
    print(f"{y} დიდია {x}-ზე")
else:
    print(f"{x} და {y} იგივეა")

