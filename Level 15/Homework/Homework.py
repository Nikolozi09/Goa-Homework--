number1 = int(input("Print any number: "))
number2 = int(input("Print one more number: "))
while True:
    magaliti = int(input("how you want to interact with this numbers?(1.plus 2.minus 3.multiple 4.division): "))
    if magaliti == 1:
        print(number1,"+", number2, "=", number1 + number2)
    elif magaliti == 2:
        print(number1,"-", number2, "=", number1 - number2)
    elif magaliti == 3:
        print(number1,"*", number2, "=", number1 * number2)
    elif magaliti == 4 and number2 != 0:
        print(number1,"/", number2, "=", number1 / number2)
    elif magaliti == 4 and number2 == 0:
        print("You cant division with 0")