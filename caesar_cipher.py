# GW, Caesar Cipher Assignment

# Ask user for information
d_e = input("Do you wan't to (E)ncript or (D)ecrypt your message: ")
text = input("What is the message: ")
shift = int(input("Insert the shift amount: "))

# Define the function


def encrypt(text, shift):
    for letter in text:
       if letter.isalpha():
          letter = ord(letter)
          return chr(letter + shift)
print(f"You message is {encrypt(text, shift)}")