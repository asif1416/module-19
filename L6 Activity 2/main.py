# Random date and time
import random
import time

def getRandomDate(startDate, endDate):
    print("Printing random date between", startDate, 'and', endDate)
    randomGenerator = random.random()
    dateFormat = '%d/%m/%Y'

    startDate = time.mktime(time.strptime(startDate, dateFormat))
    endDate = time.mktime(time.strptime(endDate, dateFormat))

    randomTime = startDate + randomGenerator * (endDate - startDate)
    randomDate = time.strftime(dateFormat, time.localtime(randomTime))

    return randomDate
print('Random date is ',getRandomDate("1/2/2011", "1/2/2021"))


