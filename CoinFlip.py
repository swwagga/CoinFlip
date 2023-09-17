import random

def flip():
    result = random.randrange(2)

    if result == 0:
        print("Heads")
    else:
        print("Tails")

for x in range(0, 1):
    flip()