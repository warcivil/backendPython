import requests

r=requests.delete('http://localhost:8082/index', data={'a':'b'})
print(r.text)