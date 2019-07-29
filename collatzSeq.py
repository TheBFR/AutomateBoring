def collatz():
    numInput = input("Enter a number")
    if int(numInput)%2 == 0:
        print (int(numInput) // 2)
    elif int(numInput)%2 != 0:
        print (3 * int(numInput) + 1)


try:
    collatz()
except ValueError:
    print("Error: not an integer")