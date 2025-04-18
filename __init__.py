import requests

response_code = requests.post('http://localhost:8000/coding/invoke', json={"input":{"topic":"discord bot"}})

#print(response_code.json()['output']['content'])

response_research = requests.post("http://localhost:8000/research/invoke", json={"input":{"topic":"AI"}})

#print(response_research.json()['output']['content'])