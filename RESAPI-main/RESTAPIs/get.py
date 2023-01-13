import requests
api_url = "https://api.github.com/users/Kaitttonn"
response = requests.get(api_url)
print(response.json())
print(response.status_code)
