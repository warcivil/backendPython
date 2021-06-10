from json import dumps


class app(object):
    '''WSGI приложение'''

    def __init__(self, environ, start_response):
        self.environ = environ
        self.start_response = start_response

    def __iter__(self):
        '''функция анализатора запроса'''

        if(self.environ["PATH_INFO"] not in ("/content", "/bugs", "/index", "/redirect")):
            self.create_response("404 Not Found", "application/json")
            answer = self.create_answer(
                "404 not found", self.environ["REQUEST_METHOD"], self.environ["PATH_INFO"], "not found error")
            yield f"{answer}".encode("utf-8")
        elif(self.environ["REQUEST_METHOD"] == "GET"):
            yield self.get()
        elif(self.environ["REQUEST_METHOD"] == "POST"):
            yield self.post()
        elif(self.environ["REQUEST_METHOD"] == "PUT"):
            yield self.put()
        else:
            yield self.delete()

    def post(self):
        '''POST ответ'''

        self.create_response("201 Created", "application/json")
        answer = self.create_answer(
            "201 Created", "POST", self.environ["PATH_INFO"], "METHOD POST")
        return f"{answer}".encode("utf-8")

    def put(self):
        '''PUT ответ'''

        self.create_response("200 OK", "application/json")
        answer = self.create_answer(
            "200 OK", self.environ["REQUEST_METHOD"], self.environ["PATH_INFO"], "METHOD PUT")
        return f"{answer}".encode("utf-8")

    def delete(self):
        '''delete ответ'''

        self.create_response("410 Gone", "application/json")
        answer = self.create_answer(
            "410 Gone",  self.environ["REQUEST_METHOD"], self.environ["PATH_INFO"], "METHOD DELETE")
        return f"{answer}".encode("utf-8")

    def get(self):
        '''GET ответ'''
        if(self.environ["PATH_INFO"] == "/content"):
            return f"{self.environ}".encode("utf-8")
        elif(self.environ["PATH_INFO"] == "/bugs"):
            return self.bugs_info()
        elif(self.environ["PATH_INFO"] == "/redirect"):
            self.start_response('301 Moved Permanently', [
                                ('Location', 'http://google.com')])
        answer = self.create_answer("200 OK", "GET", self.environ["PATH_INFO"])
        self.create_response('200 OK', 'application/json')
        return f"{answer}".encode("utf-8")

    def create_response(self, response_status, headers):
        ''' создаем код ответа и тип контента '''
        status = response_status
        response_headers = [('Content-type', headers)]
        self.start_response(status, response_headers)

    def create_answer(self, status, request_method, path_info, detail="default"):
        ''' создаем ответ '''
        return dumps({
            "status": status,
            "REQUEST_METHOD": request_method,
            "PATH_INFO": path_info,
            "detail": detail,
        })

    def bugs_info(self):
        ''' немного логики при обращении к /bugs '''
        
        if(self.environ['QUERY_STRING'] == "123456"):
            self.create_response("418 I'm teapot", "application/json")
            answer = self.create_answer(
                '418 I’m teapot', "GET", self.environ["PATH_INFO"], "i'am teapot :(")
            return f"{answer}".encode("utf-8")
        else:
            self.create_response("406 Not Acceptable", "application/json")
            answer = self.create_answer(
                "406 Not Acceptable", "GET", self.environ["PATH_INFO"])
            return f"{answer}".encode("utf-8")
