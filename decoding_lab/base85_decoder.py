def base85_decode(encoded: str) -> bytes:
    padding = int(encoded[-1])
    encoded = encoded[:-1]

    result = bytearray()

    for i in range(0, len(encoded), 5):
        block = encoded[i:i+5]
        num = 0
        for ch in block:
            num = num * 85 + (ord(ch) - BASE85_START)
        for shift in range(24, -1, -8):
            result.append((num >> shift) & 0xFF)

    return bytes(result[:-padding]) if padding else bytes(result)
