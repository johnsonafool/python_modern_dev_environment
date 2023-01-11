import socketio


def connect_socket_server(IP: str) -> None:
    try:
        sio = socketio.Client()
        sio.connect(IP)
    except socketio.exceptions.ConnectionError:
        print("Connection error")
        return


def UDP(message: str, con):
    if con:
        try:
            con.emit("gesture", message)
            print("message sent")
            return
        except socketio.exceptions.ConnectionError:
            print("Connection error")
            return
