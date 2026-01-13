BASE64_TABLE="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
def base62_encode(data: bytes) -> str:
  result = []
  for i in range(0,len(data),3):
    block = data[i:i+3]
    buffer = 0
    for b in block:
      buffer = (buffer << 8) | b
    missing_bytes = 3 - len(block)
    buffer <<= (missing_bytes * 8)
    for shift in range (18,-1,-6):
      index = (buffer >> shift) & 0b111111
      result.append(BASE64_TABLE[index])
    if missing_bytes:
      result[-missing_bytes:] = "=" * missing_bytes
  return "".join(result)
   
