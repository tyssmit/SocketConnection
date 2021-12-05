import socket

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host='localhost'
    port=5000
    sock.bind((host,port))
    sock.connect((host,port))
    print('Congrats we are connected')
    sock.close
if __name__ == "__main__":
    main()