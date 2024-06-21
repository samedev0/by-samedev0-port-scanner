import socket


Server = input("Enter a host to scan: ")
serverip = socket.gethostbyname(Server)


for port in range(1, 101):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)  
    result = sock.connect_ex((serverip, port))
    
    if result == 0:
        print(f"Port {port}: Open")
    else:
        print(f"Port {port}: Closed")
    
    sock.close() 

print("𝐒𝐜𝐚𝐧 𝐬𝐮𝐜𝐜𝐞𝐬𝐬𝐟𝐮𝐥")
print("𝐁𝐲 𝐃𝐞𝐯𝐞𝐥𝐨𝐩𝐞𝐫 𝐬𝐚𝐦𝐞𝐝𝐞𝐯𝟎")