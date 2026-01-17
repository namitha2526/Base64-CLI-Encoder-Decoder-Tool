BASE64_TABLE = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
REVERSE_TABLE = {ch: i for i, ch in enumerate(BASE64_TABLE)}

def base64_decode(encoded: str) -> bytes:
    data = bytearray()

    for i in range(0, len(encoded), 4):
        block = encoded[i:i+4]

        buffer = 0
        padding = block.count("=")

        # Convert Base64 chars to 24-bit buffer
        for ch in block:
            if ch == "=":
                buffer <<= 6
            else:
                buffer = (buffer << 6) | REVERSE_TABLE[ch]

        # Extract bytes (3 bytes = 24 bits)
        for shift in range(16, -1, -8):
            byte = (buffer >> shift) & 0xFF
            data.append(byte)

        # Remove bytes added due to padding
        if padding:
            del data[-padding:]

    return bytes(data)
