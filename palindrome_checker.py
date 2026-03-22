# Palindrome Checker

text = input("Enter a word: ")

reverse_text = text[::-1]

if text == reverse_text:
    print("It is a Palindrome")
else:
    print("It is NOT a Palindrome")
    text = input("Enter a word: ").lower()

if text == text[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")
