import socket
import dill
from task import Task, factorial

def send_task(host, port, tasks):
     """
    Send tasks to a server and receive the results.

    Args:
        host (str): The IP address or hostname of the server.
        port (int): The port number of the server.
        tasks (list): A list of Task objects to be sent to the server.

    Returns:
        list: A list of results corresponding to the execution of each task.
              If an error occurs, returns None.
    """
    try:
        result = []
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((host, port))

        for task in tasks:
            client_socket.send(dill.dumps(task))
            result.append(dill.loads(client_socket.recv(4096)))
        return result
    except Exception as e:
        print("Error occurred while sending the task: ", e)
        return None
    finally:
        client_socket.close()

if __name__ == "__main__":
    task1 = Task(factorial, (5,))
    result = send_task("localhost", 5000, [task1])
    print("Results: ", result)
