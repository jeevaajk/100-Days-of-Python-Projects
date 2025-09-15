#A program to give the bill amount with the tip 
bill=float(input("Enter the total bill : "))
tip=int(input("Enter Your tip Percentage : "))
total_tip=tip/100
total_bill=bill*total_tip+bill
print("The total bill Amount is $ ",round(total_bill,2),"Only Sir !")
print("Thank You for Purchasing !")