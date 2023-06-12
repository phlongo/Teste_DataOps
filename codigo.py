import pandas as pd
import pymongo

carros_data = {
    'Carro': ['Onix', 'Polo', 'Sandero', 'Fiesta', 'City'],
    'Cor': ['Prata','Branco','Sandero','Fiesta','City'],
    'Montadora': ['Chevrolet', 'Volkswagen', 'Renault','Frod','Honda']
}

carros_df = pd.DataFrame(carros_data)

montadora_data ={
    'Montadora': ['Chevrolet', 'Volkswagen', 'Renault','Frod','Honda'],
    'Pais':['EUA','Alemanhã','Franca','EUA','Japão']
}

montadora_df = pd.DataFrame(montadora_data)

print(montadora_df)

print(carros_df)
client = pymongo.MongoClient("mongodb://localhost:27017/")


db = client["local"]
carros_collection = db["Carros"]
montadoras_collection = db["Montadoras"]

carros_data = carros_df.to_dict(orient="records")
montadora_data = montadora_df.to_dict(orient="records")

carros_collection.insert_many(carros_data)
montadoras_collection.insert_many(montadora_data)