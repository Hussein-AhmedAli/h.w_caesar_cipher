def caesar_decrypt(text):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for shift in range(1, 26):
        result = ''
        for char in text:
            if char in alphabet:
                index = (alphabet.index(char) - shift) % 26
                result += alphabet[index]
            else:
                result += char
        print(f'Shift {shift}: {result}')

text = input("Enter encrypted text: ")
caesar_decrypt(text)
