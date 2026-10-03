import pandas as pd


train_df = pd.read_csv("data/Training.csv")

train_df.drop_duplicates(inplace=True)

train_df.fillna(0, inplace=True)

train_df.to_csv("data/clean_training.csv", index=False)

print("Data Cleaned")