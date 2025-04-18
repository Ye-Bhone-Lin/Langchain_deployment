import requests

response_code = requests.post('https://langchain-deployment-dwwo.onrender.com/coding/invoke', json={"input":{"topic":"discord bot"}})

print(response_code.json()['output']['content'])

response_research = requests.post("https://langchain-deployment-dwwo.onrender.com/research/invoke", json={"input":{"topic":"AI"}})

print(response_research.json()['output']['content'])
