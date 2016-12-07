#Problem: Receive Miles and Convert To Kilometers
#km = miles * 1.60934
#Enter Miles, Output 5 Miles Equals 8.04 Kilometers

miles = input ("Enter Miles: ")
#Convert miles to integer
miles = int(miles)
#Kilometer Equation
kilometers = miles * 1.60934
#Data Output
print("{} Miles equals {} Kilometers".format(miles, kilometers))