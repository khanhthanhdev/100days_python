print("Welcome to the tip calculator!")
price = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

pay = (price / people) *((tip+100)/100)
print(f"Each person should pay: ${round(pay,2)}")