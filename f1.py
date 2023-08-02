import pandas as pd
 
import matplotlib.pyplot as plt
 
from matplotlib import style
 
style.use('fivethirtyeight')
 
country= pd.read_csv("c:\users\home\appdata\Local\Programs\Python\Python37-32\book1.csv",index_col=0)
 
df= country.head(5)
 
df= df.set_index(["url"])
 
sd = sd.reindex(columns=['release year'])
 
#db= sd.diff(axis=1)
 
sb.plot(kind="bar")
 
plt.show()
