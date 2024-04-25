class Handler:
    """Abstract handler: defines an interface for handling requests and
    optionally implements the successor link."""

    def __init__(self, successor=None):
        self._successor = successor

    def handle_request(self, request):
        raise NotImplementedError("Must provide implementation in subclass.")


class HardwareHandler(Handler):
    """Concrete handler 1: handles hardware-related requests."""

    def handle_request(self, request):
        if request['type'] == 'hardware':
            return f"Hardware team handling request {request['id']}"
        elif self._successor is not None:
            return self._successor.handle_request(request)


class SoftwareHandler(Handler):
    """Concrete handler 2: handles software-related requests."""

    def handle_request(self, request):
        if request['type'] == 'software':
            return f"Software team handling request {request['id']}"
        elif self._successor is not None:
            return self._successor.handle_request(request)


class NetworkHandler(Handler):
    """Concrete handler 3: handles network-related requests."""

    def handle_request(self, request):
        if request['type'] == 'network':
            return f"Network team handling request {request['id']}"
        elif self._successor is not None:
            return self._successor.handle_request(request)


def test_handlers():
    """Function to test the Chain of Responsibility"""
    # Creating handlers
    network_handler = NetworkHandler()  # End of the chain, no successor
    software_handler = SoftwareHandler(network_handler)
    hardware_handler = HardwareHandler(software_handler)

    # List of requests
    requests = [
        {'id': 1, 'type': 'software', 'description': 'Cannot install software.'},
        {'id': 2, 'type': 'hardware', 'description': 'Laptop screen is broken.'},
        {'id': 3, 'type': 'network', 'description': 'Wi-Fi keeps disconnecting.'},
        {'id': 4, 'type': 'unknown', 'description': 'Something else is wrong.'}
    ]

    # Process each request
    for request in requests:
        result = hardware_handler.handle_request(request)
        print(result if result else f"No handler found for request {request['id']} with type {request['type']}.")


if __name__ == "__main__":
    test_handlers()
