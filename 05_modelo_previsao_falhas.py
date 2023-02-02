#%%
import pandas as pd
import joblib
import sys

#%%
class PredFalhas():
    
    def __init__(self):
        self.modelo = joblib.load('modelo_pred_falhas.pkl')
        self.encoder = joblib.load('label_encoder.pkl')
    
    def fit(self, x):   
        self.x = x
        self.x.drop(['udi', 'product_id'], axis=1, inplace=True)
        self.x = self.x.drop(columns='air_temperature_k')
        self.x = pd.get_dummies(self.x)
    
    def previsao(self):
        self.y = self.modelo.predict(self.x)
        return self.encoder.inverse_transform(self.y)

# %%

if __name__ == "__main__":
    input_data = sys.argv[1]
    print(input_data)
    
    modelo = PredFalhas()
    x = pd.read_csv(input_data)
    modelo.fit(x)
    previsoes = modelo.previsao()
    previsoes = pd.DataFrame(previsoes)
    previsoes.to_csv('classificacoes_falhas.csv', index=False, header=None)
    print('done')