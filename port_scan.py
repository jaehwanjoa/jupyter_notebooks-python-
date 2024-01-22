import socket
import concurrent.futures
import os
import sys
import csv

def scan_port(ip, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: #socket 모듈로 TCP 소캣을 생성
        s.settimeout(1)
        try:
            s.connect((ip, port))
            return True
        except:
            return False
 
def port_scanner(ip, start_port, end_port):
    ports = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor: #1~100까지 스레드 생성
        future_to_port = {executor.submit(scan_port, ip, port): port for port in range(start_port, end_port+1)}
        for future in concurrent.futures.as_completed(future_to_port):
            port = future_to_port[future]
            if future.result():
                print(f'Port {port} is open!')
                ports.append(port)
    return ports
 
# Port Scan Test
Target_ip = input("Input Target IP: ")
start_port = input("Input Start Port: ")
end_port = input("Input End Port: ")

# Write csv file
base_path = os.path.abspath(os.path.dirname(sys.argv[0]))
with open(base_path+'results.csv', 'a', encoding='utf-8') as f:
    writer = csv.writer(f)
    open_ports = port_scanner(Target_ip, int(start_port), int(end_port))
    print('Port Open: ', open_ports, file=f)
    #writer.writerows(open_ports)