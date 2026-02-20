import socket

def grab_banner(ip, port):
    try:
        # 1. Inisialisasi socket (AF_INET = IPv4, SOCK_STREAM = TCP)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # 2. Set timeout agar tidak nunggu kelamaan (misal: 2 detik)
        s.settimeout(2)
        
        # 3. Lakukan koneksi ke target (IP dan Port)
        s.connect((ip, port))
        # FIX_ME: Gunakan fungsi s.connect((ip, port))
        
        # 4. Terima data banner dari server (misal 1024 bytes)
        s.recv(1024)
        # FIX_ME: banner = s.recv(1024)
        
        print(f"[+] Port {port} Open! Banner: {grab_banner.decode().strip()}")
        s.close()
    except:
        print(f"[-] Port {port} Closed or Filtered.")

# TARGET TESTING
target_ip = "127.0.0.1" # Coba ke localhost kamu sendiri
target_port = 22        # Coba port SSH atau yang sedang open

grab_banner(target_ip, target_port)