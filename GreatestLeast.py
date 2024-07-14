number_1 = int(input("Enter a number: "))
number_2 = int(input("Enter a number: "))
number_3 = int(input("Enter a number: "))

if number_1 > number_2 and number_1 > number_3:
    print("The first number is the greatest!")
elif number_2 > number_3 and number_2 > number_1:
    print("The second number is the greatest!")
elif number_3 > number_1 and number_3 > number_2:
    print("The third number is the greatest!")

if number_1 < number_2 and number_1 < number_3:
    print("The first number is the least!")
elif number_2 < number_3 and number_2 < number_1:
    print("The second number is the least!")
elif number_3 < number_1 and number_3 < number_2:
    print("The third number is the least!")
    