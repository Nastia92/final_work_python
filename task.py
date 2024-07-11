import pandas as pd
import random

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

one_hot = pd.DataFrame(index=data.index)

for category in data['whoAmI'].unique():
    one_hot.loc[:, category] = (data['whoAmI'] == category).astype(int)

data = data.join(one_hot)

print(data.head())