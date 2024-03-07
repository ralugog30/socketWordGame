import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("0.0.0.0", 7777))
server_socket.listen(1)

print("Server is listening on port ...")

client_socket, client_address = server_socket.accept()
print("Client connected!")

invalid_endings = ["nt", "ee", "ct", "rb", "rt", "ns", "rd", "lt", "ft", "ps", "ng", "im", "nd", "nz", "lm", "nj"]

game_over = False

while not game_over:
    received_word = client_socket.recv(1024).decode('utf-8')
    received_word = received_word.strip()
    print("Received from client: " + received_word)

    if received_word[:9] == "Game Over":
        print("Server won!")
        break

    valid_word = True

    received_word = received_word.strip('\n')

    for i in invalid_endings:
        if received_word[-2:] == i:
            valid_word = False
            break

    if valid_word:
       print("Server's turn")
       server_input = input("Write a word that ends with the last two letters of the given word: ")
       if server_input[:2] != received_word[-2:]:
           print("Change the word")
       	   server_input = input("Write a word that ends with the last two letters of the given word: ")
       client_socket.send(server_input.encode('utf-8')+ b'\n')
    else:
       print("Client won!")
       client_socket.send("Game Over".encode('utf-8')+ b'\n')
       break



client_socket.close()
server_socket.close()
