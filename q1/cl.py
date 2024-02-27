#Japit Singh|| 113570220

# client.py
import socket
import pickle
import os

def load_file(filename):
     """
    Load the content of a file and return its binary data.

    Args:
        filename (str): The path of the file to be loaded.

    Returns:
        bytes: The binary data representing the content of the file.
    """
    with open(filename, 'rb') as f:
        return f.read()

def main():
     """
    Main function to connect to the server and send a file.

    Args:
        None

    Returns:
        None
    """
    host = '127.0.0.1'
    port = 12352
    buffer_size = 4096

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client_socket.connect((host, port))
    except Exception as e:
        print("Error connecting to the server:", e)
        return

    try:
        file_path = input("Enter the path of the file to send: ")
        if not os.path.exists(file_path):
            print("File not found.")
            return
        
        file_data = load_file(file_path)
        pickled_data = pickle.dumps(file_data)

        client_socket.sendall(pickled_data)
        print("File sent successfully")
    except Exception as e:
        print("Error:", e)
    finally:
        client_socket.close()

if __name__ == "__main__":
    main()
