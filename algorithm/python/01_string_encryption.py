"""
Written by: PiggyBotanist
Date: June 12, 2023

Description: 
- Given a sentence or a paragraph, this program will encrypt it and then decrypt it using a key.
- Both results after encryption and decryption will be printed to the console.
"""
import random

"""Function: shuffles the given reference into random orders to generate a key"""
def randomKeyGenerator(encryptorTemplate):
    x = 0  # Counter variable for the while loop
    output = ""  # Initialize an empty string to store the generated key

    # Iterate until x reaches the length of the encryptor template
    while x < len(encryptorTemplate):
        # Generate a random number between 0 and (len(encryptorTemplate) - 1)
        randomNumber = random.randint(0, len(encryptorTemplate) - 1)

        # Append the character at the randomly chosen position to the output string
        output += encryptorTemplate[randomNumber]

        # Remove the chosen character from the encryptor template
        # by concatenating the characters before and after the chosen position
        encryptorTemplate = encryptorTemplate[:randomNumber] + \
            encryptorTemplate[randomNumber + 1:]

        # Increment the counter
        x += 1

    return output


"""Function: Given the key, reference, and string to encrypt, output the encrypted result"""
def stringEncryptor(string, key, alphabetReference):
    output = ""
    x = 0

    # Loop through all the characters in the string, replace the character with encrypted character
    # If the character is a space, we will let it be space (This is optional)
    while x < len(string):
        if string[x] == " ":
            output = output + " "
        else:
            output = output + key[alphabetReference.find(string[x])]
        x += 1
    return output

"""Function: Given the key, reference, and string to decrypt, output the decrypted result"""
def stringDecryptor(string, key, alphabetReference):
    output = ""  # Initialize an empty string to store the decrypted string
    x = 0  # Counter variable for the while loop

    # Iterate until x reaches the length of the input string
    while x < len(string):
        if string[x] == " ":
            output = output + " "  # Preserve spaces in the decrypted string
        else:
            # Find the position of the character in the key and use it as an index
            # to retrieve the corresponding character from the alphabet reference
            decrypted_char = alphabetReference[key.find(string[x])]
            output = output + decrypted_char

        # Increment the counter
        x += 1

    # Return the decrypted string
    return output


# Define run
run = True

while run:
    # Define Reference
    alphabetReference = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!?@#$%^&*()[]{<>,./}"
    # Define Encryption Key
    key = randomKeyGenerator(alphabetReference)

    # Prompt the user, and output the references
    print("Welcome to a python program where simple encryption method will be demonstrated.")
    print("Reference: \t", alphabetReference)
    print("Key: \t\t", key)
    string = input("Please input a string you want to encrypt: ")

    # Perform encryption and decryption
    encryptedString = stringEncryptor(string, key, alphabetReference)
    decryptedString = stringDecryptor(encryptedString, key, alphabetReference)
    print("The encrypted string will be: \t", encryptedString)
    print("The decryptedString will be: \t", decryptedString)

    # Prompt the user to continue or terminate the program
    while True:
        answer = input("Would you like to continue (Y/N):")
        if answer.lower() == "y" or answer.lower() == "yes":
            run = True
            break
        elif answer.lower() == "n" or answer.lower() == "no":
            run = False
            break
        else:
            print("Sorry, this does not seem like a valid answer. Please try it again!")
