import socket
import struct

def process_message(message):
    number1, operator, number2 = struct.unpack('>IcI', message)
    operator = operator.decode()
    if operator == '+':
        return number1 + number2
    elif operator == '-':
        return number1 - number2
    elif operator == '*':
        return number1 * number2
    else:
        raise ValueError("Invalid operator")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('10.1.2.12', 13337))
s.listen(1)
conn, addr = s.accept()

while True:
    try:
        # Read message length
        raw_length = conn.recv(4)
        if not raw_length:
            break
        length = struct.unpack('>I', raw_length)[0]
        
        # Read the message
        message = conn.recv(length)
        print(f"Received Message: {message}, Length: {length}")
        result = process_message(message)

        # Send the result back
        conn.send(str(result).encode())

    except Exception as e:
        print(f"Error: {e}")
        break

conn.close()
