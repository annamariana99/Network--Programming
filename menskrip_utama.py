import socket

SEND_BUF_SIZE = 4096
RECV_BUF_SIZE = 4096

def modify_buff_size():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Get the size of the socket's send buffer
    bufsize = sock.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF)
    print("Buffer size [Before]: %d" % bufsize)

    sock.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, SEND_BUF_SIZE)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, RECV_BUF_SIZE)

    bufsize = sock.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF)
    print("Buffer size [After]: %d" % bufsize)

def socket_timeout():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(5)  # Set a timeout of 5 seconds for socket operations

    host = "example.com"
    port = 80

    try:
        sock.connect((host, port))
        print("Socket connection successful")
    except socket.timeout:
        print("Socket operation timed out")
    except Exception as e:
        print("Socket connection error:", e)

def main():
    print("a. Socket Timeout:")
    socket_timeout()

    print("\nb. Informasi Tentang Status Koneksi:")
    # Add your code to check connection status here

    print("\nc. Ukuran Buffer Sebelum dan Sesudah Modifikasi:")
    modify_buff_size()

if __name__ == '__main__':
    main()