import socket

def get_default_buffer_size():
    # Mendapatkan ukuran buffer pengiriman default
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sndbuf = sock.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF)
    print("Default send  Buffer size: %d bytes" % sndbuf)
    
    # Mendapatkan ukuran buffer penerimaan default
    rcvbuf = sock.getsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF)
    print("Default send  Buffer size: %d bytes" % sndbuf)
    
if __name__ == '__main__':
    get_default_buffer_size()