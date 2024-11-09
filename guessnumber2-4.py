import random

n = random.randint(0, 100)
#print(n)
i = 0
while True:
    x = int(input("Guessing number: "))
    i += 1
    if x == n :
        print("Congratulations!")
        print("your attempts is: ", i)
        break
    elif x > n:
        print("Try Again! You guessed too high")
    else:
        print("Try Again! You guessed too small")
