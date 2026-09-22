import pandas as pd

# url = 'https://raw.githubusercontent.com/adrianfelsky/TrabalhoRedesNeurais26-2/main/exercicio1/audit_data/audit_risk.csv'

df = pd.read_csv("audit_data/audit_risk.csv")

display(df.head())
print("\nInformações do Dataset:")
df.info()