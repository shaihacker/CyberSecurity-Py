# --------------------------------------------------------
#   Coded By Shai Halfon                                 -
#   LinkedIn: https://www.linkedin.com/in/shai-halfon/   -
# --------------------------------------------------------

import platform
import socket, ftplib, paramiko

class colors:
    NORMAL = '\033[0m'
    PINK = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    Bold = '\033[1m'

if platform.system() == "Linux" or platform.system() == "Windows":
    while True:
        print(f"[{colors.Bold}{colors.BLUE}Options{colors.NORMAL}]\n\t┗ [{colors.YELLOW}1{colors.NORMAL}] {colors.Bold}Scan Specific Ports{colors.NORMAL}\n\t  [{colors.YELLOW}2{colors.NORMAL}] {colors.Bold}Scan Range Ports{colors.NORMAL}\n\t  [{colors.YELLOW}0{colors.NORMAL}] {colors.Bold}Exit{colors.NORMAL}\n")
        _choice = input(f"[{colors.Bold}{colors.BLUE}Question{colors.NORMAL}] Enter your choice: ")

        if _choice.isdigit():
            if int(_choice) == 1:
                _ip = input(f"[{colors.Bold}{colors.BLUE}Question{colors.NORMAL}] Enter your IP: ")
                _port = input(f"[{colors.Bold}{colors.BLUE}Question{colors.NORMAL}] Enter your specific Port: ")
                _success = False

                def PortScanner(IP, PORT):
                    try:
                        socketX = socket.socket()
                        socketX.connect((IP, PORT))
                        socketX.settimeout(5)

                        print(f"[{colors.Bold}{colors.BLUE}Scanner{colors.NORMAL}] Port {colors.Bold}{PORT}{colors.NORMAL} {colors.Bold}{colors.GREEN}Opened{colors.NORMAL}.")

                    except TimeoutError:
                        print(f"[{colors.Bold}{colors.BLUE}Scanner{colors.NORMAL}] Port {colors.Bold}{PORT}{colors.NORMAL} {colors.Bold}{colors.YELLOW}TimedOut{colors.NORMAL}.")
                    except ConnectionRefusedError:
                        print(f"[{colors.Bold}{colors.BLUE}Scanner{colors.NORMAL}] Port {colors.Bold}{PORT}{colors.NORMAL} {colors.Bold}{colors.RED}Closed{colors.NORMAL}.")

                PortScanner(_ip, int(_port))
                print()

            elif int(_choice) == 2:
                _ip = input(f"[{colors.Bold}{colors.BLUE}Question{colors.NORMAL}] Enter your IP: ")
                _port = input(f"[{colors.Bold}{colors.BLUE}Question{colors.NORMAL}] Enter your Port range (Minimum/Maximum): ")
                _port_s = str(_port).split("/")
                _success = False

                def PortScanner(IP, PORT1, PORT2):
                    for i in range(int(PORT1), int(PORT2) + 1):
                        if _success == True:
                            break
                        elif _success == False:
                            try:
                                socketX = socket.socket()
                                socketX.connect((IP, i))
                                socketX.settimeout(5)

                                print(f"[{colors.Bold}{colors.BLUE}Scanner{colors.NORMAL}] Port {colors.Bold}{i}{colors.NORMAL} {colors.Bold}{colors.GREEN}Opened{colors.NORMAL}.")

                            except TimeoutError:
                                print(f"[{colors.Bold}{colors.BLUE}Scanner{colors.NORMAL}] Port {colors.Bold}{i}{colors.NORMAL} {colors.Bold}{colors.YELLOW}TimedOut{colors.NORMAL}.")
                            except ConnectionRefusedError:
                                print(f"[{colors.Bold}{colors.BLUE}Scanner{colors.NORMAL}] Port {colors.Bold}{i}{colors.NORMAL} {colors.Bold}{colors.RED}Closed{colors.NORMAL}.")

                PortScanner(_ip, int(_port_s[0]), int(_port_s[1]))
                print()

            elif int(_choice) == 0:
                break

            else:
                print(f"[{colors.Bold}{colors.RED}Failed{colors.NORMAL}] Your choice {colors.Bold}{_choice}{colors.NORMAL} are wrong or not existing.\n")
                continue
        else:
            print(f"[{colors.Bold}{colors.RED}Failed{colors.NORMAL}] Your choice {colors.Bold}{_choice}{colors.NORMAL} are not valid!\n\t┗ Your choice should include digits only.\n")
            continue

else:
    print(f"[{colors.Bold}{colors.RED}Failed{colors.NORMAL}] {colors.Bold}AdvPortScanner{colors.NORMAL} are not supported with {colors.Bold}{platform.system()} operation system{colors.NORMAL}.\n\t┗ All the operation systems that are supported:\n\t\t┗ [{colors.YELLOW}1{colors.NORMAL}] {colors.Bold}Windows Operation System{colors.NORMAL}\n\t\t  [{colors.YELLOW}2{colors.NORMAL}] {colors.Bold}Linux Operation System{colors.NORMAL}")
