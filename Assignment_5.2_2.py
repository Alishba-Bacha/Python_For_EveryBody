
largest = None
smallest = None
z = 0
while z == 5:
    num = input("Enter an integer number (or 'done' to exit): ")

    if num == 'done':
        break

    try:
        num = int(num)
        if largest is None or num > largest:
            largest = num
        if smallest is None or num < smallest:
            smallest = num
    except :
        print("Invalid input. Please enter a valid integer.")
    z = z+1

if largest is not None and smallest is not None:
    print("Largest number:", largest)
    print("Smallest number:", smallest)
else:
    print("No valid numbers were entered.")
