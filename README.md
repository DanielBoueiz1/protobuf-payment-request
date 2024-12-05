# Protobuf Payment Request

This project demonstrates how to use Protocol Buffers (Protobuf) to serialize and deserialize a simple payment request in Python.

## Features
- Define a payment request using Protobuf (`.proto` file).
- Generate Python classes from the `.proto` file using `protoc`.
- Serialize the payment request into a compact binary format.
- Deserialize the binary format back into a readable object.

## Files
- `payment.proto`: Defines the structure of the payment request.
- `payment_pb2.py`: Generated Python code from the `.proto` file.
- `serialize_deserialize.py`: A Python script that demonstrates Protobuf serialization and deserialization.

## How to Run
1. Ensure the Protobuf compiler (`protoc`) is installed and in your system's PATH.
2. Compile the `payment.proto` file to generate the `payment_pb2.py` file:
   ```bash
   protoc --python_out=. payment.proto