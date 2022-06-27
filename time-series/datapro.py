#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# %%
df = pd.read_csv("mrrFinalInput_csv.csv")
df.head(10)
# %%
df.dtypes
#df3[df3.columns[1:4]]
# %%
#pd.to_datetime(df3[df3.columns[7:]],format="%m-%Y")
df_1 = df.copy
#%%
df_1.drop(['Unnamed'])
#%%
type(df_1)
# %%
df2 = (df.melt(['Unnamed: 0','Customer Code','Segment 1','Segment 2','Segment 3','Segment 4','Segment 5'], var_name='date')
        .assign(date = lambda x: pd.to_datetime(x['date'],errors = 'ignore'))
        .set_index('date'))

#df2.head()
# %%
df2
# %%
df2.dtypes
#%%
df2['date']
# %%
from datetime import datetime, date
df3 = (df.melt(['Unnamed: 0','Customer Code','Segment 1','Segment 2','Segment 3','Segment 4','Segment 5'], var_name='date')
        .assign(date = lambda x: pd.to_datetime(x['date'],format='%M-%d'))
        )
#%%
df3
#%%
df3['date'] = df3['date'].astype('datetime64[ns]')
#%%
df3.dtypes
#%%
df3
# %%
df3[df3['date'].isna()]

#%%

#%%
pd.Timestamp.min

# %%
from datetime import datetime, date 

df3['date'] = pd.to_datetime(df3['date'],infer_datetime_format=True,errors = 'ignore')
df3.dtypes
# %%
#Chronological Order and Equidistant Timestamps
df3 = df3.sort_values(by='date')

# Check time intervals
df3['delta'] = df3['date'] - df3['date'].shift(1)

df3[['date', 'delta']].head()
# %%
df3 = df3.drop('delta', axis=1)
df3.isna().sum()

#%%
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

import seaborn as sns # Visualization
import matplotlib.pyplot as plt # Visualization
from colorama import Fore

from sklearn.metrics import mean_absolute_error, mean_squared_error
import math

import warnings # Supress warnings 
warnings.filterwarnings('ignore')

np.random.seed(7)
# %%
sns.lineplot(x=df3['date'], y=df3['Segment 5'].fillna(0), color='darkorange', label = 'modified')
sns.lineplot(x=df3['date'], y=df3['Segment 5'].fillna(np.inf), color='dodgerblue', label = 'original')
plt.title('Fill NaN with 0', fontsize=14)
#ax[0].set_ylabel(ylabel='Volume C10 Petrignano', fontsize=14)
plt.tight_layout()
plt.show()
# %%
f, ax = plt.subplots(nrows=4, ncols=1, figsize=(15, 12))

sns.lineplot(x=df3['date'], y=df3['Segment 5'].fillna(0), ax=ax[0], color='darkorange', label = 'modified')
sns.lineplot(x=df3['date'], y=df3['Segment 5'].fillna(np.inf), ax=ax[0], color='dodgerblue', label = 'original')
ax[0].set_title('Fill NaN with 0', fontsize=14)
ax[0].set_ylabel(ylabel='Volume C10 Petrignano', fontsize=14)

mean_drainage = df3['Segment 5'].mean()
sns.lineplot(x=df3['date'], y=df3['Segment 5'].fillna(mean_drainage), ax=ax[1], color='darkorange', label = 'modified')
sns.lineplot(x=df3['date'], y=df3['Segment 5'].fillna(np.inf), ax=ax[1], color='dodgerblue', label = 'original')
ax[1].set_title(f'Fill NaN with Mean Value ({mean_drainage:.0f})', fontsize=14)
ax[1].set_ylabel(ylabel='Volume C10 Petrignano', fontsize=14)

sns.lineplot(x=df3['date'], y=df3['Segment 5'].ffill(), ax=ax[2], color='darkorange', label = 'modified')
sns.lineplot(x=df3['date'], y=df3['Segment 5'].fillna(np.inf), ax=ax[2], color='dodgerblue', label = 'original')
ax[2].set_title(f'FFill', fontsize=14)
ax[2].set_ylabel(ylabel='Volume C10 Petrignano', fontsize=14)

sns.lineplot(x=df3['date'], y=df3['Segment 5'].interpolate(), ax=ax[3], color='darkorange', label = 'modified')
sns.lineplot(x=df3['date'], y=df3['Segment 5'].fillna(np.inf), ax=ax[3], color='dodgerblue', label = 'original')
ax[3].set_title(f'Interpolate', fontsize=14)
ax[3].set_ylabel(ylabel='Volume C10 Petrignano', fontsize=14)

    
plt.tight_layout()
plt.show()
# %%
