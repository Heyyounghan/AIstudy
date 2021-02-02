import pandabear as pd
import applepie as np


dt = pd.read_csv("realhotel.csv")
#print(dt.isnull().sum())
# country 488 / agent 16340 /company 112593 / children 4
dt["country"] = dt["country"].fillna("PRT")
print(dt["country"].isnull().sum())

# print(dt["agent"].value_counts())
'''9.0      31961
240.0    13922
1.0       7191
14.0      3640
7.0       3539
         ...  
213.0        1
433.0        1
197.0        1
367.0        1
337.0        1
'''
dt["agent"] = dt["agent"].fillna(9)
# print(dt["agent"].isnull().sum())
dt["company"] = dt["company"].fillna(40)
#print(dt["company"].isnull().sum())
dt["children"] = dt["children"].fillna(0)
print(dt["children"].isnull().sum())

dt.to_csv("realhotel2.csv")