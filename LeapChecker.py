year_check = int(input("Enter the year to be checked for leap year"))

if year_check %100 !=0 and year_check %4 ==0:
    print("This year is a leap year!")
elif year_check %400 ==0:
    print("This year is a leap year!")
else:
    print("Not a leap year.")
