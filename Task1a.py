"""
a.	[easy] Розробити echo-клієнт з використанням python socket API, який встановлює з'єднання з сервером, надсилає строкові дані та отримує відповідь.
"""
import socket

HOST = '127.0.0.1'
PORT = 50007

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.connect((HOST, PORT))
    message = "Hello, Echo Server!"
    print(f"Відправлення: {message}")
    client_socket.sendall(message.encode('utf-8'))
    data = client_socket.recv(1024)
    print(f"Отримано: {data.decode('utf-8')}")