# GW, Loop Notes
import random
#code that will repeat over and over again

count = 1

while count <= 10:
    print(count)
    count += 1

goose = random.randint(1,11)
ducks = 1

while True:
    print("duck")
    if ducks == goose:
        break
    ducks += 1
print("GOOSE!!!!")


siblings = ["Alex", "Kaite", "Andrew", "Tia", "Treyson", "Xaiver", "Jake"]