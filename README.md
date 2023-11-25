# Overview

Aspiring to enhance my skills as a software engineer, I developed a networking program comprising a server and client components. The software demonstrates communication between the server and client applications, aiming to help me understand networking principles and implementation.

The networking program facilitates communication between a server and client. To utilize the software, start the server application first, followed by the client application.

The primary goal behind creating this software was to comprehend the intricacies of networking and gain hands-on experience in establishing communication protocols between different endpoints.

[Software Demo Video](https://youtu.be/H_8K2ubwOJQ)

# Network Communication

The architecture employed in this software is the client/server model. The communication relies on the TCP protocol, utilizing specific port numbers for connection.

TCP was used for reliable, ordered, and error-checked delivery of messages. The server code binds to IP an address, however, using 'localhost' and port '26062' works as well. The client code also connects to the same IP address and port for communication.

The server generates a simple addition problem and sends it to the client. The client receives the problem, allows the user to input an answer, and sends it back to the server for verification.

# Development Environment

Tools and languages used:

- IDEs like Visual Studio Code
- Python programming language
- Python's `socket` library for networking functionalities
- Tkinter for GUI management (utilized in the client-side application)

# Useful Websites

* [socket — Low-level networking interface](https://docs.python.org/3/library/socket.html)
* [socketserver — A framework for network servers](https://docs.python.org/3/library/socketserver.html)
* [OSI model — Wikipedia](https://en.wikipedia.org/wiki/OSI_model)
* [Client server model — Wikipedia](https://docs.python.org/3/library/socketserver.html)
* [Peer to Peer Computing](https://www.tutorialspoint.com/Peer-to-Peer-Computing)
* [What's the Difference Between TCP and UDP? — How-To Geek](https://www.howtogeek.com/190014/htg-explains-what-is-the-difference-between-tcp-and-udp/)
* [Graphical User Interfaces with Tk](https://docs.python.org/3/library/tk.html)

# Future Work

* Implement encryption for secure data transmission
* Enhance error handling and exception management
* Develop a more robust user interface for better interaction
* Allow multiple clients to connect to the server at the same time