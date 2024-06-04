def encrypt(shift, message):
    result = ""
    for letter in message:
        if letter.isalpha():
            ascii_offset = 65 if letter.isupper() else 97
            result += chr((ord(letter) - ascii_offset + shift) % 26 + ascii_offset)
        else:
            result += letter
    return result

def decrypt(shift, message):
    result = ""
    for letter in message:
        if letter.isalpha():
            ascii_offset = 65 if letter.isupper() else 97
            result += chr((ord(letter) - ascii_offset - shift) % 26 + ascii_offset)
        else:
            result += letter
    return result

def main():
    action = input("Would you like to encrypt or decrypt the message? (e/d): ").lower()
    message = input("Enter the message: ")
    shift = int(input("Enter the shift value: "))

    if action == 'e':
        result = encrypt(shift, message)
        print("Encrypted message:", result)
    elif action == 'd':
        result = decrypt(shift, message)
        print("Decrypted message:", result)
    else:
        print("Invalid option. Please enter 'e' to encrypt or 'd' to decrypt.")

if __name__ == "__main__":
    main()
