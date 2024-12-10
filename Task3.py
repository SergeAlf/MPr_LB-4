"""
3.	[medium/hard]  Розробити TCP-сервер з використанням python socket API, який приймає текстовий файл від клієнта та зберігає його локально на стороні сервера.
"""
import socket

HOST = '127.0.0.1'
PORT = 50007

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST, PORT))
    server_socket.listen()
    print(f"Сервер запущено на порту {PORT}, очікування підключень...")

    while True:
        conn, addr = server_socket.accept()
        print(f"Підключено клієнта: {addr}")
        with conn:
            with open("received_file.txt", "wb") as file:
                while True:
                    data = conn.recv(1024)
                    if not data:
                        print(f"Файл отримано від клієнта {addr}")
                        break
                    file.write(data)


