# GW, Caesar Cipher Assignment

# Ask user for information
d_e = input("Do you want to (E)ncrypt or (D)ecrypt your message: ").upper()
text = input("What is the message: ")
shift = int(input("Insert the shift amount: "))


# Define the function
def encrypt(text, shift):
    everything = ""

    if d_e == "D":
        shift = -shift

    for letter in text:
        if letter.isalpha():

            # Check lowercase BEFORE using ord()
            if letter.islower():
                letter_moved = ord(letter) + shift

                # Wrap around if it goes past z
                if letter_moved > ord("z"):
                    letter_moved -= 26
                elif letter_moved < ord("a"):
                    letter_moved += 26

            # Check uppercase
            elif letter.isupper():
                letter_moved = ord(letter) + shift

                # Wrap around if it goes past Z
                if letter_moved > ord("Z"):
                    letter_moved -= 26
                elif letter_moved < ord("A"):
                    letter_moved += 26

            everything += chr(letter_moved)

        else:
            # Keep spaces and punctuation unchanged
            everything += letter

    return everything


print(f"Your message is: {encrypt(text, shift)}")
