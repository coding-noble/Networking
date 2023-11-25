import socket
import tkinter as tk
from tkinter import messagebox

def receive_problem():
    try:
        problem = client_socket.recv(1024).decode()
        problem_label.config(text=problem)
    except ConnectionAbortedError as e:
        print("Connection Aborted:", e)
    except ConnectionResetError as e:
        print("Connection Reset:", e)

def send_answer():
    user_answer = entry.get().strip()  # Get user input and remove leading/trailing spaces

    if not user_answer:
        messagebox.showerror("Error", "Please provide an answer.")
        return  # Stop processing if the user input is empty

    client_socket.send(user_answer.encode())
    server_response = client_socket.recv(1024).decode()

    if server_response == "Correct":
        messagebox.showinfo("Congratulations", "You got it right!")
        receive_problem()  # Get a new problem
    else:
        messagebox.showerror("Incorrect", "Try again!")

    entry.delete(0, tk.END)

def close_connection():
    client_socket.close()
    root.quit()

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 26062))

root = tk.Tk()
root.title("Math Quiz")
root.geometry("400x200")  # Set the initial size of the window

frame = tk.Frame(root)
frame.pack(expand=True, fill=tk.BOTH)

problem_label = tk.Label(frame, text="Solve the math problem:", font=("Arial", 14))
problem_label.pack(pady=10)

receive_problem()

entry = tk.Entry(frame, font=("Arial", 12))
entry.pack(pady=5)

submit_button = tk.Button(frame, text="Submit", command=send_answer, font=("Arial", 12))
submit_button.pack(pady=10)

root.protocol("WM_DELETE_WINDOW", close_connection)
root.mainloop()
