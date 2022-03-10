import random

head = 0
tail = 0
take = int(input("enter the value:"))

for value in range(take):
    if random.randint(0, 1) == 0:
        print("head")
        head += 1

    else:
        print("Tail")
        tail += 1
print("head", head)
print("tail", tail)

percentage_of_head = ((head * 100)/take)
print("Head Occurrence Percentage is:", percentage_of_head)

percentage_of_tail = ((tail * 100)/take)
print("Tail Occurrence Percentage is:", percentage_of_tail)
