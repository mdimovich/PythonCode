#Have the user enter their investment amount and expected interest
# Each year their investment will increase by their investment + their investment * interest rate
# Print out earnings after a 10 year period

#Ask for the money invested & The Interest
investment = input("Enter the investment amount: ")
interest = input("Enter the interest amount: ")
#Convert value to float
investment = float(investment)
#Convert value to float and round perecentage rate by 2 digits
interest = float(interest) * .01
#Cycle through 10 years using a for loop 0-9
for i in range(10):
    investment = investment + (investment * interest)
#Output the results
print("Investment after 10 years: {:.2f}".format(investment))