userAge = int(input("Enter your age: "))
if userAge <= 18:
        print("You are not able to vote")
else:
        userVote = input("Enter your vote food or drink:   ")
print("Your vote was suspectful")

temperature = 23
if temperature <= 15:
        print("Cold")
elif temperature > 25:
        print("Hot")
elif temperature >= 15:
        print("Warm")

password = "NikolozGOA"

UserPassword = input("enter your password:   ")
if password == UserPassword:
        print("Access Granted.")
else: 
        print("Access Denied.")