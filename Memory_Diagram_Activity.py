# GW, Memory Diagram Activity

name = "Alex"
age = 14

score = 10

height = 5.9
city = "Denver"
zip_code = 80202

price1 = 10
price2 = 10

print(f"Your name is {name} and it is saved at {id(name)}")
print(f"Your age is {age} and it is saved at {id(age)}")

print(f"Your score is {score} and it is saved as {id(score)}")
score = 25
print(f"Your score is {score} and it is saved at {id(score)}")

print(f"You are {height} and it is saved at {id(height)}")
print(f"Your city is {city} and it is saved at {id(city)}")
print(f"Your zip code {zip_code} and it is saved at {id(zip_code)}")

print(f"The price is {price1} and it is saved at {id(price1)}")
print(f"The price is {price2} and it is saved at {id(price2)}")