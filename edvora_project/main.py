import json
import uvicorn
import websocket
from fastapi import FastAPI

app = FastAPI()
session_pass = 'admin'


@app.get('/login')
def login(username, password):
    try:
        if password == session_pass:
            ws = websocket.create_connection("ws://localhost:7873")
            ws.send(json.dumps({'action': 'join_channel',
                                'payload': {
                                    'username': username,
                                    'password': password
                                }
                                }
                               ))
            response = json.loads(ws.recv())
            return json.dumps(response)
        else:
            return json.dumps({'message': 'wrong password'})
    except Exception as ex:
        print(f'Exception in login : {ex}')


@app.get('/logout')
def logout(username):
    try:
        ws = websocket.create_connection("ws://localhost:7873")
        ws.send(json.dumps({'action': 'leave_channel',
                            'payload': {
                                'username': username,
                            }
                            }
                           ))
        return json.dumps({'message': 'logged out'})
    except Exception as ex:
        print(f'Exception in logout : {ex}')

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=7863)
