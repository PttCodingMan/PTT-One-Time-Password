

def get_bytes_from_file(filename):
    return open(filename, "rb").read().hex()

def hex_byte(hex):
    return bytearray.fromhex(hex)

if __name__ == '__main__':
    hex = get_bytes_from_file('../PTTOTP.ico')

    print(hex)