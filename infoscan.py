import socket


# Wiill take user input and scan the host for the specified port
def scan_ports(host, ports):
    for port in ports:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((host, port))
            if result == 0:
                print(f"Port {port} is open")
            sock.close()
        except socket.error:
            print(f"Failed to connect to port {port}")


# This is the "main" function, it will allow the user
# to interact with the program
def main():
    host = input("Enter the host to scan: ")
    print("Select an option:")
    print("1. Scan specific ports")
    print("2. Scan vulnerable ports")
    print("3. Exit")
    option = input("Enter your choice: ")
    # Scanning specific ports chosen by the user
    if option == "1":
        port = int(input("Enter the port to scan: "))
        scan_ports(host, [port])
    # Scanning commonly vulnerable ports
    elif option == "2":
        vulnerable_ports = [20, 21, 23, 25, 53, 80, 137,
                            139, 443, 1433, 1434, 3306, 3389, 8080, 8443]
        scan_ports(host, vulnerable_ports)
    elif option == "3":
        print("Exiting the program...")
    else:
        print("Invalid option")


if __name__ == "__main__":
    main()
