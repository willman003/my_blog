from application import create_app
from os import environ

app = create_app('development')

if __name__ == "__main__":
    HOST = environ.get('SERVER_HOST','localhost')
    try:
        PORT = int(environ.get('SERVER_PORT','5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)