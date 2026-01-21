BASE85_START = 33  # '!'

def base85_encode(data: bytes) -> str:
    result = []
    padding = (4 - len(data) % 4) % 4
    data += b"\x00" * padding
    for i in range(0, len(data), 4):
        block = data[i:i+4]
        buffer = 0
        for b in block:
            buffer = (buffer << 8) | b
        temp = []
        for _ in range(5):
            buffer, rem = divmod(buffer, 85)
            temp.append(chr(BASE85_START + rem))

        result.extend(reversed(temp))

    return "".join(result) + str(padding)
