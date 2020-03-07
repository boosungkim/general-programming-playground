import time

#The GMT
seconds = round(time.time()%60)
minuteS = time.time()//60
minutes = round(minuteS%60)
hourS = minuteS//60
hours = round(hourS%24)

#The Korean time
hoursK = round((hourS + 9)%24)

#The GMT date
dayS = hourS//24
days = round(dayS%7)

#The Korean date
daySK = (hourS + 9)//24
daysK = round((dayS)%7)


#ADD THE 0 IN FRONT
#The GMT clock
print("The current Greenwich Mean Time is " + str(hours) + ":" + str(minutes) + ":" + str(seconds))
daysofW = {"Monday":4 , "Tuesday":5 , "Wednesday":6 , "Thursday":7 , "Friday":1 , "Saturday":2 , "Sunday":3 }
for a, b in daysofW.items():
    if b == days:
        print(a)
print("")

#The Korean clock
print("The current Korean time is " + str(hoursK) + ":" + str(minutes) + ":" + str(seconds))
daysofWK = {"Monday":4 , "Tuesday":5 , "Wednesday":6 , "Thursday":7 , "Friday":1 , "Saturday":2 , "Sunday":3 }
for a, b in daysofWK.items():
    if b == daysK:
        print(a)
print("")

#Since Epoch
print("It has been " + str(int(dayS)) + " days since Epoch (1970-01-01).")

#Try that math trick for this
