import pandas as pd
import matplotlib.pyplot as plt
 
from matplotlib import style
 
style.use('fivethirtyeight')

s1= pd.DataFrame(
[ [1,1000], [2,2000], [3,3000],[4,4000],[5,5000]  ]
,columns=["column1", "column2"]
)
s1=s1.head(5)
s1= s1.set_index(["column1"])
s1.plot(kind="bar")
plt.show()
