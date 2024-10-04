def encrypt(text, shift):
    """Function to encrypt the text using Caesar Cipher"""
    encrypted_text = ""

    for char in text:
        if char.isalpha():  # Check if character is a letter
            shift_base = 65 if char.isupper() else 97  # Uppercase letters start from ASCII 65, lowercase from 97
            encrypted_text += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            encrypted_text += char  # Non-alphabet characters remain unchanged

    return encrypted_text

def decrypt(text, shift):
    """Function to decrypt the text using Caesar Cipher"""
    decrypted_text = ""

    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            decrypted_text += chr((ord(char) - shift_base - shift) % 26 + shift_base)
        else:
            decrypted_text += char

    return decrypted_text

def main():
    print("Caesar Cipher Program")
    while True:
        print("\nOptions:")
        print("1. Encrypt a message")
        print("2. Decrypt a message")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            message = input("Enter the message to encrypt: ")
            shift = int(input("Enter the shift value (1-25): "))
            encrypted_message = encrypt(message, shift)
            print(f"Encrypted Message: {encrypted_message}")

        elif choice == '2':
            message = input("Enter the message to decrypt: ")
            shift = int(input("Enter the shift value (1-25): "))
            decrypted_message = decrypt(message, shift)
            print(f"Decrypted Message: {decrypted_message}")

        elif choice == '3':
            print("Exiting...")
            break

        else:
            print("Invalid choice! Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
