import random

def find_cost():
    cost = 0
    N = int(input("How many employees there are: "))
    what_the_employees_entered = []
    for x in range(0,N):
        what_the_employees_entered.append(random.randint(4, 8))
    for x in what_the_employees_entered:
        k = 14.25*x
        cost = cost + k
    return cost

print("The total cost you must pay is " + str(find_cost()))
