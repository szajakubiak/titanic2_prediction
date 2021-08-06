import requests


api_url = "http://localhost:3000/predict"

passenger_data = {"Age": 30,
                  "Pclass": 2,
                  "SibSp": 1,
                  "Parch": 0,
                  "Fare": 30.00,
                  "Sex": "male",
                  "Embarked": "S"}


response = requests.post(api_url, json = passenger_data)
print(response.json())