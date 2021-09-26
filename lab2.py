# Programmers: Katie, Chris, Eleni
# Course: CS151 Dr. Rajeev
# September 23, 2021
# Lab 2
# test
# creation of input variable
births = input("Enter the number of births per second of the population. ")
# typecast to float
births = float(births)
# repetition of above processes twice
deaths = input("Enter the number of deaths per second of the population. ")
deaths = float(deaths)
imms = input("Enter the number of immigrants leaving per second. ")
immigrations = float(imms)
pop = input("Enter the population size. ")
pop = float(pop)
years = input("Enter the desired projected years. ")
years = int(years)
# calculation of deaths after # of years is below;
deaths *= 60  # seconds to minutes
deaths *= 60  # minutes to hours
deaths *= 24  # hours to days
deaths *= 365  # days to years
deaths *= years  # years to number of years later
# calculation of immigrations after # of years is below;
imms *= 60
imms *= 60
# computations for determining population at desired projected year
DAY = pop - (years * deaths)
DAY = float(DAY)
IAY = pop - (years * imms)
IAY = float(IAY)
BAY = pop + (years * births)
BAY = float(BAY)
finalPop = (pop - (DAY + IAY) + BAY)
finalPop = float(finalPop)
print ("the population after ", years, "years is", finalPop, sep = " " )

# births after so many years: births per second * 60 = minute * 60 = hour * 24 = day * 365 = year * years#
# deaths after so many years: deaths per second * 60 = minute * 60 = hour *24 = day * 365 = year * years#
# immigrants after so many years: imm. per second * 60 = minute * 60 = hour * 24 = day * 365 = year * years#



