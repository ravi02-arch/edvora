import asyncio
import json
import websockets
from websockets.exceptions import ConnectionClosedError

subscribers = {}


async def notify_users():
    try:
        if subscribers:
            message = json.dumps({'users in this session': [user for user in subscribers]})
            await asyncio.wait([subscribers[user].send(message) for user in subscribers])

    except Exception as ex:
        print(f'Exception in notify_users : {ex}')


async def register(websocket, conn_details):
    try:
        username = conn_details['username']
        if username in subscribers:
            await unregister(conn_details)
        subscribers[username] = websocket
        await notify_users()
    except Exception as ex:
        print(f'Exception in registering a connection :{str(ex)}')


async def unregister(conn_details):
    try:
        username = conn_details['username']
        subscribers.pop(username)

    except Exception as ex:
        print(f'Exception in discarding a connection :{str(ex)}')


async def connection_setup(websocket, path):
    try:
        async for message in websocket:
            message = json.loads(message)
            conn_details = message['payload']
            if message['action'] == 'join_channel':
                await register(websocket, conn_details)

            elif message['action'] == 'leave_channel':
                await unregister(conn_details)

    except ConnectionClosedError:
        print('Error message : ', message)
        await unregister(conn_details)


start_server = websockets.serve(connection_setup, "localhost", 7873)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
