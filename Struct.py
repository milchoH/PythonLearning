from struct import *

#Store as bytes data
packed_data = pack('iif', 6, 19, 3.14)
print(packed_data)

print(calcsize('i'))
print(calcsize('f'))
print(calcsize('iif'))

original_data = unpack('iif', b'\x06\x00\x00\x00\x13\x00\x00\x00\xc3\xf5H@')
print(original_data)