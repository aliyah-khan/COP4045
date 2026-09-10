def caesar_cipher(text, shift):
    result = ""

    # go through each character
    for i in range(len(text)):
        char = text[i]

        if char.isalpha():
            # get the alphabet position
            if char.isupper():
                start = ord("A")
            else:
                start = ord("a")

            # shift the letter and wrap around the alphabet
            new_char = chr((ord(char) - start + shift) % 26 + start)
            result += new_char
        else:
            result += char

    return result


def caesar_decipher(cyphertext, shift):
    # decrypt by shifting in the opposite direction
    return caesar_cipher(cyphertext, -shift)


def letter_frequency(text):
    frequency = {}

    # create an entry for every letter
    for i in range(26):
        letter = chr(ord("a") + i)
        frequency[letter] = 0

    # count letters in the text
    for i in range(len(text)):
        char = text[i].lower()

        if char.isalpha():
            frequency[char] += 1

    return frequency


def main():
    text = ""
    shift = 0

    while True:
        print("\n--- Caesar Cipher Menu ---")
        print("1. Enter a message")
        print("2. Enter a shift value")
        print("3. Encrypt message")
        print("4. Show letter frequency")
        print("5. Decrypt message")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            text = input("Enter your message: ")
            print("message saved.")

        elif choice == "2":
            try:
                shift = int(input("Enter the shift value: "))
                print("shift saved.")
            except ValueError:
                print("please enter an integer.")

        elif choice == "3":
            if text == "":
                print("please enter a message first.")
            else:
                encrypted = caesar_cipher(text, shift)
                print("encrypted text:", encrypted)

        elif choice == "4":
            if text == "":
                print("please enter a message first.")
            else:
                frequency = letter_frequency(text)
                print("letter frequency:")

                for letter in frequency:
                    print(letter + ":", frequency[letter])

        elif choice == "5":
            if text == "":
                print("please enter a message first.")
            else:
                encrypted = caesar_cipher(text, shift)
                decrypted = caesar_decipher(encrypted, shift)
                print("encrypted text:", encrypted)
                print("decrypted text:", decrypted)

        elif choice == "6":
            print("goodbye!")
            break

        else:
            print("invalid choice. please try again.")


if __name__ == "__main__":
    main()
