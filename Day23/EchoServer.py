import socket

HOST = '127.0.0.1'
PORT = 65432 # Non-privileged ports are > 1023

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST,PORT)) # parm is a tuple, defined in round brackets
    s.listen()
    conn, addr = s.accept()
    with conn:
        print("Connected by: ", addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)