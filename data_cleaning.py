import pandas as pd

# Load the dataset
df = pd.read_csv("bank-full.csv", sep=";")

# split data into separate DataFrames
client_columns = ['age', 'job', 'marital', 'education', 'default', 'balance', 'housing', 'loan']
campaign_columns = ['contact', 'day', 'month', 'duration', 'campaign', 'pdays', 'previous', 'poutcome', 'y']


# create separate dataframes
client_df = df[client_columns].copy()
campaign_df = df[campaign_columns].copy()

# Convert columns to appropriate data types
client_df['age'] = client_df['age'].astype('int')
client_df['balance'] = client_df['balance'].astype('int')

campaign_df['day'] = campaign_df['day'].astype('int')
campaign_df['duration'] = campaign_df['duration'].astype('int')
campaign_df['campaign'] = campaign_df['campaign'].astype('int')
campaign_df['pdays'] = campaign_df['pdays'].astype('int')
campaign_df['previous'] = campaign_df['previous'].astype('int')


# Save Dataframes to CSV files
client_df.to_csv('client_data.csv', index=False)
campaign_df.to_csv('campaign_data.csv', index=False)



print("Data Cleaning Completed!")

