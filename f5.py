import numpy as np
import pandas as pd
ser1 = pd.Series(list('abcedfghijklmnopqrstuvwxyz'))
ser2 = pd.Series(list('abcedfghijklmnopqrstuvwxyz'))
ser3 = pd.Series(np.arange(26))

# Solution 1
df = pd.concat([ser1, ser2, ser3], axis=1)

# Solution 2
df = pd.DataFrame({'col1': ser1, 'col2': ser2, 'col3':ser3})
print(df.head())
