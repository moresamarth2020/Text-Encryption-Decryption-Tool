def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

def encryption_tool():
    print("----- TEXT ENCRYPTION & DECRYPTION -----")
    print("1. Encrypt Text")
    print("2. Decrypt Text")
    print("3. Exit")

    while True:
        choice = input("Enter choice: ")

        if choice == "1":
            text = input("Enter text to encrypt: ")
            shift = int(input("Enter shift value: "))
            print("Encrypted Text:", encrypt(text, shift))

        elif choice == "2":
            text = input("Enter text to decrypt: ")
            shift = int(input("Enter shift value: "))
            print("Decrypted Text:", decrypt(text, shift))

        elif choice == "3":
            print("Exiting tool.")
            break

        else:
            print("Invalid choice. Try again.")

encryption_tool()
