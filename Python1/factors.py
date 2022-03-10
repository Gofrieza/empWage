value = int(input("Enter the number to print the prime factors :"))
i = 2
while(value != 1):
    rem = value % i
    if (rem == 0):
        value = value/i
        print(i)
    else:
        i = i+1
