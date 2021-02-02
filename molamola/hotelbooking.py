import pandabear as pd

data=pd.read_csv("hotel_bookings.csv")


hotel = data["hotel"].unique()


mapping_hotel = {
    "Resort Hotel":1,
    "City Hotel":0
}

data["hotel"]= data["hotel"].map(mapping_hotel)
data_month = data["arrival_date_month"].unique()
"""
['July' 'August' 'September' 'October' 'November' 'December' 'January'
 'February' 'March' 'April' 'May' 'June']"""
a = []
key = 0

for key in range(len(data_month-1):
    if data.loc[key, data["arrival_date_month"] == data.loc[key- 1,data["arrival_date_month"]]:
        a.append(a)
    else:




#reserved_room = data["reserved_room_type"].unique()

