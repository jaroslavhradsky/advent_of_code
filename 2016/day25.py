import numpy as np
import math
import datetime as dt



np.array([a+b for ])






quit()



birthday = dt.datetime(1981,4,10)
today = dt.datetime.today()


count = 0
for i in range (0, (today-birthday).days+1):
    day = birthday + dt.timedelta(days=i)
    if day.weekday() == 4 and day.day == 13: 
        count += 1
        print(day.date())
print(count)
