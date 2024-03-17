def caesar_cipher(text, shift, decrypt=False):
    result = ''
    for char in text:
        if char.isalpha():
            # Determine whether to encrypt or decrypt based on the 'decrypt' flag
            if decrypt:
                shift *= -1
            # Shift the character by the specified amount
            shifted = ord(char) + shift
            # Wrap around the alphabet if necessary
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
                elif shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26
            result += chr(shifted)
        else:
            result += char
    return result

def main():
    # Get user input
    text = input("Enter the message: ")
    shift = int(input("Enter the shift value (a positive number): "))
    # Encrypt the message
    encrypted_text = caesar_cipher(text, shift)
    print("Encrypted:", encrypted_text)
    # Decrypt the message
    decrypted_text = caesar_cipher(encrypted_text, shift, decrypt=True)
    print("Decrypted:", decrypted_text)

if __name__ == "__main__":
    main()
