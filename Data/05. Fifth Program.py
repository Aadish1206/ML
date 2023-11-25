#assing and explode
import pandas as pd

d = {
    'Team': ["Team 1", "Team 2"],
    'Name': ["a,b,c,d,e", "f,k,l,m"]
}

df = pd.DataFrame(d)

df['Name'] = df['Name'].str.split(',')

df = df.assign(Player=df['Name']).explode('Player')

df = df.drop(columns=['Name'])

print(df)
