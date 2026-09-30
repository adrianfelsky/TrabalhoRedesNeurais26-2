
import pandas as pd

# URL raw do arquivo audit_risk.csv no seu GitHub
audit_risk = 'https://raw.githubusercontent.com/adrianfelsky/TrabalhoRedesNeurais26-2/main/exercicio1/audit_data/audit_risk_TESTELEITURA4.csv'
trial = 'https://raw.githubusercontent.com/adrianfelsky/TrabalhoRedesNeurais26-2/main/exercicio1/audit_data/trial.csv'


# Carregando o dataset
audit_risk = pd.read_csv(audit_risk)
trial = pd.read_csv(trial)

print("\nDataset audit_risk:")
print(audit_risk)

print("\nDataset trial:")
print(trial)
