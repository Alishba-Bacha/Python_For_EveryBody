score = input("Enter Score: ")
Sc = float(score)

#Conditions to check
if Sc >= 0.9 and Sc <= 1.0:
    print("A")
elif Sc >= 0.8 and Sc < 0.9:
    print("B")
elif Sc >= 0.7 and Sc < 0.8:
    print("C")
elif Sc >= 0.6 and Sc < 0.7:
    print("D")
elif Sc <0.6 and Sc > 0:
    print("F")
else:
    print("Out of Range")
# Check
smallest_so_far = -1
for the_num in [9, 41, 12, 3, 74, 15] :
   if the_num < smallest_so_far :
      smallest_so_far = the_num
print(smallest_so_far)
#check
value = 3
smallest = None
if smallest is None :
     smallest = value
print(smallest)