"""
1.	[easy] Розробити echo-сервер з використанням python socket API, який приймає з'єднання від клієнта та повертає клієнту отримані дані.
"""
import socket

HOST = '127.0.0.1'
PORT = 50007

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST, PORT))
    server_socket.listen(1)
    print(f"Сервер запущено на порту {PORT}, очікування підключення...")
    conn, addr = server_socket.accept()
    with conn:
        print(f"Підключено клієнта: {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print(f"Отримано: {data.decode('utf-8')}")
            response = f"[ECHO] {data.decode('utf-8')}"
            conn.sendall(response.encode('utf-8'))
            print(f"Відправлено: {response}")


