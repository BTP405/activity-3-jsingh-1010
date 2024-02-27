import socket
import dill
from task import task_worker

def main(address, port):
     """
    Start a server to listen for incoming connections and process tasks.

    Args:
        address (str): The IP address or hostname to bind the server to.
        port (int): The port number to bind the server to.

    Returns:
        None
    """
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = (address, port) 
    server_socket.bind(server_address)
    server_socket.listen(1)
    print('\nServer is listening...')

    while True: 
        client_socket, client_address = server_socket.accept(); 
        try: 
            print('Connection Established with: ', client_address)
            while True: 
                task_data = client_socket.recv(1024)
                if not task_data: 
                    break
                task_worker(task_data, client_socket)
        except Exception as e:
            print("Error occurred in server: ", e)   
        finally:
            client_socket.close()    

if __name__ == "__main__":
    main("localhost", 5000)
