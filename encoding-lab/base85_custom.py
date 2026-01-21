BASE85_START = 33  # '!'


def base85_encode(data: bytes) -> str:
    result = []

    padding = (4 - len(data) % 4) % 4
    data += b"\x00" * padding

    for i in range(0, len(data), 4):
        block = data[i:i+4]

        # Pack 4 bytes into 32-bit buffer (same idea as Base64)
        buffer = 0
        for b in block:
            buffer = (buffer << 8) | b

        # Convert 32-bit number into 5 Base85 chars
        temp = []
        for _ in range(5):
            buffer, rem = divmod(buffer, 85)
            temp.append(chr(BASE85_START + rem))

        # Reverse because we built it backwards
        result.extend(reversed(temp))

    # Store padding count (so decoding becomes correct)
    return "".join(result) + str(padding)
