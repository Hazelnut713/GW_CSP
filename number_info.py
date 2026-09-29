# GW, Number Information Assignment

for number in range(1,21):
    if number%2 == 0:
        if number%5 == 0:
            print(f"{number} is even and divisable by 5")
        else:
            print(f"{number} is even and not divisable by 5")
    else:
         if number%5 == 0:
                print(f"{number} is odd and divisable by 5")
         else:
                print(f"{number} is odd and not divisable by 5")