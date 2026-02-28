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

if num > 7:
    print("Number is greater than 7")
else:
    print("Enter a number greater than 7")
