import pandas as pd

training = pd.read_csv("data/Training.csv")
testing = pd.read_csv("data/Testing.csv")

merged = pd.concat([training, testing])

merged.to_csv("data/merged_dataset.csv", index=False)

print("Datasets merged")