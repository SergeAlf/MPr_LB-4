"""
a.	[medium]  Розробити TCP-клієнт, який відправляє будь-який текстовый файл на сервер.
"""
import socket

HOST = '127.0.0.1'
PORT = 50007
FILE_TO_SEND = "file_to_send.txt"

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.connect((HOST, PORT))
    print(f"Підключено до сервера {HOST}:{PORT}")
    try:
        with open(FILE_TO_SEND, "rb") as file:
            while (chunk := file.read(1024)):
                client_socket.sendall(chunk)
        print(f"Файл {FILE_TO_SEND} успішно відправлено.")
    except FileNotFoundError:
        print(f"Файл {FILE_TO_SEND} не знайдено.")