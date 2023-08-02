costPerFeet = float(0.87)

print("\n******** Welcome to fiber optic cable cost calculator ********\n")
name = input("Enter the company name: ")
feets = int(input("Enter the number of feet of fiber optic to be installed: "))

totalCost = feets*costPerFeet

print("\nThe Total Cost for installing fiber optica cable for the company",name,"is",totalCost)
