# Programmers: Katie, Chris, Eleni
# Course: CS151 Dr. Rajeev
# September 23, 2021
# Lab 2

# creation of input variable
births = input("Enter the number of births per second of the population. ")
# typecast to int
births = float(births)
# repetition of above processes twice
deaths = input("Enter the number of deaths per second of the population. ")
deaths = float(deaths)
immigrations = input("Enter the number of immigrants. ")
pop = input("Enter the population size. ")
pop = float(pop)
Years = input("Enter the desired projected years")
Years = int(Years)

#computations for determining population at desired projected year
DAY = pop - (Years * deaths)
DAY = float(DAY)
IAY = pop - (Years * immigrations)
IAY = float(IAY)
BAY = pop + (Years * births)
BAY = float(BAY)



