import requests

# URL
url = "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/FIQ02/CSV/1.0/en"

#GET request
response = requests.get(url)

# If the request was successful (status code 200)
if response.status_code == 200:
    # Store in "cso.csv"
    with open("cso.csv", "w", encoding="utf-8") as file:
        file.write(response.text)
else:
    print(f"Error: {response.status_code}")
