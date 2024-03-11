import requests

BASE = "http://127.0.0.1:5000/"

data = [{'likes':10 , 'name': 'Hubele', 'views': 1000000},
        {'likes':78 , 'name': 'How to make rest APIs', 'views': 90000},
        {'likes':876 , 'name': 'My firts video', 'views': 10},
        {'likes':13 , 'name': 'Nowy jpeg', 'views': 3}]


for i in range(len(data)):
    response = requests.put(BASE + 'video/' +str(i), data[i])
    print(response.json())


response = requests.delete(BASE + "video/0")
print(response)
 
input()

response = requests.get(BASE + 'video/2')
print(response.json())

input()

'''
response = requests.put(BASE + 'video/3', {'likes':10 , 'name': 'Hubele', 'views': 1000000})
print(response.json())

input()

response = requests.get(BASE + 'video/1')
print(response.json())

input()

response = requests.get(BASE + 'video/2')
print(response.json())
'''