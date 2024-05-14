import pandas as pd
url = "C:/Users/Ivonne/Desktop/Maestria/Aprendizaje Automatico/Clase1/Data (1)\Data/oil-spill.csv"
oil_data = pd.read_csv(url)
print(oil_data.head(10))