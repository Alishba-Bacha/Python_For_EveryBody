# a programm which  find sum, count and average of entered numbers
# and continue even if a string is entered
x = 0
tot = 0.0

while True:
    c = input("Enter a number")
    if c == "done":
        break
    try:
        z = float(c)
    except:
        print("Invalid Input")
        continue
    print(z)
    x = x + 1
    tot = tot + z
print("All Done")
print(x, tot, tot/x)
