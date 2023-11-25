import socket
import random

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 26062))
server_socket.listen(1)

print("Server is running...")

while True:
    conn, addr = server_socket.accept()
    print(f"Connection from {addr} has been established.")

    while True:
        # Generate a simple addition problem
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        expression = f"{num1} + {num2}"

        conn.send(expression.encode())

        try:
            client_answer = conn.recv(1024).decode()
            correct_answer = num1 + num2

            while client_answer != str(correct_answer):
                conn.send("Incorrect".encode())
                client_answer = conn.recv(1024).decode()

            # If the client's answer is correct
            conn.send("Correct".encode())

        except socket.timeout:
            print("Client response timed out.")
            break  # Break the loop if client response times out

    conn.close()
