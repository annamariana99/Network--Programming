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

if __name__ == '__main__':
    modify_buff_size()
    
Tujuan: Skrip ini bertujuan untuk menguji dan mengatur ukuran buffer kirim dan terima pada soket. Ini berguna untuk mengoptimalkan kinerja komunikasi jaringan dengan mengatur ukuran buffer sesuai kebutuhan.

Langkah-langkah:
1.Membuat objek soket.
2.Mendapatkan ukuran buffer kirim saat ini.
3.Mengatur ukuran buffer kirim dan terima menggunakan setsockopt.
4.Mendapatkan ukuran buffer kirim setelah dimodifikasi.
5.Mencetak ukuran buffer sebelum dan sesudah modifikasi