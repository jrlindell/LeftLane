import pandas as pd
import matplotlib as plt

data = pd.read_csv('Dataset.csv', nrows=5000)

# START WITH EDA
# what is the user engagement over time?
data['transaction_timestamp'] = pd.to_datetime(data['transaction_timestamp'])
data['date'] = data['transaction_timestamp'].dt.date
data['year'] = pd.DatetimeIndex(data['transaction_timestamp']).year
data['month'] = pd.DatetimeIndex(data['transaction_timestamp']).month
data['day'] = pd.DatetimeIndex(data['transaction_timestamp']).day
a = data.groupby(['date'])['transaction_revenue'].count()
a.plot.line() #this is a little messy, so maybe if we group by month then plot

a = data.groupby(['year', 'month'])['transaction_revenue'].count()
a.plot.line()
# do line per transaction type
#########

# avg transaction value? revenue? (for both winners and orders)
data.groupby(['transaction_type'])['transaction_value'].mean()
data.groupby(['transaction_type'])['transaction_revenue'].mean()
### by state
data.groupby(['transaction_type', 'state'])['transaction_value'].mean()
data.groupby(['transaction_type', 'state'])['transaction_revenue'].mean()

# what states are most active?
data.groupby(['state'])['user_id'].count()
data.groupby(['state'])['transaction_value'].sum()

# what users are most active?
data.groupby(['user_id'])['state'].count().head(5)

# X% of users rebought something
len(data[data.groupby(['user_id'])['state'].transform('count') > 1]) / len(data) 




z = 2