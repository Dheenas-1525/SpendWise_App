expense = []

print("========================================")
print("      Welcome To My Expense App         ")
print("========================================")


user = input("Enter your good name please : ")

amount = int(input("Enter the amount you spend in expense : "))
category = input("Enter the category you spend the amount (Travel, food, etc.. : )")
notes = input("Give me note for remember what u spend ur money : ")

expenses ={'amount' : amount,
           'category' : category,
           'notes' : notes}

expense.append(expenses)

print("hey {} successfully added expenses ".format(user))

print(" All Expenses ")

for exp in expense:
    print(exp)