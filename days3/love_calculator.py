print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
name = name1 + name2
new_name = name.lower()

t = new_name.count("t")
r = new_name.count("r")
u = new_name.count("u")
e = new_name.count("e")
true = str(t+r+u+e)

l = new_name.count("l")
o = new_name.count("o")
v = new_name.count("v")
e = new_name.count("e")
love = str(l+o+v+e)
true_love = true+love
new_love = int(true_love)
if new_love < 10 or new_love > 90:
    print(f"Your score is {new_love}, you go together like coke and mentos.")
elif new_love >= 40 and new_love <= 50:
    print(f"Your score is {new_love}, you are alright together.")
else:
    print(f"Your score is {new_love}")

