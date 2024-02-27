#Japit Singh|| 113570220


# server.py
import socket
import pickle

def save_file(data, directory, filename):
      """
    Save the received file data to a specified directory with the given filename.

    Args:
        data (bytes): The binary data representing the file.
        directory (str): The directory path where the file will be saved.
        filename (str): The name of the file to be saved.

    Returns:
        None
    """
    os.makedirs(directory, exist_ok=True)
    filepath = os.path.join(directory, filename)
    with open(filepath, 'wb') as f:
        f.write(data)

def main():
     """
    Main function to start the server and handle incoming connections.

    Args:
        None

    Returns:
        None
    """
    host = '127.0.0.1'
    port = 12352
    buffer_size = 4096
    directory = "received_files"  

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        server_socket.bind((host, port))
        server_socket.listen(1)
        print("Server is listening at", (host, port))

        while True:
            client_socket, client_address = server_socket.accept()
            print("Connected to", client_address)

            try:
                data = client_socket.recv(buffer_size)
                if not data:
                    print("No data received.")
                    continue

                file_data = pickle.loads(data)

                filename = input("Enter the filename to save the received file: ")
                save_file(file_data, directory, filename)
                print("File saved successfully as", filename)
            except Exception as e:
                print("Error:", e)
            finally:
                client_socket.close()
    finally:
        server_socket.close()

if __name__ == "__main__":
    main()
