import requests

file = {'file':  open('test.txt', 'rb')}
r = requests.post('https://anonymfile.com/api/v1/upload', files=file)

print(r.text)