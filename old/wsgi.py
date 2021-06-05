from wsgiref.simple_server import make_server                                   
                                                                                
PORT = 8082                                                                     
                                                                                
def application(environ, start_response):                                               
    start_response('200 OK', [('Content-Type', 'text/html')])                   
    return [b'Hello, world!']                                                   
                                                                                
if __name__ == '__main__':                                                      
    try:                                                                        
        httpd = make_server('', PORT, app)                                      
        print(f'Serving on port {PORT}...')                                     
        httpd.serve_forever()                                                   
    except KeyboardInterrupt:                                                   
        print('Shutting Down Server')                                           
