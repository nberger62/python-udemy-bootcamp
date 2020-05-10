import requests
url = "https://icanhazdadjoke.com/"

response = requests.get(url, headers={"Accept": "application/json"})

data = response.json()

#it will return as a JSON as a string, but by setting up the data variable we are turning that long string into a dictionary, which we can now utilize as python

print(type(data))
print(f"status: {data['status']}")

# <class 'dict'>
# They laughed when I said I wanted to be a comedian – they’re not laughing now.
