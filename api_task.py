import requests
import json

url = "https://catfact.ninja/fact"

response = requests.get(url)

data = response.json()

print("Random Cat Fact:")
print(data["fact"])

with open("cat_fact.json", "w") as file:
    json.dump(data, file, indent=4)

print("\nJSON response saved to cat_fact.json")