# Student Marks System

# 5 subjects marks input
m1 = int(input("Enter marks for Subject 1: "))
m2 = int(input("Enter marks for Subject 2: "))
m3 = int(input("Enter marks for Subject 3: "))
m4 = int(input("Enter marks for Subject 4: "))
m5 = int(input("Enter marks for Subject 5: "))

# Total calculate
total = m1 + m2 + m3 + m4 + m5

# Average calculate
average = total / 5

print("Total Marks:", total)
print("Average:", average)

# Grade calculate
if average >= 90:
    print("Grade: A")
elif average >= 75:
    print("Grade: B")
elif average >= 50:
    print("Grade: C")
else:
    print("Grade: Fail")
