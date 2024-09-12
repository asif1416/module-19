# Trip Expenditure
def hotelCost(nights):
    return 140*nights

#function for calculaing plane ride Cost for cities
def planeRideCost(city):
    if 'Charlotte' == city:
        return 183
    elif 'Feni' == city:
        return 220
    elif 'Cumilla' == city:
        return 200
    elif 'Chattagram' == city:
        return 350

#function for calculating the rental cost 
def rentalCarCost(days):
    if days>=7:
        return 40*days - 50
    elif days>=3:
        return 40*days - 20
    else:
        return 40*days
    

#function for calculating trip cost
def tripCost(city, days, moneySpent):
    return rentalCarCost(days) + hotelCost(days) + planeRideCost(city) + moneySpent

print('cost of car rental: ',rentalCarCost(10))

print('cost of plane ride: ',planeRideCost('Chattagram'))

print('cost of hotel room: ',hotelCost(8))

print('cost of the trip: ',tripCost('Chattagram', 7,500))


