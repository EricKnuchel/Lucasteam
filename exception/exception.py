class DemoException(Exception):
    """_summary_

    Args:
        Exception (_type_): _error_
        exception personalisada para mostrar un message
    """

    def __init__(self, message):
        super().__init__(message)
