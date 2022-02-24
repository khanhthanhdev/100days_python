import random
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

random_name = random.randint(0, len(names))
print(f"{names[random_name-1]} is going to buy the meal today!")
