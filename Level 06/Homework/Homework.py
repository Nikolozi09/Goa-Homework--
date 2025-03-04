#2)

a = int(input("Enter Number: "))
b = int(input("Enter Number: "))
c = int(input("Enter Number: "))

print(a + b + c)
print(a - b - c)
print(a * b * c)
print(a / b / c)

#3)

name = input("Enter Your Name: ")
last_name = input("Enter Your Last name: ")
print(f"My name is {name} and my last name is {last_name}")

#4)

#მომხმარებელს ვეკითხებით რომ შემოიტანოს სიტყვა
string = input("Enter word: ")
#მომხმარებლის შემოტანილ მნიშვნელობას ვამრავლებთ 5-ზე
string *= 5

#მომხმარებელს ვეკითხებით რომ შემოიტანოს რიცხვი
num = int(input("Enter number: "))
#მომხმარებლის შემოტანილ მნიშვნელობას ვამრავლებთ 5-ზე
num *= 5

#ვბეჭდავთ ორივე ცვლადს
print(string,num)