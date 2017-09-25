def app(environ, start_response):
    data = environ["QUERY_STRING"].split('&')
    body = [item + '\r\n' for item in data]
    status = '200 OK'
    headers = [('Content-Type', 'text/plain')]
    start_response(status, headers)
    return body
