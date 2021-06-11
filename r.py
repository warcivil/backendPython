import requests
from pprint import pprint
token = "xxxxxxxxxxx"
username = "warcivil"
r = requests.get('https://api.github.com/user', auth=(username, token))

with requests.Session() as session:
    session.auth = (username, token)
    response = session.get('https://api.github.com/user')

#pprint(response.json())
repos = session.get('https://api.github.com/user/repos')
repo_list = [item for item in repos.json() if item["private"] == True]
pprint(repo_list)