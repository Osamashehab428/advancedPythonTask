print("Enter your monthly income")
monthtlyincome = input()
print("")

print("Enter your expsenes")
expenses = input()

monthlysavings = int(monthtlyincome) - int(expenses)
ProjectedSavings = (int(monthlysavings) * 12)  
+ int((monthlysavings) * 12 * 0.05)

print("Your monthly savings are: ", monthlysavings)
print("")
print("Projected savings after one year, with interest, is: "
      ,ProjectedSavings)
