import pandas as pd

# Sample data
data = {
    'UserID': ['user1', 'user2', 'user3', 'user4'],
    'Status': ['active', 'inactive', 'active', 'inactive']
}

df = pd.DataFrame(data)

# Key-value pairs for the condition
key_value_pairs = {'user1': 'active', 'user3': 'active'}

# Create new column based on condition
df['NewColumn'] = df.apply(lambda row: '@' + row['UserID'] if row['UserID'] in key_value_pairs and row['Status'] == key_value_pairs[row['UserID']] else None, axis=1)

print(df)
