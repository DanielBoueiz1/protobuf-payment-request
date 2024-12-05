import payment_pb2  # Import the generated Protobuf file

# Create a PaymentRequest object
payment = payment_pb2.PaymentRequest()
payment.payer = "Alice"
payment.payee = "Bob"
payment.amount = 100.50

# Serialize the object to a binary file
with open("payment_request.bin", "wb") as f:
    f.write(payment.SerializeToString())

# Deserialize the object from the binary file
with open("payment_request.bin", "rb") as f:
    payment_read = payment_pb2.PaymentRequest()
    payment_read.ParseFromString(f.read())

# Print the deserialized object
print(f"Payer: {payment_read.payer}")
print(f"Payee: {payment_read.payee}")
print(f"Amount: {payment_read.amount}")