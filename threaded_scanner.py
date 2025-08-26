import socket
from threading import Thread

# Performing a threaded port scan on a host within a given port range

def threaded_scan(host, start_port=1, end_port=1024):
    open_ports = [] # List to store open ports found

    def scan(port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)  # Timeout for connection attempt
        if s.connect_ex((host, port)) == 0: # Checking if port is open
            open_ports.append(port)
        s.close()

    threads = []

     # Creating and starting a thread for each port :

    for port in range(start_port, end_port + 1):
        t = Thread(target=scan, args=(port,))
        threads.append(t)
        t.start()

    # Wait for all threads to finish :

    for t in threads:
        t.join()

    return sorted(open_ports) # Return the list of open ports in order
