import base64
message_enc = input("Past here the message encode: \n")
key = input("Write the key for decryption:")
dec = []
message = base64.urlsafe_b64decode(message_enc).decode()
for i in range(len(message)):
    key_c = key[i % len(key)]
    dec.append(chr((256 + ord(message[i]) - ord(key_c)) % 256))
print("This is the decryption of your message: \n" + "".join(dec))