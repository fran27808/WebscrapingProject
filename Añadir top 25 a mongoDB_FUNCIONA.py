from datetime import date
from MEME import lista
from pymongo import MongoClient

fecha = date.today()

mongo_data = {fecha: lista}

client = MongoClient('localhost', 27017)

db = client['Google_Trends']
tendencias = db[str(fecha)]

tendencia = {'Top 25': lista}

insertado = tendencias.insert_one(tendencia)
