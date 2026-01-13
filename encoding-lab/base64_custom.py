BASE64_TABLE="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
def base62_encode(data:bytes)-> str:
  bits=""
  for byte in data:
    bits += f"{byte:08b}"
  while len(bits) % 6 != 0:
    bits += "0"
  encoded = " "
  for i in range(0,len(bits),6):
    chunk = bits[i:i+6]
    value = int(chunk, 2)
    encoded += BASE64_TABLE[value]
    
  padding = (3 - len(data) % 3) % 3
  encoded += "=" * padding
  return encoded
