import subprocess
import re
import os

# 從 txt 檔案讀取 cURL 指令
with open('curl_command.txt', 'r') as f:
    curl_command = f.read()

# 從 cURL 指令中找出 URL
match = re.search(r"curl\s+'([^']+)'", curl_command)
if match:
    url = match.group(1)
    filename = os.path.basename(url)
    if not filename.lower().endswith('.pdf'):
        filename = 'downloaded_file.pdf'
else:
    filename = 'downloaded_file.pdf'

# 執行命令
process = subprocess.Popen(curl_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
stdout, stderr = process.communicate()

if process.returncode == 0:
    with open(filename, 'wb') as f:
        f.write(stdout)
    print(f"檔案已成功下載並儲存為 '{filename}'")
else:
    print("執行 cURL 命令時發生錯誤：")
    print(stderr.decode('utf-8'))