import pandas as pd
import numpy as np

#drop header
dfTop_10000_Movies = pd.read_csv('/Users/asiyahahmad/Downloads/Top_10000_Movies.csv')
dfTop_10000_Movies.head()


to_drop = ['id',
            'revenue']
dfTop_10000_Movies.drop(to_drop, inplace=True, axis=1)

dfTop_10000_Movies.head()

dfTop_10000_Movies.drop(columns=to_drop, inplace=True)


