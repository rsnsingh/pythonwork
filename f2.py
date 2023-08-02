import pandas as pd
 
import matplotlib.pyplot as plt
 
from matplotlib import style
 
style.use('fivethirtyeight')
 
country= pd.read_csv("C:/Users/home/AppData/Local/Programs/Python/Python37-32/Table106.csv",index_col=0)
 
df= country.head(5)
 
df= df.set_index(["band"])
 
sd= df.reindex(columns=["estimate1","estimate2"])
 
db= sd.diff(axis=1)
 
db.plot(kind="bar")
 
plt.show()
