import socket
import concurrent.futures
import os

def scan_port(ip, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: #socket 모듈로 TCP 소캣을 생성
        s.settimeout(1)
        try:
            s.connect((ip, port))
            return True
        except:
            return False
 
def port_scanner(ip, start_port, end_port):
    resutls = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor: #1~100까지 스레드 생성
        future_to_port = {executor.submit(scan_port, ip, port): port for port in range(start_port, end_port+1)}
        for future in concurrent.futures.as_completed(future_to_port):
            port = future_to_port[future]
            if future.result():
                portinfo = socket.getservbyport(port)
                #print('Port_Open: ', port, 'Port_Info: ', portinfo)
                print('Port_Open: ', port, 'Port_Info: ', portinfo)
                resutls.append(port)
                resutls.append(portinfo)
    return resutls
 
# Port Scan Test
Target_ip = input("Input Target IP: ")
start_port = input("Input Start Port: ")
end_port = input("Input End Port: ")

# Write csv file
open_ports = port_scanner(Target_ip, int(start_port), int(end_port))
print('Results: ', open_ports)
os.system('pause')