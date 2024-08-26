print("Welcome to the tip calculator!")
bill=float(input("What was the total bill? $"))
tip=input("How much tip would you like to give? 10, 12, or 15?")
people=int(input("How many people tp split the bill?"))
#total_bill=int(tip)/100*bill+bill
#print(int(total_bill)/people)
tip_as_percent=int(tip )/ 100
total_tip_amount=bill*tip_as_percent
total_bill=bill+total_tip_amount
bill_per_person=total_bill / people
final_amount=round(bill_per_person,2)
#round number to 2 decimal places python
final_amount="{:.2f}".format(bill_per_person)
print(f'Each person should pay ${ final_amount}')