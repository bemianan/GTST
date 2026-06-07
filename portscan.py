import socket
target = input("Enter target IP or hostname: ")
for port in (22, 80, 8080):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)
    result= sock.connect_ex((target,port))
    if result==0:
        print(f"port {port} is open.")
    else:
        print(f"port {port} is closed.")