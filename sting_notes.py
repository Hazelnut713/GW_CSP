# GW, String Notes
last_name = 'LaRose'
first_name = "Vienna"
# concoatenation = add two string together
name = first_name + " " + last_name
# excape char lets the progam ignore the next characyer in the string (\)
print(f'{name} told the class "You can\'t drive my car."')

user = input("Please tell me your name:\n").strip().title()

print(f"New user recognized\nWelcome {user}")

sentence = 'The quick brown fox jumped over the lazy dog.'
print(f"The sentence is {len(sentence)} characters long.")
print(sentence)
print(sentence.replace("dog", "cat"))
