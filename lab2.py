# Programmers: Katie, Chris, Eleni
# Course: CS151 Dr. Rajeev
# September 23, 2021
# Lab 2

secondsPerYear = 60*60*24*365
births = input("Enter the number of births per second of the population. ")
births = float(births) * secondsPerYear
deaths = input("Enter the number of deaths per second of the population. ")
deaths = float(deaths) * secondsPerYear
imms = input("Enter the number of immigrants leaving per second. ")
imms = float(imms) * secondsPerYear
pop = input("Enter the population size. ")
pop = float(pop)
years = input("Enter the desired projected years. ")
years = int(years)

pop = int(pop + (births * years) + (imms * years) - (deaths * years))
print("the population after ", years, "years is", pop, sep = " " )

print("The future predicted population is,", finalPop)







