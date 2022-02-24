import random

# random_int = random.randint(1, 10)
# print(random_int)
# print('Random number from 0 to 1 :', random.random())
# print('Uniform Distribution between [1,5] :', random.uniform(1, 5))
# print('Gaussian Distribution with mean = 0 and standard deviation = 1 :', random.gauss(0, 1))
# print('Exponential Distribution with lambda = 0.1 :', random.expovariate(0.1))
# print('Normal Distribution with mean = 1 and standard deviation = 2:', random.normalvariate(1, 5))

states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine",
                     "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
 
dirty_dozen = [fruits, vegetables]
print(dirty_dozen)
print(dirty_dozen[1][1])