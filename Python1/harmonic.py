value = int(input("enter the nth term of Harmonic Number:"))
number = 0
for i in range(1, value + 1):
    number += 1 / i
print("Value of Harmonic Series is:", number)
