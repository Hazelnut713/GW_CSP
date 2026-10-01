# GW, Caesar Cipher Assignment

# Ask user for information
d_e = input("Do you wan't to (E)ncript or (D)ecrypt your message: ").upper()
text = input("What is the message: ")
shift = int(input("Insert the shift amount: "))

# Define the function


def encrypt(text, shift):
    everything = ""
    if d_e == "D":
       shift = -shift
    if d_e == "E":
       shift = shift
    for letter in text:
       if letter.isalpha():
          letter = ord(letter)
          letter_moved = letter + shift
          if letter.islower():
             for i in range(ord('a'), ord('z') +1):
                print(chr(i), end= " ")
          if letter.isupper():
             for i in range(ord('A'), ord("Z") + 1):
                print(chr(i), end=" ")
          everything += chr(letter_moved)
       else:
          everything += letter
    return everything

print(f"You message is {encrypt(text, shift)}")