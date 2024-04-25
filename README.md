# Help Desk Ticketing System

This repository contains a Python implementation of the Chain of Responsibility design pattern applied to a help desk ticketing system. The system is designed to handle different types of support requests, such as hardware issues, software issues, and network issues, by passing them through a series of handlers until the request is processed.

## Overview

The Chain of Responsibility pattern allows an object to send a command without knowing which object will handle the request. This pattern decouples the sender and the receiver. In this implementation, each type of request (hardware, software, network) has a dedicated handler. If a handler cannot process a request, it passes the request along to the next handler in the chain.

## Structure

The project is structured as follows:

- `Handler`: An abstract base class for all handlers, defining the interface for handling requests.
- `HardwareHandler`: A concrete handler class for handling hardware-related support requests.
- `SoftwareHandler`: A concrete handler class for handling software-related support requests.
- `NetworkHandler`: A concrete handler class for handling network-related support requests.

Requests are processed starting from the `HardwareHandler`. If the `HardwareHandler` is not appropriate for the request, it is passed to the `SoftwareHandler`, and potentially on to the `NetworkHandler`.

## How to Run

Ensure you have Python installed on your system. You can run the script directly from the command line:

```bash
python help_desk.py
