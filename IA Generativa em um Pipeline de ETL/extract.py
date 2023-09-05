import pandas as pd
import requests
import json

# cd IA Generativa #
df = pd.read_csv("SBC2023.csv") #df == dataframe
user_ids = df["UserID"].tolist()
print(user_ids)

api_url = "https://sdw-2023-prd.up.railway.app"

def get_user(id):
    response = requests.get(f"{api_url}/users/{id}")
    return response.json() if response.status_code == 200 else None

users: list = [user for id in user_ids if (user := get_user(id)) is not None]
                # usuario para cada id em user ids, se o usuario retornado pelo get_user() for diferente de None
print(json.dumps(users, indent=4))

#### Preciso criar um criador de mais usuarios.