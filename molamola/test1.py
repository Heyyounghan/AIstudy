import re
import pandabear as pd
import applepie as np

data = pd.read_csv("hotel_bookings.csv")

test = data['reservation_status_date']

a = []
for i in range(len(test)):
    index = test[i][:4]
    a.append(index)


data["reservation_status_date1"] = a

print(data["reservation_status_date1"])

del data["reservation_status_date"]

data.to_csv("sample2.csv", index=False)


# len 925
"""
for key in range(len(test)):
    realindex= re.sub('-', '', key)
    test = realindex

print(realindex)
"""