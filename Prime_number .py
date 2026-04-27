# Prime Number Checker

num = int(input("Enter a number: "))

if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print(num, "is NOT a Prime Number")
            break
    else:
        print(num, "is a Prime Number")
else:
    print("Enter a number greater than 1")
num = int(input("Enter a number: "))
# Check greater than 7
if num > 7:
    print("Number is greater than 7")
else:
    print("Enter a number greater than 7")
# Palindrome Number Checker

num = int(input("Enter a number: "))
temp = num
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

if temp == reverse:
    print(temp, "is a Palindrome")
else:
    print(temp, "is NOT a Palindrome")
