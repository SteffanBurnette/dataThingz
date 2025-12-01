import pandas as pd

df = pd.read_csv("C:/Users/Steffan/Desktop/Ude-Science-Data/dataThingz/python==3.14.0/nyc_SAT_scores.csv")

print(df.head()) 



dfn = pd.DataFrame({
    'category': ['A', 'B', 'A', 'C', 'B', 'A'],
    'value': [10, 20, 15, 25, 30, 12]
})

grouped_df = dfn.groupby('category')["value"].mean() #mean

print(grouped_df.head())