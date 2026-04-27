import socket
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime

target = input("Inserisci IP o dominio: ")

try:
    target_ip = socket.gethostbyname(target)
except socket.gaierror:
    print("Host non valido.")
    exit()

print(f"\nScansione di {target_ip}")
print("-" * 40)

start_time = datetime.now()

# funzione che scansiona una singola porta
def scan_port(port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)

        result = s.connect_ex((target_ip, port))

        if result == 0:
            try:
                banner = s.recv(1024).decode().strip()
            except:
                banner = "N/A"
            print(f"[OPEN] Porta {port} | Servizio: {banner}")

        s.close()
    except:
        pass

# numero di thread (puoi modificarlo)
THREADS = 100

# esecuzione multithreading
with ThreadPoolExecutor(max_workers=THREADS) as executor:
    executor.map(scan_port, range(1, 1025))

end_time = datetime.now()

print("-" * 40)
print(f"Tempo totale: {end_time - start_time}")