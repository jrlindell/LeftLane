#  Please draw out insights around growth, retention, user behavior, concentration, predictive behavior, etc. along with any other things you think are important to point out.
# growth, retention, user behavior, concenration, predictive behavior

import pandas as pd
import matplotlib as plt

data = pd.read_csv('Dataset.csv', nrows=100)

# 
# order, deposit, prize claimed
# what is the avg buy in amount?

data.groupby(data['transaction_type'])
# who wins the most? which state has the most winners?



## which user participates the most? which states have the most gamblers?



# value/revenue by user
data.groupby(['user_id'])['transaction_value'].count() # how many purchases by user
data.groupby(['user_id'])['transaction_value'].mean() # average transaction value by user

# avg time between transactions per user

# # of transactons, transaction value, transaction revenue by week/month. show growth over time

## transactions per month
data['transaction_timestamp'] = pd.to_datetime(data['transaction_timestamp'])
data['year'] = pd.DatetimeIndex(data['transaction_timestamp']).year
data['month'] = pd.DatetimeIndex(data['transaction_timestamp']).month

data.groupby(['year', 'month'])['state'].count() # transactions per month by year
data.groupby(['month'])['state'].count() # transactions per month by year
data.groupby(['year', 'month'])['transaction_value'].sum() # spent per month
data.groupby(['year', 'month'])['transaction_revenue'].sum() # revenue per month

# plot revenue per month
a = data.groupby(['year', 'month'])['transaction_revenue'].sum()
a.plot.bar()


# how often do users rebuy soomething?

len(data[data.groupby(['user_id'])['state'].transform('count') > 1]) / len(data) # X% of users rebought something

# state with mos rebuys

# do users usually spend small, then big? usually spend the same?

# what is the breakdown by state? are there states with more/less? better marketing in those states?
data.groupby(['state'])['transaction_revenue'].count() # number of purchases by state
data.groupby(['state'])['user_id'].nunique() # number of unique users by state
data.groupby(['state'])['transaction_value'].mean()

z = 2