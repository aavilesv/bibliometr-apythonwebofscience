import numpy as np
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from semopy import Model, Optimizer
# Simulamos algunos datos para el ejemplo
np.random.seed(42) # Para reproducibilidad
data = np.random.randn(100, 5) # 100 observaciones, 5 variables
df = pd.DataFrame(data, columns=['X1', 'X2', 'X3', 'X4', 'X5'])

# Estandarizar los datos antes de aplicar PCA
scaler = StandardScaler()
df_scaled = scaler.fit_transform(df)

# Aplicar PCA
pca = PCA(n_components=2) # Reducir a 2 componentes principales
principalComponents = pca.fit_transform(df_scaled)
principalDf = pd.DataFrame(data = principalComponents, columns = ['PC1', 'PC2'])



# Añadimos una variable de resultado simulada al DataFrame
outcome = np.random.randn(100) # Simulamos una variable de resultado
principalDf['Y'] = outcome

# Definimos el modelo SEM
model_desc = """
    Y ~ PC1 + PC2
"""

# Ajustar el modelo
model = Model(model_desc)
model.fit(principalDf)
results = model.inspect()

print(results)

