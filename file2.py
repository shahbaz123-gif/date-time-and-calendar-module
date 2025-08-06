import random
import time

def getRandomDate(startDate, endDate):
    print("Printing random date between", startDate, "and", endDate)
    
    
    
    # Generate a random float between 0 and 1
    randomGenerator = random.random()
    
    dateFormat = "%m/%d/%Y"
    
    # Convert start and end dates to time in seconds
    startTime = time.mktime(time.strptime(startDate, dateFormat))
    endTime = time.mktime(time.strptime(endDate, dateFormat))
    
    # Calculate a random time between start and end
    randomTime = startTime + randomGenerator * (endTime - startTime)
    
    # Convert random time back to readable date format
    randomDate = time.strftime(dateFormat, time.localtime(randomTime))
    
    return randomDate

# Call the function
print("Random date =", getRandomDate("1/1/2016", "12/12/2018"))

