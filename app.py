from flask import Flask, request, send_file, render_template_string
import re
import os
import subprocess
import tempfile

app = Flask(__name__)

HTML = '''
<!doctype html>
<title>cURL 下載器</title>
<h2>貼上你的 cURL 指令：</h2>
<form method=post>
  <textarea name=curl_command rows=10 cols=100></textarea><br>
  <input type=submit value="使用cURL下載">
</form>
{% if filename %}
  <p>下載完成：<a href="/download/{{ filename }}">點此下載 {{ filename }}</a></p>
{% endif %}
'''

@app.route('/', methods=['GET', 'POST'])
def index():
    filename = None
    if request.method == 'POST':
        curl_command = request.form['curl_command']
        # 處理多行 cURL 指令：去除行尾的 \ 和換行
        curl_command = curl_command.replace('\\\n', ' ').replace('\\\r\n', ' ')
        match = re.search(r"curl\s+'([^']+)'", curl_command)
        if match:
            url = match.group(1)
            filename = os.path.basename(url)
            if not filename.lower().endswith('.pdf'):
                filename = 'downloaded_file.pdf'
        else:
            filename = 'downloaded_file.pdf'

        # 建立暫存檔案路徑
        tmp_path = os.path.join(tempfile.gettempdir(), filename)
        # 執行 cURL 指令
        process = subprocess.Popen(curl_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        if process.returncode == 0:
            with open(tmp_path, 'wb') as f:
                f.write(stdout)
        else:
            return f"<pre>下載失敗：\n{stderr.decode('utf-8')}</pre>"

        return render_template_string(HTML, filename=filename)
    return render_template_string(HTML, filename=None)

@app.route('/download/<filename>')
def download(filename):
    tmp_path = os.path.join(tempfile.gettempdir(), filename)
    return send_file(tmp_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port=5001)