import pandas as pd
import matplotlib.pyplot as plt
import datetime

print('started download')
data = pd.read_csv('/Users/footb/Downloads/Dataset.csv')
print('completed download')
data.head(5).to_csv('outputs/head.csv')

# START WITH EDA
# what is the user engagement over time?
data['transaction_timestamp'] = pd.to_datetime(data['transaction_timestamp'])
data['date'] = data['transaction_timestamp'].dt.date

#month_gb = data.groupby(['year', 'month'])['transaction_revenue'].sum().reset_index(name = 'revenue')

fig, axs = plt.subplots(figsize=(11.5,4))
data.groupby(['date'])['transaction_revenue'].sum().plot(kind='line')
plt.xlabel('Date')
plt.ylabel('Revenue ($)')
plt.savefig('plots/transaction_revenue_over_time.png')

### zoomed in
fig, axs = plt.subplots(figsize=(11.5,4))
a = data[data['date'] >= datetime.date(2021, 1, 1)]
a.groupby(['date'])['transaction_revenue'].sum().plot(kind='line')
plt.xlabel('Date')
plt.ylabel('Revenue ($)')
plt.savefig('plots/transaction_revenue_over_time_zoomed.png')


# do line per transaction type
#########
a = data.groupby(['date', 'transaction_type'])['transaction_revenue'].sum().reset_index(name = 'revenue')
fig, ax = plt.subplots(figsize=(11.5, 4))
for type in list(a['transaction_type'].unique()):
    ax.plot(a[a.transaction_type==type].date, a[a.transaction_type==type].revenue,label=type)
plt.xlabel('Date')
plt.ylabel('Revenue ($)')
plt.legend()
plt.savefig('plots/transaction_revenue_over_time_by_type.png')

### zoomed
t = data[data['date'] >= datetime.date(2021, 1, 1)]
a = t.groupby(['date', 'transaction_type'])['transaction_revenue'].sum().reset_index(name = 'revenue')
fig, ax = plt.subplots(figsize=(11.5, 4))
for type in list(a['transaction_type'].unique()):
    ax.plot(a[a.transaction_type==type].date, a[a.transaction_type==type].revenue,label=type)
plt.xlabel('Date')
plt.ylabel('Revenue ($)')
plt.legend()
plt.savefig('plots/transaction_revenue_over_time_by_type_zoomed.png')

# avg transaction value? revenue? (for both winners and orders)
a = data.groupby(['date', 'transaction_type'])['transaction_revenue'].sum().reset_index(name = 'revenue')
a.boxplot(column=['revenue'], by='transaction_type')
plt.savefig('plots/revenue_box.png')

b = data.groupby(['date', 'transaction_type'])['transaction_value'].sum().reset_index(name = 'value')
b.boxplot(column=['value'], by='transaction_type')
plt.savefig('plots/value_box.png')

### by state
a = data.groupby(['state'], as_index=True)['transaction_revenue'].sum().reset_index(name = 'revenue')
a.set_index(['state']).plot(kind='bar', xlabel='State', ylabel='Revenue ($)', legend=False)
plt.savefig('plots/revenue_state.png')

b = data.groupby(['state'], as_index=True)['transaction_value'].sum().reset_index(name = 'value')
b.set_index(['state']).plot(kind='bar', xlabel='State', ylabel='Value ($)', legend=False)
plt.savefig('plots/value_state.png')



# what states are most active?
a = data.groupby(['state'])['user_id'].count()
a.to_csv('outputs/state_count.csv')
a = data.groupby(['state'])['transaction_revenue'].sum()
a.to_csv('outputs/state_revenue.csv')


# what states win the most?
a = data[data['transaction_type'] == 'Prize claimed'].groupby(['state'])['transaction_revenue'].count()
a.to_csv('outputs/state_wins.csv')

# X% of users rebought something
t = len(data[data.groupby(['user_id'])['state'].transform('count') > 1]) / len(data) * 100
print(t, "% of users re-played")

# growth over time by state

a = data.groupby(['date', 'state'])['transaction_revenue'].sum().reset_index(name = 'revenue')
fig, ax = plt.subplots()
for type in list(a['state'].unique()):
    ax.plot(a[a.state==type].date, a[a.state==type].revenue,label=type)
plt.xlabel('Date')
plt.ylabel('Revenue ($)')
plt.legend()
plt.savefig('plots/growth_by_state.png')