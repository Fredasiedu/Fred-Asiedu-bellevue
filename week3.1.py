#print welcome message
print("*******************Welcome fiber optics Cost Calculator*****************")
#get company name from user
company_name=input("Enter your company name:")
#get number of feet from user
no_of_feet=float(input("Enter number of feet of fiber optic to be installed: "))
#initialise variable to 0 for cost and charge per feet
cost=0
charge=0
#check the number of feet and give discount as per number of feet
if(no_of_feet>100 and no_of_feet<250):
   charge=0.80
   cost=no_of_feet*charge
elif(no_of_feet>250 and no_of_feet<500):
   charge=0.70
   cost=no_of_feet*charge
elif(no_of_feet>500):
   charge=0.50
   cost=no_of_feet*charge
else:
   charge=0.87
   cost=no_of_feet*charge
#print calculations
print("*********************Calculation*******************************")
print("The number of feet:",no_of_feet)
print("Charge per feet   :$",round(charge,2))
print("Total Cost        :$",cost)
