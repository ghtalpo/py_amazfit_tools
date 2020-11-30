def uint2int(n):
    if type(n) == int:
        if n >= 0x7fffffffffffffff:
            return -(0xffffffffffffffff - n + 1)
        if n >= 0x7fffffff:
            return -(0xffffffff - n + 1)
    return n

def long2ulong(n):
    if type(n) == int:
        if n < 0:
            return (0xffffffffffffffff + n + 1) & 0xffffffff
    return n

def ulong2long(n):
    if type(n) == int:
        if n >= 0x7fffffffffffffff:
            n = -(0xffffffffffffffff - n + 1)
    return n
