year = int(input("Which year do you want to check? "))

if year % 400 == 0 or year % 100 != 0 and year % 4 ==0:
    print("Leap year.")
else:
    print("Not leap year.")