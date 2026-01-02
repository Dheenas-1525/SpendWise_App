expenses = []
print("==============================================")
print("     Welcome To My SpendWide Application      ")
print("==============================================")

user = input("Enter your good name please .... : ")

amount = int(input("Hey {} Enter Your Amount : ".format(user)))

category = input("Enter your category spend money (food , travel , etc..) : ")

note = input("\nEnter note for your reminder what spend your money : ")

expense = {
    "amount" : amount,
    "category" : category,
    "note" : note

}


expenses.append(expense)

print("\nHey {} All expenses added to be succesfully".format(user))


print("all expenses : ")


for exp in expenses:
    print(exp)