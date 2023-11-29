import socket
import struct

def send_message(s, number1, operator, number2):
    # Pack numbers and operator
    message = struct.pack('>IcI', number1, operator.encode(), number2)
    # Print the packed message and its length
    print(f"Packed Message: {message}, Length: {len(message)}")
    # Send message length followed by the message
    s.send(struct.pack('>I', len(message)) + message)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('10.1.2.12', 13337))

# User inputs
number1 = int(input("Enter the first number: "))
operator = input("Enter the operator (+, -, *): ")
number2 = int(input("Enter the second number: "))

# Send message
send_message(s, number1, operator, number2)

# Receive and print the result
result = s.recv(1024)
print("Result:", result.decode())

s.close()

