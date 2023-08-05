largest = None
smallest = None
itr = input("Enter number of itration")
I= int(itr)
z = 0

#While loop to check all values Entered
while z < I:
    num = input("Enter a number: ")
    if num == "done":
        break
    
    z = z+1

    # Try and Except block
    try:
        x = int(num)

        # Finding largest
        if largest is None:
            largest = x
        elif x > largest:
            largest = x

        #Finding smallest
        if smallest is None:
            smallest = x
        elif x < smallest:
            smallest = x
    except:
        print("Invalid input")
        continue

#printing Largest and smallest values
print("Maximum is", largest)
print("Minimum is", smallest)

 