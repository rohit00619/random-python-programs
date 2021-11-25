import pandas as pd
purchase_1 = pd.Series({'Name': 'Chris',
                        'Item Purchased': 'Dog Food',
                        'Cost': 22.50})
purchase_2 = pd.Series({'Name': 'Kevyn',
                        'Item Purchased': 'Kitty Litter',
                        'Cost': 2.50})
purchase_3 = pd.Series({'Name': 'Vinod',
                        'Item Purchased': 'Bird Seed',
                        'Cost': 5.00})
df = pd.DataFrame([purchase_1, purchase_2, purchase_3], index=['Store 1', 'Store 1', 'Store 2'])
#print(df.head())

#print(df.loc['Store 2'])

#print(type(df.loc['Store 2']))

#print(df.loc['Store 1'])

#print(df.loc['Store 1', 'Cost'])

#print(df.T)

print(df.T.loc['Item Purchased'])
print(df['Item Purchased'])
