

#owed_points must be input as a parameter to function
import sys
from datetime import datetime
import pandas as pd
def transactions():
    owed_points = int(sys.argv[1])
    df = pd.read_csv('transactions.csv')
    sorted_df = df.sort_values(by=["timestamp"], ascending = True)
    if owed_points < 0:
        return "Input can't be negative!"
    users = {} # for final result
    usertotal = {}  # for summing up total value of points

    for index, row in sorted_df.iterrows():
        if row['payer'] not in usertotal:
            usertotal[row['payer']] = 0
        usertotal[row['payer']] += row['points']

    for index, row in sorted_df.iterrows():
        if owed_points <= 0:
            break
        if row['payer'] not in users:
            users[row['payer']] = 0
        
        if owed_points > row['points']:
            owed_points -= row['points']
            users[row['payer']] -= row['points']
        else:      
            users[row['payer']] -= owed_points
            owed_points = 0
    
    for val in users:
        users[val] = usertotal[val] + users[val]
    print(users)
    return users

if __name__ == '__main__':
    transactions()

