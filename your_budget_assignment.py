# GW, Your Budget Assignment
while True:
    try:
        income = float(input("How much money do you make every month: "))
        break
    except:
        print("Numbers only.")
while True:
    try:
        rent = float(input("How much do you spend on rent or mortgage every month: "))
        break
    except:
        print('Numbers only.')
while True:
    try:
        utilities = float(input("How much are your utilities every month: "))
        break
    except:
        print("Numbers only.")
while True:
    try:
        groceries = float(input("How much do you spend on groceries every month: "))
        break
    except:
        print("Numbers only.")
while True:
    try:
        trasnportation = float(input("How much do you spend on transportation every month: "))
        break
    except:
        print("Numbers only.")
while True:
    try:
        saving = float(input("How much do you save a month: "))
        break
    except:
        print("Numbers only.")


free_money = income - (rent+utilities+groceries+trasnportation+saving)

print(f"Your rent is ${rent:.2f} and that is {int(round(rent/income*100,2))}%")
print(f"Your utilities is ${utilities:.2f} and that is {int(round(utilities/income*100,2))}%")
print(f"Your gorceries is ${groceries:.2f} and that is {int(round(groceries/income*100,2))}%")
print(f"Your transportation is ${trasnportation:.2f} and that is {int(round(trasnportation/income*100,2))}%")
print(f"You want to save ${saving:.2f} and that is {int(round(saving/income*100,2))}%")
print("You have ", free_money, "to do whatevery you want with each month")