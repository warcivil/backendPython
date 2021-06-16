import requests
from settings import USERNAME, TOKEN
from json import dumps

class GitModule:
    def __init__(self, url):
        self.url = url

    def repos_content(self):
        ''' генерируем инфу о репозиториях в формате json '''

        answer = []
        response = self.create_session()
        for item in response.json():
            answer.append({
                "name": item["name"],
                "reposity full name": item["full_name"],
                "html url": item["html_url"],
                "visibility": "private" if item["private"] else "public",
                "subscribers count": item["watchers_count"],
                "size": item["size"],
            })
        return f"{dumps(answer)}".encode("utf-8")

    def create_session(self):
        ''' создаем сессию '''

        with requests.Session() as session:
            session.auth = (USERNAME, TOKEN)
            return session.get(self.url)
