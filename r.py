import requests
from settings import TOKEN, USERNAME
from pprint import pprint

with requests.Session() as session:
    session.auth = (USERNAME, TOKEN)
    response = session.get('https://api.github.com/user/repos')

pprint(response.json())
