import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sn

names = ['Recente','Frequente','Monetario','Tempo','Doou_Sangue_em_Marco_de_2007']
    
df = pd.read_csv(r'C:\Users\cauae\Downloads\blood+transfusion+service+center\dados\transfusion_edited.data.csv', encoding='utf-8-sig', names=names)

features = ['Recente','Frequente','Monetario','Tempo']
target = 'Doou_Sangue_em_Marco_de_2007'

    

# Excluir a variável dependente 'classificacao' do DataFrame
independente_df = df[features]

# Calcular a matriz de correlação
correlation = independente_df.corr()

# Imprimir a matriz de correlação
print(correlation)

# Plotar a matriz de correlação usando um heatmap
plt.figure(figsize=(10, 8))
plt.rcParams.update({'font.size': 12})
sn.heatmap(correlation, cmap='viridis', vmin=-1, vmax=1, center=0, annot=True, fmt=".2f", square=True, linewidths=.5)
plt.show()
