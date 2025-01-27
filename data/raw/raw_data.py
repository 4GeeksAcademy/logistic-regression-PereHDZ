import pandas as pd

url = "https://raw.githubusercontent.com/4GeeksAcademy/logistic-regression-project-tutorial/main/bank-marketing-campaign-data.csv"

df = pd.read_csv(url)

df.to_csv('bank_data.csv', index=False)
print("Dataset saved as 'bank_data.csv'")