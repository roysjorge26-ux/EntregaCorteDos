import pandas as pd
import numpy as np
import random

# Elegir una semilla aleatoria dentro de un rango
seed = random.randint(30, 50)
np.random.seed(seed)
print(f"Usando semilla aleatoria: {seed}")

n = random.randint(60000, 65000)

# Generar variables
temperatura = np.random.normal(loc=22, scale=5, size=n)
personas = np.random.randint(1, 6, size=n).astype(float)
electrodomesticos = np.random.randint(5, 21, size=n).astype(float)

# Calcular consumo con algo de ruido
consumo = (temperatura * 0.85 + personas * 3.2 + electrodomesticos * 1.7 +
           np.random.normal(0, 3, n))

# Introducir NaNs aleatorios (~5%)
for col in [temperatura, personas, electrodomesticos, consumo]:
    idx_nan = np.random.choice(n, size=int(n * 0.05), replace=False)
    col[idx_nan] = np.nan

# Introducir outliers en el consumo (~1%)
outlier_idx = np.random.choice(n, size=int(n * 0.01), replace=False)
consumo[outlier_idx] += np.random.normal(100, 20, size=len(outlier_idx))

# Crear DataFrame
df = pd.DataFrame({
    'Temperatura': temperatura,
    'Personas': personas,
    'Electrodomesticos': electrodomesticos,
    'Consumo_kWh': consumo
})

# Guardar CSV
df.to_csv('consumo_hogar.csv', index=False)
print("Archivo 'consumo_hogar.csv' generado con éxito.")
