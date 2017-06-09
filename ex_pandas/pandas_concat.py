from __future__ import print_function
import pandas as pd
import numpy as np

# concatenating
# ignore index
df1 = pd.DataFrame(np.ones((3,4))*0, columns=['a', 'b', 'c', 'd'])
df2 = pd.DataFrame(np.ones((3,4))*1, columns=['a', 'b', 'c', 'd'])
df3 = pd.DataFrame(np.ones((3,4))*2, columns=['a', 'b', 'c', 'd'])
res = pd.concat([df1, df2, df3], axis=0, ignore_index=True)
print(res)

#join, ('inner', 'outer')
df1_1 = pd.DataFrame(np.ones((3, 4))*0, columns=['a', 'b', 'c', 'd'], index=[1, 2, 3])
df2_1 = pd.DataFrame(np.ones((3, 4))*1, columns=['b', 'c', 'd', 'e'], index=[2, 3, 4])
res1 = pd.concat([df1_1, df2_1], axis=0, join='outer', ignore_index=True)
print(res1)
res2 = pd.concat([df1_1, df2_1], axis=0, join='inner', ignore_index=True)
print(res2)
res3 = pd.concat([df1_1, df2_1], axis=1, join='outer', ignore_index=True)
print(res3)
res4 = pd.concat([df1_1, df2_1], axis=1, join='inner', ignore_index=True)
print(res4)
res5 = pd.concat([df1_1, df2_1], axis=1, join_axes=[df1_1.index])
print(res5)

#append
df1_2 = pd.DataFrame(np.ones((3, 4))*0, columns=['a', 'b', 'c', 'd'])
df2_2 = pd.DataFrame(np.ones((3, 4))*1, columns=['a', 'b', 'c', 'd'])
df3_2 = pd.DataFrame(np.ones((3, 4))*1, columns=['b', 'c', 'd', 'e'], index=[2, 3, 4])
res6 = df1.append(df2_2, ignore_index=True)
print(res6)
res7 = df1.append([df2_2, df3_2])
print(res7)
s1 = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
res8 = df1_2.append(s1, ignore_index=True)
print(res8)