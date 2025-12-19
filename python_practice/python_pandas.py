import pandas as pd

# series
data =pd.Series([1,2,3,4],index=['a','b','c','d'])
print(data)

# dataframe
population_dict={'beijing':3000,"shanghai":1200,'guangzhou':1800}
area_dict={'beijing':300,"shanghai":180,'guangzhou':200}
data2 = pd.DataFrame([population_dict,area_dict])
print(data2)

import numpy as np
data3 = pd.DataFrame(np.random.randint(0,100,(4,3)), index=list('abcd'),columns=list('ert'))
print(data3)
print(data3['e'])
print(data3['e']['a'])
print(data3.loc['a','t'])