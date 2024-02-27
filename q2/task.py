import dill

class Task:
    """
    Represents a task to be executed.

    Attributes:
        func (callable): The function to be executed.
        args (tuple): The arguments to be passed to the function.
    """
    def __init__(self, func, args):
        """
        Initialize a Task object.

        Args:
            func (callable): The function to be executed.
            args (tuple): The arguments to be passed to the function.
        """
        self.func = func
        self.args = args
    
    def runTask(self):
        """
        Execute the task.

        Returns:
            The result of the task execution.
        """
        return self.func(*self.args)

def factorial(n):
    """
    Calculate the factorial of a given number.

    Args:
        n (int): The number for which factorial is to be calculated.

    Returns:
        int: The factorial of the given number.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def task_worker(task_data, client_socket):
    """
    Perform the task sent by the client and send back the result.

    Args:
        task_data (bytes): Serialized task data received from the client.
        client_socket (socket.socket): Socket object for communication with the client.

    Returns:
        None
    """
    try:
        task = dill.loads(task_data)
        result = task.runTask()
        client_socket.sendall(dill.dumps(result))
    except Exception as e:
        print("Exception occurred: ", e)
        client_socket.close()
