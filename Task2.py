"""
2.	[medium] Модифікувати TCP-сервер з п.1, щоб він працював постійно та обробляв запити від багатьох клієнтів послідовно.
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
            while True:
                data = conn.recv(1024)
                if not data:
                    print(f"Клієнт {addr} завершив з'єднання")
                    break
                print(f"Отримано від {addr}: {data.decode('utf-8')}")
                response = f"[ECHO] {data.decode('utf-8')}"
                conn.sendall(response.encode('utf-8'))
                print(f"Відправлено до {addr}: {response}")
