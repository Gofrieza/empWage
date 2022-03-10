year = int(input("Enter year to be checked:"))
if (year % 4 == 0) & (year % 100 != 0) | (year % 400 == 0):
    print("The year is a leap year", year)
else:
    print("The year is not a leap year", year)
