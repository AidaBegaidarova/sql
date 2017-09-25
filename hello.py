def wsgi_application(environ, start_response):
    body = ""
    data = environ["QUERY_STRING"].split('&')
    for item in data:
        body += item + '\r\n'
    status = '200 OK'
    headers = [('Content-Type', 'text/plain')]
    start_response(status, headers)
    return [body]
