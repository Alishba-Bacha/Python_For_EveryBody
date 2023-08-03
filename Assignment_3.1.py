def computepay(Hrs , R):

    #Condition to check if working hours exceed 40
    if Hrs > 40:
        Hrs = Hrs - 40
        pay = Hrs * R * 1.5
    else:
        pay = R * 1

    #Calculating Gross pay
    Gross_Pay = pay + Pay_1
    return Gross_Pay
Hours = input("Enter Hours")
Rate = input("Enter Rate per hour")

#Conversion to float
Hrs = float(Hours)
R = float(Rate) 
Pay_1 = R * 40

p = computepay(Hrs, R)
print("Pay" , p)