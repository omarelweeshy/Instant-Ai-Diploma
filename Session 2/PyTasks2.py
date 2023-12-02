# task1
x = int(input("Enter the number\n"))
print(abs(x))
# _______________________________________________
# task2
year = int(input("Enter the year\n"))

if year % 4 == 0:
    print("Leap year")
else:
    print("Not a leap year")
# _______________________________________________
# task3
age1 = int(input("Enter the age of the first person\n"))
age2 = int(input("Enter the age of the second person\n"))
age3 = int(input("Enter the age of the third person\n"))

if age1 > age2 and age1 > age3:
    print("first person")
elif age2 > age1 and age2 > age3:
    print("Second person")
else:
    print("Third person")
