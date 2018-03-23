import socket, json

def logged_in_terminal(func):
    def inner(*args, **kwargs):
        print("[+] command executed. ")
        try:
            return func(*args, **kwargs)
        except Exception as e:
            return "command was not successful.\n\treason : "+str(e)
    return inner

class NotAPhoneNumberError(Exception):
    def __init__(self, msg):
        super().__init__(msg)    

class Bot:
    def __init__(self, server):
        self._server = server

    @logged_in_terminal
    def execute(self, command):
        if command.startswith("/stop"):
            print("quitting server...")
            self._server.stop()
            return "server is stoping."
        elif command.startswith("/locate") and len(command.replace("/locate", ""))>4:
            phone_number = command.replace("/locate","").replace("?","").replace("phone=","").strip()
            try:
                return Bot.phone_locator(phone_number)
            except NotAPhoneNumberError as err:
                return str(err) + " is not a valid phone number"    
        else:
            return "unknown command or invalid usage - " + command

    @staticmethod
    def phone_locator(phone_number):
        phone_number = phone_number.replace("+", "")

        if not phone_number.isnumeric() or len(phone_number) != 12:
            raise NotAPhoneNumberError(phone_number)

        if(phone_number.startswith("251")):
            return phone_number + " is registered to Ethiopia (ET)"
        else:
            return phone_number + " is registered to Unknown Country"

class HttpServer:
    def __init__(self, host = '', port = 8888):
        self.host = host
        self.port = port

        self._bot = Bot(self)

        self.shouldRun = True
        self.listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.listen_socket.bind((self.host, self.port))        

        self.client_connection = None

    def respond(self, text):        
        http_response = "HTTP/1.1 200 OK\nContent-type: application/json\n\n"+json.dumps({
            'success' : True,
            'message' : text
        })
        print(http_response)
        self.client_connection.sendall(http_response.encode("utf-8"))
        self.client_connection.close()

    def respondWithHTML(self, html):        
        http_response = "HTTP/1.1 200 OK\nContent-type: text/html\n\n"+html
        print(http_response)
        self.client_connection.sendall(http_response.encode("utf-8"))
        self.client_connection.close()


    def serve(self):
        self.listen_socket.listen(1)
        print('Serving HTTP on port %s ...' % self.port)

        while self.shouldRun:
            self.client_connection, client_address = self.listen_socket.accept()
            request = self.client_connection.recv(1024).decode("utf-8").splitlines()
            try:
                first_line = request.pop(0)

                method, url, http_version = first_line.split()

                if url == '/':
                    self.respondWithHTML(HttpServer.getIndexPageHTML())
                else:
                    self.respond(self._bot.execute(url))        
            except:
                print("Invalid Request")
                

    @staticmethod
    def getIndexPageHTML():
        with open('index.html') as file:
            return file.read()
            
    def stop(self):
        print("[-] Server is stopping...")
        self.shouldRun = False

server = HttpServer()
server.serve()