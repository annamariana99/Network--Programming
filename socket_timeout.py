import socket

def socket_timeout():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(5)  # Mengatur timeout soket menjadi 5 detik untuk operasi soket

    host = "example.com"
    port = 80

    try:
        sock.connect((host, port))
        print("Socket connection successful")
    except socket.timeout:
        print("Socket operation timed out")
    except Exception as e:
        print("Socket connection error:", e)

if __name__ == '__main__':
    socket_timeout()