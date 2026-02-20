import socket

def grab_banner(ip, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(2)
        s.connect((ip, port))
        banner = s.recv(1024)
        
        print(f"[+] Port {port} Open! Banner: {banner.decode().strip()}")
        s.close()
    except:
        print(f"[-] Port {port} Closed or Filtered.")

target_ip = "scanme.nmap.org"
target_port = [21,22,80]

for p in target_port:
    grab_banner(target_ip, p)