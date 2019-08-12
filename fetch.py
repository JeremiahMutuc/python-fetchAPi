import requests

req = requests.get('https://jsonplaceholder.typicode.com/todos')

print(req) #numbers of attributes

print(dir(req)) #print all 200 attributes

print(req.json()) #print all objects in fetched link